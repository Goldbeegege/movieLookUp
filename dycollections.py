# -*-coding:utf-8-*-
# @author: JinFeng
# @date: 2019/9/26 10:21

import requests
from lxml import etree
import threading
import urllib
import re
from queue import Queue
from queue import Empty


class BaseSpider(object):
    """
    电影查询的基类
    """
    def __init__(self,keyword,type_id,func,task_mount=10):
        """
        :param keyword: 查询的关键词
        :param type_id: 查询的类型，如电影？电视剧等。。。
        :param func: #回调函数，在查询有结果是调用
        :param task_mount: #多线程开启的数量
        """
        self.keyword = keyword
        self.type_id = type_id
        self.task_mount = task_mount
        self.func = func
        self.movies = []
        self.page = None #有些结果不止一页，该变量用于判断是否有分页的存在
        self.q = Queue()
        self.task = []
        self.size = 0
        self.count = 0 #计数器，没完成一个线程记一次数，当计数达到符合要求的线程数时调用回调函数；
        self.movie_type = ["mkv","mp4","3gp","avi","rm","rmvb"] #视频格式类型
        self.header = {
            "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36",
            "Content-Type":"application/x-www-form-urlencoded"
        } #默认的请求头，若不指定请求头，则默认使用该请求头

    def start_request(self):
        #开始处理需要发送的第一个请求
        pass

    def send_request(self,link,method="get",**kwargs):
        """
        :param link: 链接地址
        :param method: 请求方式，get，post等。。。
        :param kwargs: 关键词参数，添加headers，和cookies
        :return:
        """
        if method == "get":
            ret = requests.get(link,timeout=8)
        else:
            ret = requests.post(link,timeout=8,**kwargs)
        return ret

    def handler_response(self,link_list):
        """
        :param link_list:从搜索出的页面获取到所有可能匹配结果的链接列表
        :return:
        """
        for link in link_list:
            self.q.put(link)
        self.size = self.q.qsize()
        self.multi_task()
        #将所有的链接入队列并开启多线程任务

    def multi_task(self):
        #多线程
        #实际上，搜索也中的结果有的可能要不等于指定的任务数量，即self.task_mount
        #所以队列中的结果如果小于self.task_mount，即要提前结束循环
        #如果大于self.task_mount,就取self.task_mount
        for i in range(self.task_mount):
            try:
                link = self.q.get()
                t = threading.Thread(target=self.get_movie,args=(link,self.get_download_link))
                t.start()
                self.task.append(t) #将实际的任务存到一个列表中去
            except Empty:
                break


    def get_movie(self,link,callback):
        #多任务中的每一个子任务，用于获取每部电影的结果
        pass

    def get_download_link(self,ret):
        #获取每部电影的链接
        pass

    def job_done(self):
        #判断所有子线程是否完成
        if self.count == min([self.size,self.task_mount]):
            return True

class DyttSpider(BaseSpider):

    def start_request(self):
        link = "http://s.ygdy8.com/plus/so.php?typeid={}&keyword={}".format(self.type_id,urllib.parse.quote(self.keyword.encode("gbk")))
        ret = self.send_request(link,method="get",headers=self.header)
        if ret is not None:
            html = etree.HTML(ret.text)
            link_list = html.xpath("//div[@class='co_content8']//table//td[2]/b/a/@href")
            if link_list:
                page_list = re.findall(r"<a href=['\"](.*)['\"]>\[\d+\]</a>", ret.text) #获取该页的页码数
                self.handler_response(link_list)
            else:
                self.func([])
            # if page_list and self.page is None:
            #     self.page = page_list

    def get_movie(self,link,callback):
        link = "https://www.ygdy8.com" + link
        res = self.send_request(link,method="get",headers=self.header)
        if res is not None:
            if callable(callback):
                callback(res.content.decode("gbk"))

    def get_download_link(self,ret):
        res_list = re.findall(r"<a .*>(ftp.*)</a>", ret) or re.findall(r"<a .*>(http.*)</a>", ret)

        if len(res_list) == 0:
            condition = r'<a href="(.*)" .*>{}.*</a>'.format(self.keyword)
            res_list = re.findall(condition, ret)
        print(res_list)
        self.movies.extend(res_list)
        self.count += 1
        if self.job_done():
            self.func(self.movies)
            
class SixvdySpider(BaseSpider):
    def start_request(self):
        ret = self.send_request(
            "http://so.hao6v.com/e/search/index.php",
            method="post",
            data={
                "show": "title,Csmalltext",
                "tempid": "1",
                "keyboard": "{}".format(self.keyword).encode("gbk"),
                "tbname": "article",
            },
            headers = self.header
        ).text
        self.get_response(ret)
        
    def get_response(self,s):
        html = etree.HTML(s)
        root_list = html.xpath("//table//font[1]/a")
        if root_list:
            for mov in root_list:
                if self.get_movie_type(mov.text):
                    movie_list = mov.xpath("../span/a")
                    for index,movie in enumerate(movie_list):
                        href = movie.xpath("./@href")[0]
                        self.q.put(href)
            self.size = self.q.qsize()
            self.multi_task()
        else:
            self.func([])
            pass

    def get_movie(self,link,callback):
        response = self.send_request(
            "http://so.hao6v.com" + link,
            method="get",
            headers = self.header
        ).content
        if callable(callback):
            callback(response)

    def get_download_link(self,ret):
        self.count += 1
        try:
            html = etree.HTML(ret.decode("gbk"))
        except UnicodeDecodeError:
            return
        link_list = html.xpath("//table//a")
        links = []
        for link in link_list:
            if self.get_link_name(link.text):
                movie = "[{}]  ".format(link.text) + link.xpath("./@href")[0]
                links.append(movie)
        self.movies.extend(links)
        if self.job_done():
            self.func(self.movies)

    def get_link_name(self,text):
        if self.keyword in text:
            return True
        parts = text.rsplit(".",1)
        if parts[-1] in self.movie_type:
            return True
                        
    def get_movie_type(self,type_title):
        type_list = self.type_id.split("&")
        for tl in type_list:
            if tl in type_title:
                return True
            else:
                continue
        return False
        
if __name__ == '__main__':
    dy = SixvdySpider("黑豹","电影&3D",0)
    dy.start_request()
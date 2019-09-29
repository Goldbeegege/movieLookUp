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
import time


class BaseSpider(object):
    def __init__(self,keyword,type_id,func,task_mount=10):
        self.keyword = keyword
        self.type_id = type_id
        self.task_mount = task_mount
        self.func = func
        self.movies = []
        self.page = None
        self.q = Queue()
        self.task = []
        self.header = {
            "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36",
            "Content-Type":"application/x-www-form-urlencoded"
        }

    def start_request(self):
        pass

    def send_request(self,link,method="get",**kwargs):
        if method == "get":
            ret = requests.get(link,**kwargs)
        else:
            ret = requests.post(link,**kwargs)
        return ret

    def handler_response(self,link_list):
        for link in link_list:
            self.q.put(link)
        self.multi_task()

    def multi_task(self):
        for i in range(self.task_mount):
            time.sleep(0.5)
            try:
                link = self.q.get()
                t = threading.Thread(target=self.get_movie,args=(link,self.get_download_link))
                t.start()
                self.task.append(t)
            except Empty:
                break

    def job_done(self):
        while True:
            [t.isAlive() for t in self.task]

    def get_movie(self,link,callback):
        pass

    def get_download_link(self,ret):
        pass


class DyttSpider(BaseSpider):

    def start_request(self):
        link = "http://s.ygdy8.com/plus/so.php?typeid={}&keyword={}".format(self.type_id,urllib.parse.quote(self.keyword.encode("gbk")))
        ret = self.send_request(link,method="get",headers=self.header).text
        html = etree.HTML(ret)
        link_list = html.xpath("//div[@class='co_content8']//table//td[2]/b/a/@href")
        if link_list:
            page_list = re.findall(r"<a href=['\"](.*)['\"]>\[\d+\]</a>", ret)
            self.multi_task()
        else:
            self.func([])
        # if page_list and self.page is None:
        #     self.page = page_list

    def get_movie(self,link,callback):
        link = "https://www.ygdy8.com" + link
        res = self.send_request(link,method="get",headers=self.header).content.decode("gbk")
        if callable(callback):
            callback(res)

    def get_download_link(self,ret):
        res_list = re.findall(r"<a .*>(ftp.*)</a>", ret)
        if len(res_list) == 0:
            res_list = re.findall(r"<a .*>(http.*)</a>", ret)
        self.movies.extend(res_list)
        if callable(self.func):
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
                        if movie.text is None:
                            movie = movie.xpath("./font")[0]
                        if self.keyword in movie.text:
                            self.q.put(href)
            self.multi_task()
        else:
            self.func([])

    def get_movie(self,link,callback):
        response = self.send_request(
            "http://so.hao6v.com" + link,
            method="get",
            headers = self.header
        ).content
        if callable(callback):
            self.get_download_link(response)

    def get_download_link(self,ret):
        html = etree.HTML(ret.decode("gbk"))
        link_list = html.xpath("//table[1]//a")
        for link in link_list:
            if self.keyword in link.text:
                movie = "[{}]  ".format(link.text) + link.xpath("./@href")[0]
                self.movies.append(movie)
        self.func([])


                        
    def get_movie_type(self,type_title):
        type_list = self.type_id.split("&")
        for tl in type_list:
            if tl in type_title:
                return True
            else:
                continue
        return False
        
if __name__ == '__main__':
    dy = SixvdySpider("蜘蛛侠","电影&3D",0)
    dy.start_request()
    print(dy.movies)
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
        self.size = 0
        self.count = 0
        self.movie_type = ["mkv","mp4","3gp","avi","rm","rmvb"]
        self.header = {
            "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36",
            "Content-Type":"application/x-www-form-urlencoded"
        }

    def start_request(self):
        pass

    def send_request(self,link,method="get",**kwargs):
        try:
            if method == "get":
                ret = requests.get(link,timeout=8)
            else:
                ret = requests.post(link,**kwargs,timeout=8)
            return ret
        except requests.exceptions.ConnectTimeout:
            print("timeout")
            return None
        except requests.exceptions.ReadTimeout:
            print("readTimeOut")

    def handler_response(self,link_list):
        for link in link_list:
            self.q.put(link)
        self.size = self.q.qsize()
        self.multi_task()

    def multi_task(self):
        for i in range(self.task_mount):
            try:
                link = self.q.get()
                t = threading.Thread(target=self.get_movie,args=(link,self.get_download_link))
                t.start()
                self.task.append(t)
            except Empty:
                break


    def get_movie(self,link,callback):
        pass

    def get_download_link(self,ret):
        pass

    def job_done(self):
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
                page_list = re.findall(r"<a href=['\"](.*)['\"]>\[\d+\]</a>", ret.text)
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
        res_list = re.findall(r"<a .*>(ftp.*)</a>", ret)
        if len(res_list) == 0:
            res_list = re.findall(r"<a .*>(http.*)</a>", ret)
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
        print(ret)
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
        link_list = html.xpath("//table[1]//a")
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
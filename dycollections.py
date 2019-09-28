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


class DyttSpider(object):
    def __init__(self,keyword,type_id,func):
        print(keyword)
        self.keyword = urllib.parse.quote(keyword.encode("gbk"))
        self.type_id = type_id
        self.func = func
        self.movies = []
        self.page = None


    def send_request(self,link):
        ret = requests.get(link)
        return ret

    def start_request(self):
        link = "http://s.ygdy8.com/plus/so.php?typeid={}&keyword={}".format(self.type_id,self.keyword)
        ret = self.send_request(link).text
        html = etree.HTML(ret)
        link_list = html.xpath("//div[@class='co_content8']//table//td[2]/b/a/@href")
        if link_list:
            self.mutil_task(link_list)
            page_list = re.findall(r"<a href=['\"](.*)['\"]>\[\d+\]</a>",ret)

        else:
            self.func([])
        # if page_list and self.page is None:
        #     self.page = page_list


    def mutil_task(self,tasks):
        for link in tasks:
            t = threading.Thread(target=self.get_response, args=(link, self.get_movie))
            t.start()

    def get_response(self,link,callback):
        link = "https://www.ygdy8.com" + link
        res = self.send_request(link).content.decode("gbk")
        if callable(callback):
            callback(res)

    def get_movie(self,ret):
        res_list = re.findall(r"<a .*>(ftp.*)</a>", ret)
        if len(res_list) == 0:
            res_list = re.findall(r"<a .*>(http.*)</a>", ret)
        self.movies.extend(res_list)
        if callable(self.func):
            self.func(self.movies)
            
class SixvdySpider(object):
    
    def __init__(self,keyword,type_id,func):
        self.keyword = keyword
        self.type_id = type_id
        self.func = func
        self.q = Queue()
    def start_request(self):
        ret = requests.post(
            "http://so.hao6v.com/e/search/index.php",
            data={
                "show":"title,Csmalltext",
                "tempid":"1",
                "keyboard":"{}".format(self.keyword).encode("gbk"),
                "tbname":"article",
            },
            headers={
                "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36",
                "Content-Type":"application/x-www-form-urlencoded",
            },
        ).text
        self.get_response(ret)
        
    def get_response(self,s):
        link_list = []
        html = etree.HTML(s)
        root_list = html.xpath("//table//font[1]/a")
        for mov in root_list:
            if self.get_movie_type(mov.text):
                movie_list = mov.xpath("../span/a")
                for index,movie in enumerate(movie_list):
                    href = movie.xpath("./@href")[0]
                    if movie.text is None:
                        movie = movie.xpath("./font")[0]
                    if self.keyword in movie.text:
                        self.q.put(href)
        self.mutil_task()

    def mutil_task(self):
        for i in range(10):
            time.sleep(0.5)
            try:
                link = self.q.get()
                t = threading.Thread(target=self.get_movie,args=(link,))
                t.start()
            except Empty:
                break

    def get_movie(self,link):
        response = requests.get(
                "http://so.hao6v.com"+link,
                headers={
                        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36",
                        "Content-Type":"application/x-www-form-urlencoded",
                    },
            ).content
        html = etree.HTML(response.decode("gbk"))
        link_list = html.xpath("//table[1]//a")
        for link in link_list:
            if self.keyword in link.text:
                print("[{}]  ".format(link.text) + link.xpath("./@href")[0])

                        
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
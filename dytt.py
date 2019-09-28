# -*-coding:utf-8-*-
# @author: JinFeng
# @date: 2019/9/26 10:21

import requests
from lxml import etree
import threading
import urllib
import re


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

if __name__ == '__main__':
    dy = DyttSpider("名侦探柯南")
    dy.start_request()
# -*-coding:utf-8-*-
# @author: JinFeng
# @date: 2019/9/26 15:33

import requests
# from lxml import etree
import re
#
# ret = requests.get("http://s.ygdy8.com/plus/so.php?typeid=1&keyword=%C3%FB%D5%EC%CC%BD%BF%C2%C4%CF").text
# res = re.findall(r"<a href=['\"](.*)['\"]>\[\d+\]</a>",ret)
# print(res)
# # html = etree.HTML(ret)
# # ret_list = html.xpath("//table[last()]")
# # for i in ret_list:
# #     print(i)
# import os
# ret = os.system('"D:\Program Files (x86)\Thunder9\Program\ThunderStart.exe" -StartType:DesktopIcon')
# pid = os.getpid()
# print(pid)
# print(ret)

# ret = requests.get("http://s.ygdy8.com/plus/so.php?typeid=16&keyword=%BB%F0%D3%B0%C8%CC%D5%DF").text
# res = re.findall(r"<a href=['\"](.*)['\"]>\[\d+\]</a>", ret)
# print(res)

# import os
#
# ret = os.path.expanduser("~")
# print(ret)
import time

ret = requests.post(
    "http://so.hao6v.com/e/search/index.php",
    data={
        "show":"title,Csmalltext",
        "tempid":"1",
        "keyboard":"蜘蛛侠".encode("gbk"),
        "tbname":"article",
    },
    headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36",
        "Content-Type":"application/x-www-form-urlencoded",
    },
).text
print(ret)
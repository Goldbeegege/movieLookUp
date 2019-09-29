# -*-coding:utf-8-*-
# @author: JinFeng
# @date: 2019/9/26 16:44

import sys 
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from dycollections import DyttSpider,SixvdySpider
import threading
import os



class DyttSpiderUi(QMainWindow):
    def __init__(self,*args,**kwargs):
        super(DyttSpiderUi, self).__init__(*args,**kwargs)
        self.resize(800,400)

        self.topWidget = QWidget()
        self.topLayout = QHBoxLayout()

        self.lineEdit = QLineEdit()
        self.lineEdit.setPlaceholderText("请输入关键词...")

        self.combox = QComboBox()
        self.combox.addItems(["电影","电视剧","综艺","旧综艺","游戏","动漫"])

        self.btn = QPushButton("搜索")
        self.btn.setStyleSheet("border-radius:4px;border:1px solid red;")
        self.btn.clicked.connect(self.get_start)

        self.label = QLabel("未开始查询...")
        self.label.setStyleSheet("color:blue;font-weight:bold")
        self.qlist = QListWidget()
        # self.qlist.addItems(["hah","111"])
        self.qlist.itemDoubleClicked.connect(self.down_load)

        self.topLayout.addWidget(self.lineEdit)
        self.topLayout.addWidget(self.combox)
        self.topLayout.addWidget(self.btn)
        self.topWidget.setLayout(self.topLayout)

        self.status = self.statusBar()
        self.status.setStyleSheet("color:red;font-weight:bold")


        self.centerLayout = QVBoxLayout()
        self.centerLayout.addWidget(self.topWidget)
        self.centerLayout.addWidget(self.label)
        self.centerLayout.addWidget(self.qlist)
        self.centerWidget = QWidget()
        self.centerWidget.setLayout(self.centerLayout)
        self.setCentralWidget(self.centerWidget)

        self.typeMap = {
            0:"1",
            1:"2",
            2:"99",
            3:"89",
            4:"19",
            5:"16"
        }
        self.spider = None

    def down_load(self,item):
        print(item.text())

        clipBoard = QApplication.clipboard()
        clipBoard.setText(item.text())
        self.status.showMessage("复制成功",3000)


    def callback(self,movie_list):
        if movie_list:
            msg = "搜索结果：1页共{}个结果;双击电影名称即可复制到剪切板，请先打开迅雷！".format(len(movie_list))
        else:
            msg = "搜索结束！未搜索到相关结果！"
        self.new_thread(msg)
        t = threading.Thread(target=self.insertValue,args=(self.spider.movies,))
        t.start()


    def insertValue(self,movies):
        self.qlist.clear()
        self.qlist.addItems(movies)

    def log_result(self,movie_list):
        self.qlist.clear()
        self.qlist.addItems(movie_list)

    def dispatch(self):
        keyword = self.lineEdit.text()
        if keyword:
            t1 = threading.Thread(target=self.log_msg, args=("开始搜索请稍后...",))
            t1.setDaemon(True)
            t1.start()
            t2 = threading.Thread(target=self.get_start,args=(keyword,))
            t2.start()


    def get_start(self):
        keyword = self.lineEdit.text()
        print(keyword)
        if keyword:
            self.new_thread("开始搜索请稍后...")
            # index = self.combox.currentIndex()
            # type_id = self.typeMap[index]
            # spider = DyttSpider(keyword,type_id,self.callback)
            t = threading.Thread(target=self.start_request,args=(keyword,"电影&3D",self.callback))
            t.start()

    def start_request(self,keyword,type_id,callback):
        self.spider = SixvdySpider(keyword, type_id, callback)
        self.spider.start_request()

    def new_thread(self,msg):
        t1 = threading.Thread(target=self.log_msg, args=(msg,))
        t1.setDaemon(True)
        t1.start()

    def log_msg(self,msg):
        self.label.setText(msg)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DyttSpiderUi()
    window.show()
    sys.exit(app.exec_())
# -*-coding:utf-8-*-
# @author: JinFeng
# @date: 2019/9/26 16:44

import sys 
from PyQt5.QtWidgets import *
from dycollections import DyttSpider,SixvdySpider
import threading



class DyttSpiderUi(QMainWindow):
    def __init__(self,*args,**kwargs):
        super(DyttSpiderUi, self).__init__(*args,**kwargs)
        self.originMap = {
            1: DyttSpider,
            0: SixvdySpider
        }

        self.typeMap = {
            DyttSpider: {
                0: "1",
                1: "2",
                2: "99",
                3: "89",
                4: "19",
                5: "16"
            },
            SixvdySpider: {
                0: "电影&3D",
                1: "国产剧",
                2: "日剧&韩剧",
                3: "美剧&欧剧"
            }
        }

        self.movie_type = {
            1:["电影", "电视剧", "综艺", "旧综艺  ", "游戏", "动漫"],
            0:["电影&3D", "国产剧", "日剧&韩剧", "美剧&欧剧"]
        }


        self.topWidget = QWidget()
        self.topLayout = QHBoxLayout()

        self.lineEdit = QLineEdit()
        self.lineEdit.setPlaceholderText("请输入关键词...")


        self.combox1 = QComboBox()
        self.combox1.addItems(["6v电影","电影天堂"])
        self.combox1.setToolTip("请选择片源")
        self.combox1.currentIndexChanged.connect(self.change_origin)

        self.combox2 = QComboBox()
        self.combox2.addItems(self.movie_type[0])
        self.combox2.setToolTip("请选择类型")

        self.btn = QPushButton("搜 索")
        self.btn.setStyleSheet("color:blue;font-weight:bold")
        self.btn.clicked.connect(self.get_start)

        self.label = QLabel("未开始查询...")
        self.label.setStyleSheet("color:blue;font-weight:bold")
        self.qlist = QListWidget()
        self.qlist.itemDoubleClicked.connect(self.down_load)

        self.topLayout.addWidget(self.lineEdit)
        self.topLayout.addWidget(self.combox1)
        self.topLayout.addWidget(self.combox2)
        self.topLayout.addWidget(self.btn)
        self.topWidget.setLayout(self.topLayout)

        self.status = self.statusBar()
        self.status.setStyleSheet("color:red;font-weight:bold")
        screen_size = QDesktopWidget().screenGeometry()
        window_size = self.geometry()
        x = (screen_size.width() - window_size.width())/2
        y = (screen_size.height() - window_size.height())/2
        self.resize(window_size.width()+100, window_size.height())
        self.move(x-50,y)

        self.centerLayout = QVBoxLayout()
        self.centerLayout.addWidget(self.topWidget)
        self.centerLayout.addWidget(self.label)
        self.centerLayout.addWidget(self.qlist)
        self.centerWidget = QWidget()
        self.centerWidget.setLayout(self.centerLayout)
        self.setCentralWidget(self.centerWidget)
        self.setWindowTitle("电影搜索")

    def change_origin(self,index):
        self.combox2.clear()
        self.combox2.addItems(self.movie_type[index])

    def down_load(self,item):
        clipBoard = QApplication.clipboard()
        clipBoard.setText(item.text())
        self.status.showMessage("复制成功",3000)


    def callback(self,movie_list):
        if movie_list:
            msg = "搜索结果：1页共{}个结果;双击电影名称即可复制到剪切板，请先打开迅雷！".format(len(movie_list))
        else:
            msg = "搜索结束！未搜索到相关结果！"
        self.new_thread(msg)
        t = threading.Thread(target=self.insertValue,args=(movie_list,))
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
            t1.start()
            t2 = threading.Thread(target=self.get_start,args=(keyword,))
            t2.start()


    def get_start(self):
        #点击搜索按钮后
        #若输入框是空的，则不作任何操作
        #若不是空的，则首先改变状态信息
        #接着开始发送请求
        keyword = self.lineEdit.text()
        origin = self.combox1.currentIndex()
        origin_type = self.originMap[origin]
        if keyword:
            index = self.combox2.currentIndex()
            type_id = self.typeMap[origin_type].get(index)
            self.new_thread("开始搜索请稍后...",)
            t = threading.Thread(target=self.start_request,args=(keyword,type_id,origin_type,self.callback))
            t.start()

    def start_request(self,keyword,type_id,origin,callback):
        spider = origin(keyword, type_id, callback)
        spider.start_request()

    def new_thread(self,msg):
        t1 = threading.Thread(target=self.log_msg, args=(msg,))
        t1.setDaemon(True)
        t1.start()

    def log_msg(self,msg):
        #改变状态信息
        self.label.setText(msg)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DyttSpiderUi()
    QMessageBox.information(window,"提示信息","本软件仅供学习交流使用，请勿做商业用途"+"\n"+"若有疑问或建议请联系作者邮箱："+"\n"+"jinfengxuancheng@163.com"+"\n"+"谢谢！")
    window.show()
    sys.exit(app.exec_())
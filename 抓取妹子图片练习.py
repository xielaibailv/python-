import urllib.request
import os

# def download():
url ="http://jandan.net/ooxx/"
req = urllib.request.Request(url)
req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36')
response = urllib.request.urlopen(req)
html = response.read().decode('utf-8')
print(html)

#为什么通过代码获取到的html里的内容里没有了图片的真正链接，和f12看到的不一样，不知道
#感觉这里超出了自己的所知范围，以后再来看
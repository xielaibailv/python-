#-*- coding:utf-8 -*-

from urllib.request import Request,urlopen
import urllib.parse
from urllib.error import URLError
import csv
import sys



url = "https://www.google.com.hk/async/irc?vet=10ahUKEwj-psvV86DeAhUljVQKHVffALMQo0EIqQE..i&ved=0ahUKEwj-psvV86DeAhUljVQKHVffALMQo0EIqQE&safe=strict&yv=3&q={}&bih=150&biw=1920&async=iu:0,_id:irc_async,_pms:s,_fmt:pc.format.quote('猫')"

head = {
    "accept" : "*/*",
    "accept-encoding" : "gzip, deflate, br",
    "accept-language" : "zh-CN,zh;q=0.9",
    "method" : "GET",
    "referer" : "https://www.google.com/",
    "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36"
}
# data = {}
# data['q'] = '猫'
# data = urllib.parse.urlencode(data)

req = Request(url,head)
try:
    response = urlopen(req).encode('utf-8')
except URLError as e:
    if hasattr(e,'reason'):
        print('连接有问题。')
        print('reason:',e.reason)
    elif hasattr(e,'code'):
        print('请求失败。')
        print('code:',e.code)
else:
    print('OK')
    html = response.read().decode('utf-8')
    print(html)



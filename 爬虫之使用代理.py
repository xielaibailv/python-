#使用代理进行网页访问

import urllib.request
import random


#这个ip会返回你使用的ip
url = 'https://www.whatismyip.com'
iplist = ['124.78.234.28','106.75.226.36','125.70.13.77']
proxy_support = urllib.request.ProxyHandler({'http':random.choice(iplist)})

opener = urllib.request.build_opener(proxy_support)
opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36')]
urllib.request.install_opener(opener)

response = urllib.request.urlopen(url)
html = response.read().decode('utf-8')

print(html)


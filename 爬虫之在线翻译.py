#translation

import urllib.request
import urllib.parse
import json

#复制网址
url= 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
#下面的信息都是form data里的，前面加上data[],所有内容用引号引起来
#data参数如果赋值，就是以post方式发起请求
data = {}
data['type'] = 'AUTO'
data['i'] = '我爱中国！'
data['doctype'] = 'json'
data['version'] = '2.1'
data['keyfrom'] =  'fanyi.web'
#这一参数“ue”在有道的信息里是没有的
data['ue'] = 'UTF-8'
data['typoResult'] = 'false'
#利用parse模块（这是一点单独模块，需要导入）将结果编码成utf-8，并赋值给data
#encode: 将Unicode编码成后面跟着的形式
#decode: 将所有编码形式解码成Unicode
#      decode                          encode
#str ---------> str(Unicode) ---------> str
data = urllib.parse.urlencode(data).encode('utf-8')

response = urllib.request.urlopen(url,data)
html = response.read().decode('utf-8')

print(html)



#上面的代码返回的是一串字典格式的字符串，不太直观；下面是改进的版本
# 将需要翻译的内容参数化
# url= 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
# content = input("请输入想要翻译的内容：")
# data = {}
# data['type'] = 'AUTO'
# data['i'] = content
# data['doctype'] = 'json'
# data['version'] = '2.1'
# data['keyfrom'] =  'fanyi.web'
# data['ue'] = 'UTF-8'
# data['typoResult'] = 'false'
# data = urllib.parse.urlencode(data).encode('utf-8')
#
# response = urllib.request.urlopen(url,data)
# html = response.read().decode('utf-8')
#
# #将结果以json格式付给target，然后只打印翻译结果tgt参数
# target = json.loads(html)
# print("翻译结果：%s" % (target['translateResult'][0][0]['tgt']))
#translation

import urllib.request
import urllib.parse
import json
import time

'''
第一版代码
复制网址
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
'''




'''
第二版代码
上面的代码返回的是一串字典格式的字符串，不太直观；下面是改进的版本
将需要翻译的内容参数化
url= 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
content = input("请输入想要翻译的内容：")

data = {}
data['type'] = 'AUTO'
data['i'] = content
data['doctype'] = 'json'
data['version'] = '2.1'
data['keyfrom'] =  'fanyi.web'
data['ue'] = 'UTF-8'
data['typoResult'] = 'false'
data = urllib.parse.urlencode(data).encode('utf-8')

response = urllib.request.urlopen(url,data)
html = response.read().decode('utf-8')

#将结果以json格式付给target，然后只打印翻译结果tgt参数
target = json.loads(html)
print("翻译结果：%s" % (target['translateResult'][0][0]['tgt']))
'''


'''
#第三版代码
#修改headers的user-agent信息
url= 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
content = input("请输入想要翻译的内容：")


#获取到header里的信息
head = {}
head['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36'

data = {}
data['type'] = 'AUTO'
data['i'] = content
data['doctype'] = 'json'
data['version'] = '2.1'
data['keyfrom'] =  'fanyi.web'
data['ue'] = 'UTF-8'
data['typoResult'] = 'false'
data = urllib.parse.urlencode(data).encode('utf-8')

# #使用第一种办法：通过Request的headers参数修改，直接将header信息以字典形式传入
# #将head信息传入request
# req = urllib.request.Request(url,data,head)


#第二种办法：先生成req，再利用Request.add_header()增加header
req = urllib.request.Request(url,data)
req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36')

response = urllib.request.urlopen(req)
html = response.read().decode('utf-8')

#将结果以json格式付给target，然后只打印翻译结果tgt参数
target = json.loads(html)
print("翻译结果：%s" % (target['translateResult'][0][0]['tgt']))
'''




#第四版代码，延迟提交时间
# 需要time模块
#修改headers的user-agent信息
while True:
    content = input('请输入想要翻译的内容(退出程序请按"q!")：')
    if content == 'q!':
        break

    url= 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
    #获取到header里的信息
    head = {}
    head['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/' \
                         '537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36'

    data = {}
    data['type'] = 'AUTO'
    data['i'] = content
    data['doctype'] = 'json'
    data['version'] = '2.1'
    data['keyfrom'] =  'fanyi.web'
    data['ue'] = 'UTF-8'
    data['typoResult'] = 'false'
    data = urllib.parse.urlencode(data).encode('utf-8')

    #使用第一种办法：通过Request的headers参数修改，直接将header信息以字典形式传入
    #将head信息传入request
    req = urllib.request.Request(url,data,head)


    # #第二种办法：先生成req，再利用Request.add_header()增加header
    # req = urllib.request.Request(url,data)
    # req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36')
    #
    response = urllib.request.urlopen(req)
    html = response.read().decode('utf-8')

    #将结果以json格式付给target，然后只打印翻译结果tgt参数
    target = json.loads(html)
    print("翻译结果：%s" % (target['translateResult'][0][0]['tgt']))

    time.sleep(5)




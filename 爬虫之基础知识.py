# -*- coding:utf-8 _*-

#   author : YOYO
#   time :  2020/6/19 16:25
#   email : youyou.xu@enesource.com
#   project_name :  python-study
#   file_name :  爬虫之基础知识
#   function： 主要完成下面3个小功能
#   1，直接打印读取的页面数据（  前300个字符）
#   2.判断某个网址的编码方法
#   3.依次爬取url文件中的网址，并将内容保存为txt文件

from urllib import request
import chardet  # 检测字符串的编码


def fun1():
    url = 'http://www.fishc.com'
    html_response = request.urlopen(url=url)
    data = html_response.read()   # 可以直接在read里传字节数  read(300)
    print(data[:300])


def fun2():
    url = input('请输入url：')
    data = request.urlopen(url=url).read()
    bm = chardet.detect(data)
    print('该网页使用的编码是：{}'.format(bm['encoding']))


def fun3():
    with open(r'E:\桌面\PycharmProjects\python-study\url.txt') as f:
        url = f.readlines()
        # 小甲鱼代码是使用 url = r.read().spiltlines() 说是按照换行符分割，不清楚这样和上面直接读取每行有什么不同

    for index in range(len(url)):
        data = request.urlopen(url[index]).read()
        file = 'url_' + str(index + 1) + '.txt'
        with open(file, 'w') as f:
            f.write(str(data))
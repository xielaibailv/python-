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
#   4. 从百度百科里爬取链接
#   5,增加图形界面，搜索用户输入的关键字，将结果打印出来

from urllib import request,parse
import chardet  # 检测字符串的编码
from bs4 import BeautifulSoup
import re
import easygui


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


def fun4():
    url = "http://baike.baidu.com/view/284853.htm"
    html = request.urlopen(url)
    data = html.read()
    soup = BeautifulSoup(data, 'html.parser')  # 默认解析
    # 使用正则，提取包含view的链接
    a_link = soup.find_all(href=re.compile("view"))
    # a_link = soup.find_all("a")

    for each in a_link:
        try:
            print(each.text, "-->", "".join(["http://baike.baidu.com", each["href"]]))
        except KeyError:   # 有的链接没有text，会报错，所以要忽略
            pass


def fun5():
    word = easygui.enterbox("请输入你想搜索的关键字：")
    word = parse.urlencode({"word": word})
    response = request.urlopen("http://baike.baidu.com/search/word?%s" % word)
    html = response.read()
    soup = BeautifulSoup(html, "html.parser")
    if soup.h2:  # 如果有副标题(h2)，则把标题和副标题,以及文本打印出来
        # find()和 find_all() 均不能直接使用class=''这样的方式来查找，因为class是python的保留字，需要写成class_
        # 到底是content 还是text，是根据前面是按照soup文件里的查找还是html里的参数查找
        # text = ' '.join([soup.h1.text, soup.h2.text, "\n", soup.find(attrs={"name": "description"})["content"]])
        text = ' '.join([soup.h1.text, soup.h2.text, "\n", soup.find(class_="lemma-summary").text])
        easygui.textbox(msg="查询结果如下：", text=text)


fun5()
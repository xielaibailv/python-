# -*- coding:utf-8 _*-
""" 
#   author : YOYO
#   time :  2019/7/9 16:01
#   email : youyou.xu@enesource.com
#   project_name :  python-study
#   file_name :  爬取笔趣阁小说
#   function： 
"""

import os
from bs4 import BeautifulSoup
import requests
import re
from random import choice
from time import sleep
import threading

key = input('请输入小说名称：')
path = os.getcwd() + '\\' + re.sub(r'[:：\\/*?<>|")]', '-', key)
headers = [
    {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'},
    {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'},
    {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0'},
    {'User-Agent': 'Opera/9.80 (Windows NT 6.1; U; zh-cn) Presto/2.9.168 Version/11.50'}
]


class Get_Proxy_Ip:

    def __init__(self):

        self.proxy = []
        self.url = 'https://www.kuaidaili.com/free/inha'

    def create_proxy_ip_headers(self):  # 随机生成ip和请求头
        try:
            wb_date = requests.get(url=self.url, headers=choice(headers), verify=True).text
            soup = BeautifulSoup(wb_date, 'lxml')
            for index in soup.find_all(attrs={'data-title': "IP"}):
                self.proxy.append(index.string)
            return {'https': choice(self.proxy) + ':8060'}
        except:
            return {'https': '112.111.96.219:8060'}


class Down_story:

    def __init__(self):
        self.url = "http://www.xbiquge.la"

    def get_all_titles_and_url(self):

        try:
            wb_date = requests.get(url=self.url + '/xiaoshuodaquan/', headers=choice(headers),
                                   proxies=Get_Proxy_Ip().create_proxy_ip_headers())
            wb_date.encoding = 'utf-8'
            soup = BeautifulSoup(wb_date.text, 'lxml')
            all_titles = []
            all_urls = []
            for tag in soup.find_all('li'):
                if re.match(r'(http://www.xbiquge.la/)(\d+)', tag.a.get('href')):
                    all_urls.append(tag.a['href'])
                    all_titles.append(tag.string)
            all_pages = dict(zip(all_titles, all_urls))
            if all_pages.get(key):
                return key, all_pages.get(key)
            else:
                return all_titles
        except:
            pass

    def get_stroy_data(self):
        try:
            if isinstance(self.get_all_titles_and_url(), tuple):
                wb_date = requests.get(url=self.get_all_titles_and_url()[1], headers=choice(headers),
                                       proxies=Get_Proxy_Ip().create_proxy_ip_headers())
                wb_date.encoding = 'utf-8'
                soup = BeautifulSoup(wb_date.text, 'lxml')
                page_url = []
                page_title = []
                for title in soup.find_all('dd'):
                    page_title.append(title.string)
                for url in soup.find_all('dd'):
                    page_url.append(url.a.get('href'))
                return page_url, page_title
            else:
                return self.get_all_titles_and_url()
        except:
            pass

    def downloads_story(self):

        if not os.path.exists(path):
            os.makedirs(path)
            print('正在为您创建小说路径，当前路径为：{}'.format(path))
            sleep(1)
            print('目录创建成功，正在查询小说', '*' * 20, '<{}>'.format(key), '*' * 20, '...请稍等', '\n' * 3)
            try:
                if isinstance(self.get_stroy_data(), tuple):
                    story_name = self.get_stroy_data()[1]
                    for index, url in enumerate(self.get_stroy_data()[0]):
                        story_wb_date = requests.get(self.url + url, headers=choice(headers),
                                                     proxies=Get_Proxy_Ip().create_proxy_ip_headers())
                        story_wb_date.encoding = 'utf-8'
                        story_wb_date = story_wb_date.text
                        soup = BeautifulSoup(story_wb_date, 'lxml')
                        for content in soup.find_all(id="content"):
                            if index < len(story_name):
                                with open(path + '\\' + '{}.txt'.format(story_name[index]), 'w', encoding='utf-8') as f:
                                    print('正在下载：{}'.format(story_name[index]))
                                    f.write(content.get_text())
                                    sleep(0.1)
                                    print('{}已经下载完成，准备下载{}'.format(story_name[index], story_name[index + 1]))

                            else:
                                return ('\n  恭喜你哦，已下载完成啦......over')
                else:
                    print('未找到您所需要查询的小说,本次即将爬虫结束,3秒后将打印所有小说目录........ ^_^', '\n' * 3)
                    sleep(3)

                    return (self.get_stroy_data())
            except:
                pass
        else:
            return '当前目录已经存在，爬虫结束'


if __name__ == '__main__':
    print(Down_story().downloads_story())

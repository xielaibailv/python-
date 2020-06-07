# -*- coding:utf-8 _*-
#!/usr/bin/python3

#   author : YOYO
#   time :  2020/6/7 10:44
#   email : youyou.xu@enesource.com
#   project_name :  python-study 
#   file_name :  myfirstwork.py
#   function： 首次自己编写一个带界面的查找电脑里的文档的小工具

import easygui
import os
import sys



file = easygui.fileopenbox(default="F:\桌面\PycharmProjects\python-study\赞美.txt")
if easygui.boolbox:
    easygui.textbox(msg="test", title="文件内容如下", text=file)
else:
    sys.exit(0)

# 在目录下查找匹配的文件并返回其路径
class SearchFile():
    def searchfile(self, defaultdir, target):
        choice = []
        os.chdir(defaultdir)

        for each in os.listdir(os.curdir):
            if target in each:
                choice.append(defaultdir + each)
            if os.path.isdir(each):
                self.searchfile(each, target)
                os.chdir(os.pardir)
        return choice

class InterFace:
    def searchfileface(self):
        defaultdir = easygui.enterbox(msg="请输入你想查找的文件目录：")
        target = easygui.enterbox(msg=("请输入你想要查找的文件名："))
        choice = SearchFile().searchfile(defaultdir, target)
        resultbox = easygui.choicebox(msg="在{}路径下搜索到的符合条件的文档如下：".format(defaultdir), choices=choice)
        # if easygui.:
        #     os.chdir()
        # else:
        #     sys.exit(0)


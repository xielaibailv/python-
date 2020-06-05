import easygui
import sys


easygui.msgbox("hello world")
msg = "今天午饭吃什么？"
title = '吃饭'
choices = ["黄焖鸡", "酸辣笋尖炒粉", "麻辣烫"]

choice = easygui.choicebox(msg, title, choices)

msg = ("你点的这个呀，我也喜欢吃，一起去吧")
title = "go"
if easygui.ccbox(msg,title):
    pass
else:
    sys.exit(0)
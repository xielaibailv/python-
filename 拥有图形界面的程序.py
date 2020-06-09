# -*- coding:utf-8 _*-
#!/usr/bin/python3

#   author : YOYO
#   time :  2020/6/7 19:10
#   email : youyou.xu@enesource.com
#   project_name :  python-study 
#   file_name :  拥有图形界面的程序.py
#   function： 把之前的程序，加上easygui，使之可以通过界面互动
# No1: 猜数字
# No2: 用户登录的对话框
# No3: 打开某个文本文件，读取里面的内容
# No4: 用户点击“OK”按钮的时候，比较当前文件是否修改过，如果修改过，则提示“覆盖保存”、”放弃保存”或“另存为…”
# No5: 统计自己的代码量-----因为有属性，新开一个文件


import easygui
import sys
import random
import os


class InterFaceGame:
    # 猜数字游戏界面版
    def guessnum1(self):
        secret = random.randint(1, 9)
        times = 3

        num = easygui.integerbox("来猜猜小公主我现在心里想的是哪一个数字：", title="猜数字", lowerbound=1, upperbound=9)
        while (num != secret) and (times > 0):
            times -= 1
            if num == secret:
                easygui.msgbox("你是小公主我肚子里的蛔虫吗？？！！")
                break
            elif num > secret:
                    easygui.msgbox("大了", title="游戏结果")
            elif num < secret:
                    easygui.msgbox("小了", title="游戏结果")
            if times > 0:
                num = easygui.integerbox("重新输吧：", title="猜数字", lowerbound=1, upperbound=9)
            else:
                easygui.msgbox("次数用光了")
        exitgame = easygui.boolbox("游戏结束", choices=["退出游戏", "取消"])
        if exitgame:
            sys.exit(0)
        else:
            pass

    def guessnum2(self):
        secret = random.randint(1, 9)
        times = 3

        num = easygui.integerbox("来猜猜小公主我现在心里想的是1-9里哪一个数字：：", title="猜数字", lowerbound=1, upperbound=9)
        if num == secret:
            easygui.msgbox("你是小公主我肚子里的蛔虫吗？？！！")
        else:
            while num != secret:
                times -= 1
                if num > secret:
                        easygui.msgbox("大了", title="游戏结果")
                elif num < secret:
                        easygui.msgbox("小了", title="游戏结果")
                if times > 0:
                    easygui.msgbox("总共 3 次机会，你还剩下 %d 次机会哦" % times)
                    num = easygui.integerbox("重新输吧：", title="猜数字", lowerbound=1, upperbound=9)
                else:
                    easygui.msgbox("次数用光了")
                    break
            else:
                easygui.msgbox("终于猜对了呀，哼，真是的，居然不是一次就中，你根本不爱我！")
        exitgame = easygui.boolbox("游戏结束辣", choices=["退出游戏", "再玩一次"])
        if exitgame:
            sys.exit(0)
        else:
            self.guessnum2()

    # 写一个用户登录的对话框
    def login1(self):
        field_name = ["*用户名", "*真实姓名", "固定电话", "*手机号码", "QQ", "E-mail"]
        # field_values = []
        field_values = easygui.multenterbox("请输入以下信息：", title="账号中心", fields=field_name)

        while True:
            errmsg = ""
            for each in range(len(field_name)):
                option = field_name[each]
                if field_values[each] == "" and option[0] == "*":
                    errmsg += ("[ %s ]为必填项。\n" % field_name[each])
            if errmsg == "":
                break
            field_values = easygui.multenterbox(errmsg, title="账号中心", fields=field_name, values=field_values)

    # 小甲鱼的代码
    def login2(self):
        msg = "请填写以下联系方式"
        title = "账号中心"
        field_name = [" *用户名", " *真实姓名", "  固定电话", " *手机号码", "  QQ", " *E-mail"]
        fieldValues = []
        field_values = easygui.multenterbox(msg, title, field_name)

        while 1:
            if field_values == None:
                break
            errmsg = ""
            for i in range(len(field_name)):
                option = field_name[i].strip()
                if field_values[i].strip() == "" and option[0] == "*":
                    errmsg += ('【%s】为必填项。\n\n' % field_name[i])
            if errmsg == "":
                break
            field_values = easygui.multenterbox(errmsg, title, field_name, field_values)

        print("用户资料如下：%s" % str(field_values))

    # 读取文件里的内容
    def opentext(self):
        file = easygui.fileopenbox(msg="请选择你想要打开的文本文件：",default="*.txt") # default 设置默认显示的文件类型
        title = os.path.basename(file)  # 将目录的路径去掉，只保留文件名，如果需要的话
        # msg = "文件{}的内容如下：".format(file)
        msg = "文件{}的内容如下：".format(title)
        # title = "显示文件内容"
        with open(file) as f:
            text = f.read() # 直接使用read()即可获取文本内容
            easygui.textbox(msg, title, text=text)

    # 当用户点击“OK”按钮的时候，比较当前文件是否修改过，如果修改过，则提示“覆盖保存”、”放弃保存”或“另存为…”并实现相应的功能
    def opentextandcheck(self):
        file = easygui.fileopenbox(msg="请选择你想要打开的文本文件：", default="*.txt")
        title = os.path.basename(file)
        msg = "文件{}的内容如下：".format(title)

        with open(file) as f:
            text = f.read()
            text_after = easygui.textbox(msg, title, text=text)
        if text_after == text:
            sys.exit(0)
        else:
            choices = ["覆盖保存", "放弃保存", "另存为"]
            choice = easygui.buttonbox(msg="文件有修改过，请问是否执行下面的操作：", choices=choices)
            if choice == "覆盖保存":
                with open(file, 'w') as f:
                    f.write(text_after)
                    easygui.msgbox("文件已经覆盖并保存了。")
            elif choice == "放弃保存":
                sys.exit(0)
            elif choice == "另存为":
                filename = easygui.enterbox("请输入想要创建的文件名：", title="创建文件")
                filename = filename + ".txt"
                while True:
                    if os.path.exists(filename):
                        easygui.msgbox("文件名已经存在，请重新输入", ok_button="确定")
                        filename = easygui.enterbox("请输入想要创建的文件名：", title="创建文件")
                        filename = filename + ".txt"
                    else:
                        with open(filename, 'w') as f:
                            f.write(text_after)
                            break


if __name__ == "__main__":
    game = InterFaceGame()
    game.opentext()
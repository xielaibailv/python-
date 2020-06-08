import easygui
import sys
import random
import os


class InterFaceGame:
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

    def login2(self):
        msg = "请填写以下联系方式"
        title = "账号中心"
        fieldNames = [" *用户名", " *真实姓名", "  固定电话", " *手机号码", "  QQ", " *E-mail"]
        fieldValues = []
        fieldValues = easygui.multenterbox(msg, title, fieldNames)

        while 1:
            if fieldValues == None:
                break
            errmsg = ""
            for i in range(len(fieldNames)):
                option = fieldNames[i].strip()
                if fieldValues[i].strip() == "" and option[0] == "*":
                    errmsg += ('【%s】为必填项。\n\n' % fieldNames[i])
            if errmsg == "":
                break
            fieldValues = easygui.multenterbox(errmsg, title, fieldNames, fieldValues)

        print("用户资料如下：%s" % str(fieldValues))

    # 读取文件里的内容
    def opentext(self):
        file = easygui.fileopenbox(msg="请选择你想要打开的文本文件：")
        msg = "文件{}的内容如下：".format(file)
        title = "显示文件内容"
        text = []
        os.chdir(os.curdir)
        with open(file) as f:
            for each_line in f:
                text.append(each_line)

        easygui.textbox(msg, title, text=text)

    # 当用户点击“OK”按钮的时候，比较当前文件是否修改过，如果修改过，则提示“覆盖保存”、”放弃保存”或“另存为…”并实现相应的功能
    def opentextandcheck(self):
        file = easygui.fileopenbox(msg="请选择你想要打开的文本文件：")
        msg = "文件{}的内容如下：".format(file)
        title = "显示文件内容"
        text = []
        os.chdir(os.curdir)
        with open(file) as f:
            for each_line in f:
                text.append(each_line)

        easygui.textbox(msg, title, text=text)
        if easygui.ccbox():
            ''''# 比较文件有无修改
            if 修改:
                choices = ["覆盖保存", "放弃保存", "另存为"]
                choice = easygui.buttonbox(msg="文件有修改过，请问是否执行下面的操作：", choices=choices)
                if choice == "覆盖保存":
                    pass
                elif choice == "放弃保存":
                    sys.exit(0)
                elif choice == "另存为":
                    pass
            else:
                sys.exit(0)
'''









if __name__ == "__main__":
    game = InterFaceGame()
    # game.guessnum2()
    # game.login1()
    game.opentext()

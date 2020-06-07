# -*- coding:utf-8 _*-
#!/usr/bin/python3

#   author : YOYO
#   time :  2020/6/7 19:10
#   email : youyou.xu@enesource.com
#   project_name :  python-study 
#   file_name :  拥有图形界面的程序.py
#   function： 把之前的程序，加上easygui，使之可以通过界面互动

# No1:猜数字
import easygui as g
import random


class GuessNum:
    def guessnum(self):
        # secret = random.randint(1,9)
        secret = 7
        times = 2

        msg = "来猜猜小公主我现在心里想的是1-9里哪一个数字："
        title = "数字小游戏"
        num = g.integerbox(msg=msg, title=title, lowerbound=1, upperbound=9)

        if num == secret:
            g.msgbox("你是小公主我肚子里的蛔虫吗？？！！", title="猜测结果", ok_button="退出游戏", image="歪头.gif")
        else:
            while times:
                times -= 1
                if times >= 0:
                    if num == secret:
                        g.msgbox("终于猜对了呀，哼，真是的，居然不是一次就中，你根本不爱我！", title="猜测结果", ok_button="退出游戏")
                        break
                    elif num < secret:
                        g.msgbox("小了小了,你还有 %d 次机会" % (times+ 1), title="猜测结果")
                    elif num > secret:
                        g.msgbox("大了大了,你还有 %d 次机会" % (times+ 1), title="猜测结果")
                    num = g.integerbox(msg=msg, title=title, lowerbound=1, upperbound=9)
            else:
                g.msgbox("次数用光了哦", ok_button="退出游戏")














if __name__ == "__main__":
    game = GuessNum()
    game.guessnum()
'''
# 第一个小游戏？？？
print('.................YOYO工作室.........................')
temp = input("来猜猜小公主我现在心里想的是哪一个数字：")
guess = int(temp)
if guess == 2:
	print("我擦，你是小公主我肚子里的蛔虫吗？？！！")
	print("哼，猜中了也没有奖励！")
else:
	print("猜错了，我现在心里想的是2！")
print("游戏结束！")


# 一个=是赋值，两个==是表示等于
# int(temp) 将字符串变量转化为整型
# 内置函数：BIF==Built-in function，想知道有多少bif，在idle里输入#  dir(__builtins__)
# 使用help（BIF）可以查看该BIF的使用方法
'''

'''
# 第一个小游戏的改进版1.1

import random      #导入随机数模块

secret= random.randint(0,9)  # 给答案赋值，在1-10里随机生成一个数字
print('.................YOYO工作室.........................')
temp = input("来猜猜小公主我现在心里想的是哪一个数字：")
guess = int(temp)
if guess == secret:
            print("我擦，你是小公主我肚子里的蛔虫吗？？！！")
            print("哼，猜中了也没有奖励！")
while guess !=secret:
    temp=input("哎呀，猜错了啦，再给你一次机会：")
    guess=int(temp)
    if guess == secret:
            print("终于猜对了呀，哼，真是的，居然不是一次就中，你根本不爱我！")
            print("哼，猜中了也没有奖励！")
    else:
            if guess > secret:
                    print("大了大了~~~")
            else:
                    print("小了小了！！")
print("游戏结束！")

# 如果要求答案是随机的，需要引入random模块。
# random模块里有一个函数：randint（） 可以返回一个随机整数。
# 引入模块要在代码前面导入  import random

'''

#第三版，为用户提供三次机会尝试，机会用完或者用户猜中答案均退出循环

import random

times = 3
secret= random.randint(0,9)
temp = input("来猜猜小公主我现在心里想的是哪一个数字：")
guess = int(temp)
if guess == secret:
            print("我擦，你是小公主我肚子里的蛔虫吗？？！！")
            print("哼，猜中了也没有奖励！")
while guess !=secret:
    times -= 1
    if times > 0:
        temp=input("哎呀，猜错了啦，再给你一次机会：")
        guess=int(temp)
        if guess == secret:
                print("终于猜对了呀，哼，真是的，居然不是一次就中，你根本不爱我！")
                print("哼，猜中了也没有奖励！")
        else:
                if guess > secret:
                        print("大了大了~~~")
                else:
                        print("小了小了！！")
    else:
        print("机会没有了。")
        break

print("游戏结束！")


#附上小甲鱼写的，比上面的代码稍显简洁
# import random
# times = 3
# secret = random.randint(1,10)
# # 这里先给guess赋值（赋一个绝对不等于secret的值）
# guess = 0
# # print()默认是打印完字符串会自动添加一个换行符，end=" "参数告诉print()用空格代替换行
# print("不妨猜一下小甲鱼现在心里想的是哪个数字：", end=" ")
# while (guess != secret) and (times > 0):
#     temp = input()
#     guess = int(temp)
#     times = times - 1 # 用户每输入一次，可用机会就-1
#     if guess == secret:
#         print("我草，你是小甲鱼心里的蛔虫吗？！")
#         print("哼，猜中了也没有奖励！")
#     else:
#         if guess > secret:
#             print("哥，大了大了~~~")
#         else:
#             print("嘿，小了，小了~~~")
#         if times > 0:
#             print("再试一次吧：", end=" ")
#         else:
#             print("机会用光咯T_T")
# print("游戏结束，不玩啦^_^")


#第四版，当用户输入错误类型的时候，及时提醒用户重新输入，防止程序崩溃
import random


temp = input("来猜猜小公主我现在心里想的是哪一个数字：")
#temp.isdigit()      所有字符都是数字，为真返回 True，否则返回 False
#前加一个  not ，表示 not true = false
while not temp.isdigit():
    print("输入不合法，请重新输入!")
    temp = input('请输入整数：')
    guess = int(temp)
    pass
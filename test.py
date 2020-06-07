import random
def guess1():
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

guess1()
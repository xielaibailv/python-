# 游戏编程：按以下要求定义一个乌龟类和鱼类并尝试编写游戏。
#
# 假设游戏场景为范围（x, y）为0<=x<=10，0<=y<=10
# 游戏生成1只乌龟和10条鱼
# 它们的移动方向均随机
# 乌龟的最大移动能力是2（Ta可以随机选择1还是2移动），鱼儿的最大移动能力是1
# 当移动到场景边缘，自动向反方向移动
# 乌龟初始化体力为100（上限）
# 乌龟每移动一次，体力消耗1
# 当乌龟和鱼坐标重叠，乌龟吃掉鱼，乌龟体力增加20
# 鱼暂不计算体力
# 当乌龟体力值为0（挂掉）或者鱼儿的数量为0游戏结束

import random

class Fish:
    def __init__(self):# 初始化位置
        self.fish_x = random.randint(0, 10)
        self.fish_y = random.randint(0, 10)

    def move(self):
        per = random.randint(0, 1)
        while per:
            self.fish_x += 1
        else:
            self.fish_y += 1
        if self.fish_x > 10 or self.fish_x < 0:
            self.fish_x = abs(self.fish_x - 1)
        elif self.fish_y > 10 or self.fish_y < 0:
            self.fish_y = abs(self.fish_y - 1)




class Tuple:
    def __init__(self):
        self.tuple_x = random.randint(0, 10)
        self.tuple_y = random.randint(0, 10)
        self.blood = 100

    def move(self):
        temp = random.randint(0, 1)
        per = random.randint(1,2)
        while temp:
            self.tuple_x += per
        else:
            self.tuple_y += per
        self.blood -= 1
        if self.tuple_x > 10 or self.tuple_x < 0:
            self.tuple_x = abs(self.tuple_x - 1)
        elif self.tuple_y > 10 or self.tuple_y < 0:
            self.tuple_y = abs(self.tuple_y - 1)

    def eat(self):
        tuple.blood += 20
        if tuple.blood > 100:
            tuple.blood = 100



class Game():
    print('游戏开始')
    tuple = Tuple()
    tuple.move()
    for each in range(10):
        fish = Fish()
        fish.move()
        if tuple.tuple_x == fish.fish_x and tuple.tuple_y == fish.fish_y:
            each += 1

            if tuple.blood == 0:
                break
    print('游戏结束')





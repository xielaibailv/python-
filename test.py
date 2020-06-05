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
x = [0,10]
y = [0,10]


class Fish:
    def __init__(self):  # 初始化位置
        self.fish_x = random.randint(x[0], x[1])
        self.fish_y = random.randint(y[0], y[1])

    def move(self):
        per = random.randint(-1, 1)  # x和y各自有三种移动，向下，向上，不动，但实在是搞不定只能一个坐标轴随机移动，只好不考虑0，x，y都移动
        # 新的位置 要重新 设置变量，不能搞到初始变量里
        new_fish_x = self.fish_x + per
        new_fish_y = self.fish_y + per

        # 超出范围自动往相反方向走
        # if new_fish_x > x[1] or new_fish_x < x[0]:
        #     new_fish_x = abs(new_fish_x - 1)
        # elif new_fish_y > y[1] or new_fish_y < y[0]:
        #     new_fish_y = abs(new_fish_y - 1)
        # return new_fish_x, new_fish_y
        if new_fish_x > x[1]:
            new_fish_x = new_fish_x - (new_fish_x - x[1])
        elif new_fish_x < x[0]:
class Tortoise:
    def __init__(self):
        self.tortoise_x = random.randint(x[0], x[1])
        self.tortoise_y = random.randint(y[0], y[1])
        self.blood = 100

    def move(self):
        direction = [-2, -1, 1, 2]  # 有的可能4种移动步长
        per = random.choice(direction)  # 随机选择一个数
        new_tortoise_x = self.tortoise_x + per
        new_tortoise_y = self.tortoise_y + per
        self.blood -= 1

        # 超出范围自动往相反方向走
        if new_tortoise_x > x[1] or new_tortoise_x < x[0]:
            new_tortoise_x = abs(new_tortoise_x - 1)
        elif new_tortoise_y > y[1] or new_tortoise_y < y[0]:
            new_tortoise_y = abs(new_tortoise_y - 1)
        return new_tortoise_x, new_tortoise_y

    def eat(self):
        self.blood += 20
        if self.blood > 100:
            self.blood = 100


class Game():
    print('游戏开始')
    tortoise = Tortoise()  # 实例化乌龟

    # 因为鱼要有10条，所以必须要创建一个列表来保存10条鱼
    fish = []
    for i in range(10):
        each_fish = Fish()
        fish.append(each_fish)

    while True:
        position = tortoise.move()  # 乌龟的位置
        if tortoise.blood == 0:
            print('乌龟体力用完了')
            break
        if len(fish) == 0:
            print('鱼被吃光了')
            break

        for each_fish in fish[:]:
            if each_fish.move() == position:  # 每条鱼的位置等于乌龟的位置
                print('鱼被吃掉了一条')
                fish.remove(each_fish)
                tortoise.eat()
                # print('鱼的位置', each_fish.move())
        print('乌龟的血量', tortoise.blood)
        # print('乌龟的位置', tortoise.move())

    print('游戏结束')


if __name__ == "__main__":
    game = Game()

    # tortoise = Tortoise()
    #
    # while tortoise.blood:
    #     position = tortoise.move()
    #     print(tortoise.blood)
    #
    # else:
    #         print('乌龟体力用完了')



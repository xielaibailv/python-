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

#choice ：从序列里随机获取一个元素
#randint:如果想从一个范围内随机生成一个数，还是用这个比较好

#鱼和乌龟的数量不能放到初始变量里，为什么还不知道，比较难定义吧


import random

sum_x = [0,10]     #x轴移动范围
sum_y = [0,10]     #y轴移动范围

class Tortoise:
    def __init__(self):
        #初始体力
        self.power = 100
        #初始位置也要放在这里，初始的东西
        #随机生成数的范围虽然可以直接写（0,10），但更好的是引用全局变量sum_x,sum_y
        #这样假如修改，只需要修改全局变量即可
        self.initial_x = random.randint(sum_x[0], sum_x[1])
        self.initial_y = random.randint(sum_y[0], sum_y[1])

    def move(self):
        # 利用 direction 设置移动的方向，1/2：向上（向右）；-1/-2：向下（向左）；
        #乌龟可以移动的步数，暂不考虑0
        #因为这里直接将所有步数列出来了，就不需要step这个变量了
        direction = [1,-1,2,-2]
        # 新的位置在上一个位置的基础上随机移动
        new_x = self.initial_x + random.choice(direction)
        new_y = self.initial_y + random.choice(direction)
        #检查移动后是否超出x轴边界
        if new_x > sum_x[1]:
            #这里不能是给new_x重新赋值，而应该是给初始值，此时的初始值就要开始变了
            self.initial_x = sum_x[1] - (new_x - sum_x[1])
        elif new_x < sum_x[0]:
            self.initial_x = sum_x[0] - (new_x - sum_x[0])
        else:
            self.initial_x = new_x
        # 检查移动后是否超出y轴边界
        if new_y > sum_y[1]:
            self.initial_y = sum_y[1] - (new_y - sum_y[1])
        elif new_y < sum_y[0]:
            self.initial_y = sum_y[0] - (new_y - sum_y[0])
        else:
            self.initial_y = new_y

        #体力消耗
        self.power -= 1
        #返回移动后的新位置
        return (self.initial_y,self.initial_y)

    #吃鱼时体力的变化也算乌龟的方法，所以也写到乌龟的类里
    #怎么才能吃鱼不用管，条件到main里面去写，但一旦满足这个条件，就可以调用eat()来实现体力值的增减
    def eat(self):
        self.power += 20
        #因为上限只能是100，所以超出100需要掉到100
        if self.power > 100:
            self.power = 100


class Fish:
    def __init__(self):
        #定义初始位置
        self.initial_x = random.randint(sum_x[0], sum_x[1])
        self.initial_y = random.randint(sum_y[0], sum_y[1])
    def move(self):
        direction = [1, -1]
        # 新的位置在上一个位置的基础上随机移动
        new_x = self.initial_x + random.choice(direction)
        new_y = self.initial_y + random.choice(direction)
        # 检查移动后是否超出x轴边界
        if new_x > sum_x[1]:
            # 这里不能是给new_x重新赋值，而应该是给初始值，此时的初始值就要开始变了
            self.initial_x = sum_x[1] - (new_x - sum_x[1])
        elif new_x < sum_x[0]:
            self.initial_x = sum_x[0] - (new_x - sum_x[0])
        else:
            self.initial_x = new_x
        # 检查移动后是否超出y轴边界
        if new_y > sum_y[1]:
            self.initial_y = sum_y[1] - (new_y - sum_y[1])
        elif new_y < sum_y[0]:
            self.initial_y = sum_y[0] - (new_y - sum_y[0])
        else:
            self.initial_y = new_y

        # 返回移动后的新位置
        return (self.initial_y, self.initial_y)


#游戏主体
def play():
    tortoise = Tortoise()
    #因为要生成10条鱼，所以鱼创建为一个列表比较合适？
    fish = []
    for i in range(10):
        #每遍历一次创建一条鱼
        new_fish = Fish()
        #将鱼存进列表
        fish.append(new_fish)

     #在循环的时候，鱼数量的变化和乌龟体力的变化这一过程，最好不要和判断游戏结束混在一起
    while True:
        # 鱼被乌龟吃掉，条件是他们的位置相同
        # 乌龟的位置
        # position = tortoise.move()
        # # 在迭代器中删除列表元素是非常危险的，经常会出现意想不到的问题，因为迭代器是直接引用列表的数据进行引用
        # # 这里我们把列表拷贝给迭代器，然后对原列表进行删除操作就不会有问题了^_^(其实不是很懂)
        # # 将列表拷贝
        # for each_fish in fish[:]:
        #     if each_fish.move() == position:
        #         # 位置相同，鱼被吃一只,调用eat()
        #         tortoise.eat()
        #         fish.remove(each_fish)
        #         print('有一条鱼儿被吃掉了...')

         #游戏结束判断
        print(tortoise.power)
        if not len(fish) :
            print('鱼被吃完了，游戏结束！')
            break
        if not tortoise.power :
            print('乌龟没有体力了，游戏结束！')
            break
        position = tortoise.move()
        # 在迭代器中删除列表元素是非常危险的，经常会出现意想不到的问题，因为迭代器是直接引用列表的数据进行引用
        # 这里我们把列表拷贝给迭代器，然后对原列表进行删除操作就不会有问题了^_^(其实不是很懂)
        # 将列表拷贝
        for each_fish in fish[:]:
            if each_fish.move() == position:
                # 位置相同，鱼被吃一只,调用eat()
                tortoise.eat()
                fish.remove(each_fish)
                print('有一条鱼儿被吃掉了...')

play()


#教程写法，不知道为什么，我的永远是鱼被吃完，教程却是乌龟没有力气，检查过代码没有问题，坐标的生成也都是随机的，奇怪
# import random as r
#
# legal_x = [0, 10]
# legal_y = [0, 10]
#
#
# class Turtle:
#     def __init__(self):
#         # 初始体力
#         self.power = 100
#         # 初始位置随机
#         self.x = r.randint(legal_x[0], legal_x[1])
#         self.y = r.randint(legal_y[0], legal_y[1])
#
#     def move(self):
#         # 随机计算方向并移动到新的位置（x, y）
#         new_x = self.x + r.choice([1, 2, -1, -2])
#         new_y = self.y + r.choice([1, 2, -1, -2])
#         # 检查移动后是否超出场景x轴边界
#         if new_x < legal_x[0]:
#             self.x = legal_x[0] - (new_x - legal_x[0])
#         elif new_x > legal_x[1]:
#             self.x = legal_x[1] - (new_x - legal_x[1])
#         else:
#             self.x = new_x
#         # 检查移动后是否超出场景y轴边界
#         if new_y < legal_y[0]:
#             self.y = legal_y[0] - (new_y - legal_y[0])
#         elif new_y > legal_y[1]:
#             self.y = legal_y[1] - (new_y - legal_y[1])
#         else:
#             self.y = new_y
#             # 体力消耗
#         self.power -= 1
#         # 返回移动后的新位置
#         return (self.x, self.y)
#
#     def eat(self):
#         self.power += 20
#         if self.power > 100:
#             self.power = 100
#
#
# class Fish:
#     def __init__(self):
#         self.x = r.randint(legal_x[0], legal_x[1])
#         self.y = r.randint(legal_y[0], legal_y[1])
#
#     def move(self):
#         # 随机计算方向并移动到新的位置（x, y）
#         new_x = self.x + r.choice([1, -1])
#         new_y = self.y + r.choice([1, -1])
#         # 检查移动后是否超出场景x轴边界
#         if new_x < legal_x[0]:
#             self.x = legal_x[0] - (new_x - legal_x[0])
#         elif new_x > legal_x[1]:
#             self.x = legal_x[1] - (new_x - legal_x[1])
#         else:
#             self.x = new_x
#         # 检查移动后是否超出场景y轴边界
#         if new_y < legal_y[0]:
#             self.y = legal_y[0] - (new_y - legal_y[0])
#         elif new_y > legal_y[1]:
#             self.y = legal_y[1] - (new_y - legal_y[1])
#         else:
#             self.y = new_y
#         # 返回移动后的新位置
#         return (self.x, self.y)
#
#
# turtle = Turtle()
# fish = []
# for i in range(10):
#     new_fish = Fish()
#     fish.append(new_fish)
#
# while True:
#     print(turtle.power)
#     if not len(fish):
#         print("鱼儿都吃完了，游戏结束！")
#         break
#     if not turtle.power:
#         print("乌龟体力耗尽，挂掉了！")
#         break
#
#     pos = turtle.move()
#     # 在迭代器中删除列表元素是非常危险的，经常会出现意想不到的问题，因为迭代器是直接引用列表的数据进行引用
#     # 这里我们把列表拷贝给迭代器，然后对原列表进行删除操作就不会有问题了^_^
#     for each_fish in fish[:]:
#         if each_fish.move() == pos:
#             # 鱼儿被吃掉了
#             turtle.eat()
#             fish.remove(each_fish)
#             print("有一条鱼儿被吃掉了...")

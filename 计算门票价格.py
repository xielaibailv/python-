# 按照以下要求定义一个游乐园门票的类，并尝试计算2个成人+1个小孩平日票价。
#
# 平日票价100元
# 周末票价为平日的120%
# 儿童半票

class Ticket:
    def __init__(self,weekend = False,children = False):
        self.price = 100
        if weekend:
            self.price = 120
        if children:
            self.price = 50

    def calcPrice(self,num):
        return self.price * num

adult = Ticket()
child = Ticket(children = True)
print('2个成人+1个孩子的总平日票价：%d' %(adult.calcPrice(2) + child.calcPrice(1)))

# -----小甲鱼的代码-------------------------------------------------------
class Ticket:
    def __init__(self, weekend=False, child=False):
        self.exp = 100
        if weekend:
            self.inc = 1.2
        else:
            self.inc = 1
        if child:
            self.discount = 0.5
        else:
            self.discount = 1

    def calcPrice(self, num):
        return self.exp * self.inc * self.discount * num


# -----重写，2020.0603-------------------------------------------------------
# 自己写的太复杂了

class Ticket1:
    def __init__(self):
        self.ticket = 100

    def weekendprice(self):
        ticket = self.ticket * 1.2
        return ticket

    def childprice(self):  # 这个价格定义没必要搞成函数，增加复杂度，不同的成员可以通过多次传参来搞定
        ticket = self.ticket * 0.5
        return ticket

    def weekprice(self):
        ticket = self.ticket
        return ticket

    def countprice(self):
        msg= input('请分别输入成人数量，小孩数量，是否是工作日（y/n，用逗号隔开）:')
        (adult, children, weektime) = msg.split(",")
        adult = int(adult)
        children = int(children)
        childrenprice = (self.childprice()) * children
        if weektime == 'y' or weektime == 'Y':
            adultprice = (self.weekprice()) * adult
        else:
            adultprice = (self.weekendprice()) * adult
        price = adultprice + childrenprice
        print('总票价为：% 0.2f' % price)


if __name__ == "__main__":
    t = Ticket1()
    t.countprice()
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

#感觉自己有时候会将问题 想的过于复杂，以至于无法解决
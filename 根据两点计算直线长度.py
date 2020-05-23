from math import sqrt   #  求平方
# 定义一个点（Point）类和直线（Line）类，使用 getLen 方法可以获得直线的长度
# 设点 A(X1,Y1)、点 B(X2,Y2)，则两点构成的直线长度 |AB| = √((x1-x2)2+(y1-y2)2)

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def getX(self):  # 获取点的x
        return self.x

    def getY(self): # 获取点的y
        return self.y


class Line:
    def __init__(self, p1, p2):
        self.x = p1.getX() - p2.getX()   # 计算x的长度
        self.y = p1.getY()- p2.getY()   # 计算y的长度
        self.len = sqrt(self.x*self.x + self.y*self.y)    # 计算线段长度

    def get_len(self):
        return self.len


if __name__ == '__main__':
    p1 = Point(0,0)
    p2 = Point(3,4)
    line = Line(p1,p2)
    print(line.get_len())
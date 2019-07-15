#写矩形
#1、默认有宽和高两个属性
#2、如果为一个叫square的属性赋值，则说明是一个正方形，值即边长，此时宽和高都等于边长

class Rectangle:
    def __init__(self,width=0,height=0):
        self.height = height
        self.width = width

    #给矩形边长赋值
    def __setattr__(self,name,value):
        if name == 'square':
            self.width = value
            self.height = value
        else:
            # 下面这句会造成死循环(原因见笔记)
            #self.name = value
            #1、需要使用下面的方法，调用基类的方法
            #super().__setattr__(name,value)
            #2、除了上面方法，还可以用__dict__    字典属性
            self.__dict__[name] = value


    #求矩形面积

    def getArea(self):
        return self.height * self.width



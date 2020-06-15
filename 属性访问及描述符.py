# 写矩形
# 1、默认有宽和高两个属性
# 2、如果为一个叫square的属性赋值，则说明是一个正方形，值即边长，此时宽和高都等于边长
import time
import os
import pickle


class Rectangle:
    def __init__(self,width=0, height=0):
        self.height = height
        self.width = width

    # 给矩形边长赋值
    def __setattr__(self,name,value):
        if name == 'square':
            self.width = value
            self.height = value
        else:
            # 下面这句会造成死循环(原因见笔记),这样会形成无限递归，赋值会造成setsttr()调用，然后一直调用
            # self.name = value
            # 1、需要使用下面的方法，调用基类的方法
            # super().__setattr__(name,value)
            # 2、除了上面方法，还可以用__dict__    字典属性
            self.__dict__[name] = value

    # 求矩形面积
    def get_area(self):
        return self.height * self.width


# 记录指定变量的读取和写入操作，并将记录以及触发时间保存到文件（record.txt）
class Record:
    def __init__(self, initval=None, name=None):
        self.initval = initval   # 变量名
        self.name = name    # 变量值
        self.filename = "rizhi.txt"

    def __get__(self, instance, owner):
        with open(self.filename, 'a', encoding='utf-8') as f:
            f.write("%s 变量于北京时间 %s 被读取，%s = %s\n" % (self.name, time.ctime(), self.name, str(self.initval)))
        return self.initval

    def __set__(self, instance, value):
        with open(self.filename, 'a', encoding='utf-8') as f:
            f.write("%s 变量于北京时间 %s 被修改，%s = %s\n" % (self.name, time.ctime(), self.name, str(self.initval)))
        self.initval = value


# 编写描述符 MyDes，使用文件来存储属性，属性的值会直接存储到对应的pickle（腌菜，还记得吗？）的文件中。如果属性被删除了，文件也会同时被删除，属性的名字也会被注销
class MyDes:
    saved = []

    def __init__(self, name = None):
        self.name = name
        self.filename = self.name + '.pkl'

    def __get__(self, instance, owner):
        if self.name not in MyDes.saved:
            raise AttributeError("%s 属性还没有赋值！" % self.name)

        with open(self.filename, 'rb') as f:
            value = pickle.load(f)

        return value

    def __set__(self, instance, value):
        with open(self.filename, 'wb') as f:
            pickle.dump(value, f)
            MyDes.saved.append(self.name)

    def __delete__(self, instance):
        os.remove(self.filename)
        MyDes.saved.remove(self.name)
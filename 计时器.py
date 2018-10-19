# 计时器

import time as t 

class MyTime():
    def __init__(self):
        self.unit = ['年','月','日','小时','分钟','秒']
        self.tip = "还未开始计时！"


    #__str__ and __repr__这两个方法都是用于显示的，__str__是面向用户的，而__repr__面向程序员。
    # 一定要写这个，不然返回的看不懂
    # 他们可改变一个实例的字符串表示
    def __str__(self):
        return self.tip
    __repr__ = __str__

    # 开始计时
    def start(self):
        # localtime是time的一个方法，可根据 索引来调用不同的时间范围，返回一个元组结构
        self.begin = t.localtime()
        print("现在开始计时...")

    #结束计时
    def stop(self):
        self.end = t.localtime()
        #要在结束里调用下面的计算方法，不然时间差算不出来
        self._in()
        print("结束计时！")


    #内部方法，计算开始结束时间差
    def _in(self):
        #将计算结果放到一个数组里
        self.lasted = []
        self.tip = "总共运行了"
        #让开始时间和结束时间按照对应的时间级别各自相减？要使用for循环，range后要跟上到什么单位为止（这个跟time的函数有关）
        for index in range(6):
            #不能使用下面的写法，为啥暂时不知道
            #self.lasted = self.end[index] - self.begin[index]
            self.lasted.append(self.end[index]-self.begin[index])
            #要将(self.lasted[index])变成字符串才能相加
            self.tip += (str(self.lasted[index]) + self.unit[index])

        return self.tip





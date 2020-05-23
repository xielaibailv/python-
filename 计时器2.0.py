import time as t


class MyTime():
    def __init__(self):
        # 定义计时的单位
        self.unit = ['年', '月', '日', '小时', '分钟', '秒']
        # 要先定义初始值，保证在还没有开始调用方法时实例对象有值不报错
        self.prompt = "未开始计时！"
        self.lasted = []
        self.begin = 0
        self.end = 0

    # __str__   and  __repr__这两个方法都是用于显示的，__str__是面向用户的，而__repr__面向程序员。
    # 这个的作用是  可以将方法的返回值打印出来
    # 他们可改变一个实例的字符串表示
    def __str__(self):
        return self.prompt

    __repr__ = __str__

    # 重写add方法，让程序能执行t1+t2进行时间加和
    def __add__(self, other):
        prompt = "总共运行了"
        result = []
        for index in range(6):
            result.append(self.lasted[index] + other.lasted[index])
            if result[index]:
                prompt += (str(result[index]) + self.unit[index])
        return prompt

    # 开始计时
    def start(self):
        # localtime是time的一个方法，可根据 索引来调用不同的时间范围，返回一个元组结构
        self.begin = t.localtime()
        self.prompt = "请先调用stop()停止计时！"
        print("计时开始......")

    # 停止计时
    def stop(self):
        if not self.begin:
            print("请先调用start()进行计时！")
        else:
            self.end = t.localtime()
            # 引用计算的方法
            self._calc()
            print("计时结束！")

    # 内部方法，计算运行时间
    # 内部方法可以用_开始
    def _calc(self):
        self.lasted = []
        self.prompt = "总共运行了"
        for index in range(6):
            self.lasted.append(self.end[index] - self.begin[index])
            # 假如self.lasted等于0就不执行下面的语句
            if self.lasted[index]:
                # 要将(self.lasted[index])变成字符串
                self.prompt += (str(self.lasted[index]) + self.unit[index])

        # 为下一轮计时初始化变量
        self.begin = 0
        self.end = 0

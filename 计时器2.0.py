import time 
'''
python 有自己的关于统计时间的模块，不需要自己写。timeit()
'''


class MyTime:
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
        self.begin = time.localtime()
        self.prompt = "请先调用stop()停止计时！"
        print("计时开始......")

    # 停止计时
    def stop(self):
        if not self.begin:
            print("请先调用start()进行计时！")
        else:
            self.end = time.localtime()
            # 引用计算的方法
            self._calc()
            print("计时结束！")

    # 内部方法，计算运行时间
    # 内部方法可以用_开始
    def _calc(self):
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


# ---------------重写，20200612并优化，使用了__repr__ ---------------------
# 当使用print打印一个实例化对象时，打印的其实时一个对象的地址
# 只要自己定义了__str__(self)方法，那么就会打印从在这个方法中return的数据
# __str__   and  __repr__这两个方法意义差不多，但__str__是面向用户的，而__repr__面向程序员
# 意思就是，用print obj，会打印出__str__返回的数据，但直接用obj，会打印出__repr__返回的数据
# 简单举例
'''
    class obj:
    def __init__(self):
        self.a = "我是类的一个属性"
    def __str__(self):
        return self.a
    def __repr__(self):
        return self.a

#  只使用__str__
>>>  a   #  直接敲a，会返回对象的地址
   <__main__.obj object at 0x000001F7C97914A8>

>>> print(a)  # 使用print，会调用__str__
 我是类的一个属性

#  只使用 __repr__
>>>  a
  我是类的一个属性
'''


class CountTime:
    def __init__(self):
        self.begin = 0
        self.end = 0
        self.lasted = []
        self.unit = ['年', '月', '日', '小时', '分钟', '秒']
        self.tip = "未开始计时！"  # 不同状态需要返回不同的tip，很适合用__repr__

    def __repr__(self):
        return self.tip

    def start(self):
        self.tip = "请先调用stop()停止计时！"
        self.begin = time.localtime()
        print("计时开始...")

    def stop(self):
        if not self.begin:
            print("请先调用start()进行计时！")
        else:
            self.end = time.localtime()
            print("计时结束...")
            self.tip = "总共运行了"
            self._count()

    def _count(self):
        for each in range(6):
            self.lasted.append(self.end[each] - self.begin[each])
            if self.lasted[each]:
                self.tip += str(self.lasted[each]) + self.unit[each]

        self.begin = 0
        self.end = 0


# 之前的代码里，时间相减没有进位，会出现负数
class OptimizedTime:
    def __init__(self):
        self.begin = 0
        self.end = 0
        self.lasted = []
        self.unit = ['年', '月', '日', '小时', '分钟', '秒']
        self.tip = "未开始计时！"
        self.borrow = [0, 12, 31, 24, 60, 60]
        self.addresult = []

    def __repr__(self):
        return self.tip

    def start(self):
        self.tip = "请先调用stop()停止计时！"
        self.begin = time.localtime()
        print("计时开始...")

    def stop(self):
        if not self.begin:
            print("请先调用start()进行计时！")
        else:
            self.end = time.localtime()
            print("计时结束...")
            self.tip = "总共运行了"
            self._count()

    def _count(self):
        for each in range(6):
            num = self.end[each] - self.begin[each]

            if num < 0:   # 这里的进位计算是小甲鱼代码，感觉有点复杂
                i = 1
                while self.lasted[each-i] < 1: # 高位 < 1
                    self.lasted[each-i] += self.borrow[each-1] - 1
                    self.lasted[each-1-1] -= 1  # 更高位-1
                    i += 1
                self.lasted.append(self.borrow[each] + num)
                self.lasted[each-i-1] -= 1
            else:
                self.lasted.append(num)

        for each in range(6):
            if self.lasted[each]:
                self.tip += str(self.lasted[each]) + self.unit[each]

        self.begin = 0
        self.end = 0

    def __add__(self, other):
        self.tip = "总共运行了"
        for each in range(6):
            self.addresult.append(self.lasted[each] + other.lasted[each])
            if self.addresult[each]:
                self.tip += str(self.addresult[each]) + self.unit[each]
        return self.tip


# ---------------再次优化，上面关于位数进位太复杂了，直接利用time模块的功能_ ---------------------
# 用 time 模块的 perf_counter() 和 process_time() 来计算(这两好像都行)
# perf_counter() 返回计时器的精准时间（系统的运行时间）；
# process_time() 返回当前进程执行 CPU 的时间总和

class OptimizedTimeAgin:
    def __init__(self):
        self.begin = 0
        self.end = 0
        self.lasted = 0.0
        self.tip = "未开始计时！"
        self.addresult = 0

    def __repr__(self):
        return self.tip

    def start(self):
        self.tip = "请先调用stop()停止计时！"
        self.begin = time.perf_counter()
        print("计时开始...")

    def stop(self):
        if not self.begin:
            print("请先调用start()进行计时！")
        else:
            self.end = time.perf_counter()
            self._count()
            print("计时结束...")

    def _count(self):
        self.lasted = self.end - self.begin   # 直接相减，因为单位都是s，所以不用转换
        self.tip = '总共运行了 %0.2f s' % self.lasted

        self.begin = 0
        self.end = 0

    def __add__(self, other):
        self.addresult = self.lasted + other.lasted
        self.tip = '总共运行了 %0.2f s' % self.addresult
        return self.tip


if __name__ == "__main__":
    t = OptimizedTimeAgin()
    t.start()
    time.sleep(67)
    t.stop()

    t1 = OptimizedTimeAgin()
    t1.start()
    time.sleep(21)
    t1.stop()



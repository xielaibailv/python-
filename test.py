

import datetime


class LeapYear:
    def __init__(self):
        self.year = datetime.date.today().year  # 获取当前的年份

    def __iter__(self):
        return self

    def __next__(self):
        # 循环处理，只要不是闰年，就一直往下减，知道是闰年，赋值给temp并返回，然后再向下减
        # 这样可以保证每次赋值给temp的都是闰年
        while not ((self.year % 4 == 0 and self.year % 100 != 0) or (self.year % 400 == 0)):
            self.year -= 1
        temp = self.year
        self.year -= 1
        return temp




if __name__ == "__main__":
    a = LeapYear()
    for i in a:
        if i >= 2000:
            print(i)
        else:
            break







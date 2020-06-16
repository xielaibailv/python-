#迭代器的魔法方法
# __iter__()
# __next__()
# 意思就是，要写迭代器，就要包含这两个方法


class Fibs1:
	def __init__(self):
		self.a = 0
		self.b = 1

	def __iter__(self):
		return self

	def __next__(self):
		self.a, self.b = self.b, self.a + self.b
		return self.a

# 使用如下方法调用
# fibs1 = Fibs1()
# for each in fibs1:
# 	print(each)


# 上面的没有添加限制，将会一直循环，下面在请求的时候添加一个限制
# for each in fibs1:
# 	if each < 20:
# 		print(each)
# 	else:
# 		break


# 在函数里添加一个参数，控制迭代的范围
class Fibs2:
	# 定义一个n，默认值为10
	def __init__(self,n = 10):
		self.a = 0
		self.b = 1
		self.n = n

	def __iter__(self):
		return self

	def __next__(self):
		self.a,self.b = self.b,self.a + self.b
		if self.a > self.n:
			raise StopIteration
		return self.a

# 在请求时传入n，即可随意修改迭代的次数
# fibs2 = Fibs2(100)
# for each in fibs2:
# 	print(each)


# 使用迭代器来另写reversed()方法
class MyDev:
    def __init__(self, seq):
        self.seq = seq
        self.index = len(self.seq)

    def __iter__(self):
        return self

    def __next__(self):
        if  self.index == 0:
            raise StopIteration

        self.index = self.index - 1
        return self.seq[self.index]


# 写一个迭代器，计算至今为止的闰年
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




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


#------------------------------------------------------------------------------------------------
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


# 使用生成器来写reversed()方法，非常简单
def dev(seq):
    # (start, stop,step):含，不含，步长
    for i in range(len(seq)-1, -1, -1):  # yield会自动创建__iter__ and __next__方法，所以，只需要在seq里循环，从后往前取值即可
        yield seq[i]
# 调用时直接for循环将结果打印出来


#------------------------------------------------------------------------------------------------------------------------
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


# --------------------------------------------------------------------------------------------------------------
# 计算某个范围内的素数和
# 设计思路：不能吧所有的素数都挑出来然后再加和，这会极大占用内存
# 利用生成器generators，判断一个数是否为素数，是则加和，不是则继续
# fun1:判断一个数是否为素数；fun2：对fun1返回True的进行yield；fun3：将fun2返回的数据进行循环加和
# fun1 and fun2 为什么不能合并在一起，没有明白，也没有写成功
# 下面的代码计算小的素数和没有问题，太大就不行
import math


class SumPrimes:
    def is_prime(self, num):
        if num > 1:
            if num == 2 or num == 3:
                return True
            if num % 2 == 0:
                return False
            for index in range(3, int(math.sqrt(num) + 1), 2):  # 求素数的惯用数学公式
            # for index in range(3, num):   # 这上下2句有性能问题，太慢了
                if num % index == 0:
                    return False
            return True
        return False

    def get_primes(self, num=1):
        while True:
            if self.is_prime(num):
                yield num
            num += 1

    def count_primes(self, n=1000):
        sum_primes = 0
        for new in self.get_primes():
            if new < n:
                # print(new, end=' ')
                sum_primes += new
            else:
                print(sum_primes)
                return


# ----------------------小甲鱼代码---------------------------------------------------------------------

import math

def is_prime(number):
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for current in range(3, int(math.sqrt(number) + 1), 2):
            if number % current == 0:
                return False
        return True
    return False

def get_primes(number):
    while True:
        if is_prime(number):
            yield number
        number += 1

def solve():
    total = 2
    for next_prime in get_primes(3):
        if next_prime < 2000000:
            total += next_prime
        else:
            print(total)
            return


if __name__ == "__main__":
    # a = LeapYear()
    # for i in a:
    #     if i >= 2000:
    #         print(i)
    #     else:
    #         break
    a = SumPrimes()
    a.count_primes()




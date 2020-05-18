#迭代器的魔法方法
# __iter__()
# __next__()


class Fibs1:
	def __init__(self):
		self.a = 0
		self.b = 1
	def __iter__(self):
		return self
	def __next__(self):
		self.a,self.b = self.b,self.a + self.b
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

 #在函数里添加一个参数，控制迭代的范围
class Fibs2:
	#定义一个n，默认值为10
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
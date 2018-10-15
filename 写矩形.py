#写矩形
#1、默认有宽和高两个属性
#2、如果为一个叫square的属性赋值，则说明是一个正方形，值即边长，此时宽和高都等于边长

class Rectangle:
	def __init__(self,width=0,height=0):
		self.height = height
		self.width = width

	def __setattr__(self,name,value):
		print("给边长赋值情况为：")
		super().__setattr__(square,value)



# 1.属性：姓名（默认姓名为“小甲鱼”）
# 方法：打印姓名

class Person:
	name = '习大大'

	def printname(self):
		print(self.name + '你好!')


# 2.属性：长和宽版权属于：bbs.fishc.com
# 方法：设置长和宽 -> setRect(self)，获得长和宽 -> getRect(self)，获得面积 -> getArea(self))

class Rectangle:
	(long,width) = (4,5)

	def setRect(self):
		print('输入矩形的长和宽...')
		self.long = float(input('长：'))
		self.width = float(input('宽：'))

	def getRect(self):
		print('这个矩形的长是：%0.2f, 宽是：%0.2f' %(self.long,self.width))

	def getArea(self):
		area = self.long * self.width
		print(area)


#测试函数没有起作用，以后来看看啥原因
def testCase():
	a = Person()
	a.printname()

	r = Rectangle()
	r.getRect()
	r.setRect()
	r.getRect()


if "__name__" == "__main__":
	testCase()



# -----------------重写 --2020.6.3----------------------------------------------------

class Rectangle2:
    def __init__(self):
        self.length = 5
        self.width = 4

    def setRect(self):  # 赋值的话，直接修改掉属性值
        print('请输入矩形的长和宽...')
        self.length = float(input('长：'))
        self.width = float(input('宽：'))

    def getRect(self):   # 不需要再去处理和获得值，直接调用属性值就可以
        # length = float(self.length)
        # width = float(self.width)
        print('这个矩形的长是：%0.2f，宽是：%0.2f' % (self.length, self.width))

    def getArea(self):
        area = self.length * self.width
        print(area)
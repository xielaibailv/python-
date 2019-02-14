
 #-*- coding: utf-8 -*-
# #!/usr/bin/env python

------------------------------------------------------------------------------------------------------------------------------
定制计时器
需要的资源：使用time模块的localtime方法获取时间
                                 time.localtime返回struct_time的时间格式
                                 表现类：__str__   and  __repr__
                                 当属性和方法名重名时，属性会覆盖方法，即会把这个名字当做一个属性,这个方法就无法被调用
>>>
import time as t

class MyTime():
	def __init__(self):
		#定义计时的单位
		self.unit = ['年','月','日','小时','分钟','秒']
		#要先定义初始值，保证在还没有开始调用方法时实例对象有值不报错
		self.prompt = "未开始计时！"
		self.lasted = []
		self.begin = 0
		self.end = 0
	#__str__   and  __repr__这两个方法都是用于显示的，__str__是面向用户的，而__repr__面向程序员。
	#他们可改变一个实例的字符串表示	
	def __str__(self):
		return self.prompt
	
	__repr__ = __str__
	#重写add方法，让程序能执行t1+t2进行时间加和
	def __add__(self,other):
		prompt = "总共运行了"
		result = []
		for index in range(6):
			result.append(self.lasted[index] + other.lasted[index])
			if result[index]:
				prompt += (str(result[index]) + self.unit[index])
		return prompt

	#开始计时
	def start(self):
		#localtime是time的一个方法，可根据 索引来调用不同的时间范围，返回一个元组结构
		self.begin = t.localtime()           
		self.prompt = "请先调用stop()停止计时！"  
		print("计时开始......")

	#停止计时
	def stop(self):
		if not self.begin:
			print("请先调用start()进行计时！")
		else:
			self.end = t.localtime()
			#引用计算的方法
			self._calc()
			print("计时结束！")

	#内部方法，计算运行时间
	#内部方法可以用_开始
	def  _calc(self):
		self.lasted = []
		self.prompt = "总共运行了"
		for index in range(6):
			self.lasted.append(self.end[index] - self.begin[index])
			#假如self.lasted等于0就不执行下面的语句
			if self.lasted[index]:
				#要将(self.lasted[index])变成字符串
				self.prompt += (str(self.lasted[index]) + self.unit[index])

		#为下一轮计时初始化变量
		self.begin = 0
		self.end = 0

			


>>> t1 = MyTime()		
>>> t1.start()
计时开始......
>>> t1.stop()
计时结束！！！
>>> t1
总共运行了6秒


>>> t1 = MyTime()
>>> t1
未开始计时！
>>> t1.stop()
请先调用start()进行计时！
>>> t1.start()
计时开始......
>>> t1.stop()
计时结束！！！
>>> t1
总共运行了7秒
>>> t2 = MyTime()
>>> t2.start()
计时开始......
>>> t2.stop()
计时结束！！！
>>> t2
总共运行了5秒
>>> t1 + t2
'总共运行了1分钟-47秒'

print("----------------------------------------------------over----------------------------------------------")

#属性访问
__getattr__(self,name)                  #定义当用户试图获取一个不存在 属性时的行为
__getattribute__(self,name)     #定义当该类的属性被访问时的行为
__setattr__(self,name,value)    #定义当一个属性被设置时的行为
__delattr__(self,name)                   #定义当一个属性被删除时的行为

class C:
	def __getattribute__(self,name):
		print("getattribute")
		#使用super()来找getattribute的父类
		return super().__getattribute__(name)

	def __getattr__(self,name):
		print("getattr")
	def __setattr__(self,name,value):
		print("setattr")
		super().__setattr__(name,value)
	def __delattr__(self,name):
		print("delattr")
		super().__delattr__(name)

>>> c = C()
>>> c.x                    #先调用getarribute发现x不存在，再调用getattr
getattribute
getattr
>>> c.x = 1             #赋值了，调用setattr
setattr
>>> del c.x
delattr

print("----------------------------------------------------over----------------------------------------------")
描述符 property的原理
描述符就是将某种特殊类型的类的实例指派给另一个类的属性。

特殊类：一定要实现以下三个方法中的一个

__get__(self,instance,owner)  #用于访问属性，返回属性的值
__set__(self,instance,value)     #将在属性分配操作中调用，不返回任何内容
__del__(self,instance)                    #控制删除操作，不返回任何内容

class MyDecriptor:
	def __get__(self,instance,owner):
		print("getting...",self,instance,owner)
	def __set__(self,instance,value):
		print("setting...",self,instance,value)
	def __delete__(self,instance):
		print("deleting...",self,instance)

class Test:
	x=MyDecriptor()

>>> test=Test()
>>> test.x
可以看出，第一个参数是类自身的实例，第二个是其拥有者类的实例，第三个是拥有者本身
getting... <__main__.MyDecriptor object at 0x00000261C5B13F60> <__main__.Test object at 0x00000261C5B36390> <class '__main__.Test'>
>>> test
<__main__.Test object at 0x00000261C5B36390>
>>> Test
<class '__main__.Test'>
>>> >>> test.x='ire-MAN'
setting... <__main__.MyDecriptor object at 0x00000261C5B13F60> <__main__.Test object at 0x00000261C5B36390> ire-MAN
----------------------------------------------------------------
通过下面的方法，可以利用x给_x赋值
class  MyProperty:
	def __init__(self,fget=None,fset=None,fdel=None):
		self.fget = fget
		self.fset = fset
		self.fdel = fdel
	def __get__(self,instance,owner):
		return self.fget(instance)
	def __set__(self,instance,value):
		self.fset(instance,value)
	def __delete__(self,instance):
		self.fdel(instance)


class C:
	def __init__(self):
		self._x = None
	def getX(self):
		return self._x
	def setX(self,value):
		self._x = value
	def delX(self):
		del self._x 

	x = MyProperty(getX,setX,delX)

>>> c=C()
>>> c.x='MAN'
>>> c.x
'MAN'
>>> c._x           #赋值成功
'MAN'
>>> del c.x       #c._x也将找不到值
print("----------------------------------------------------over----------------------------------------------")

协议：Protocols，类似接口，规定哪些方法必须要定义，不过在python中，协议更像是一种指南

容器类型的协议：如果希望定制的容器是不可变的话，只需要定义__len__()和__getitem__()方法
		   如果希望定制的容器是可变的话，除上面的方法外，还需定义__setitem__()和__delitem__()
__len__(self)                                      定义当被len()调用时的行为（返回容器中的个数）
__getitem__(self,key)                定义获取容器中指定元素的行为，相当于self[key]
__setitem__(self,key,value)  定义设置容器中指定元素的行为，相当于self[key]= value
__delitem__(self,key)                 定义删除容器中指定元素的行为，相当于 del self[key]


-----------------
编写一个不可改变的列表，记录列表中每个元素被访问的次数
class Countlist:
    #定义列表，因为不确定会传入多少个数，所以使用*args
    #*args 表示任何多个无名参数，类型是一个元组tuple
	def __init__(self,*args):
        #args中的 x(参数) 依次循环出来，赋给self.values列表
		self.values = [x for x in args]
        #count()是列表的一个内置函数，计算元素出现的次数
        #将该数值保存在一个字典中,下标：访问次数，默认是0
        #fromkeys：用于创建一个新字典
		self.count = {}.fromkeys(range(len(self.values)),0)
    def __len__(self):
         return len(self.values)

    def __getitem__(self, key):
        self.count[key] += 1
        return self.values[key]

 >>>  l1 = Countlist(1,2,3,4,5)
>>>l2 = Countlist(2,4,6,8,10,20)
>>>l1[3]
4
>>>l2[0]
2
>>>l1[0]+l2[0]
3
>>>l1.count
{0: 1, 1: 0, 2: 0, 3: 1, 4: 0}

print("----------------------------------------------------over----------------------------------------------")

迭代器

内置函数：BIF==Built-in

iter()  迭代器
next()
--------------
string = "monkey"
it = iter(string)

#调用next()可以返回迭代器里的值，如果没有值了，就会抛出stopIteration
>>> next(it)
'm'
>>> next(it)
'o'
>>> next(it)
'n'

---------->>>
links = {'花果山的和尚':'https://blog.csdn.net/amrenyu',\
	'我的邮箱':'amrenyu@163.com'}
for each in links:
	print("%s -> %s" %(each,links[each]))

打印效果：
花果山的和尚 -> https://blog.csdn.net/amrenyu
我的邮箱 -> amrenyu@163.com

while语句同样可以实现
string = "monkey"
it = iter(string)
while True:
	try:
		each = next(it)
	except StopIteration:
		break
	print(each)

打印效果：
k
e
y

---------------
迭代器的魔法方法
__iter__()
__next__()

class Fibs:
	def __init__(self):
		self.a = 0
		self.b = 1
	def __iter__(self):
		return self
	def __next__(self):
		self.a,self.b = self.b,self.a + self.b
		return self.a

fibs = Fibs()
for each in fibs:
	print(each)

打印效果：
1
1
2
3
5
8
13
.......

加一个限制
for each in fibs:
	if each < 20:
		print(each)
	else:
		break

修改迭代器，增加一个参数，控制迭代的范围
class Fibs:
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
fibs = Fibs(100)
for each in fibs:
	print(each)

打印效果：
1
1
2
3
5
8
13
21
34
55
89

print("----------------------------------------------------over----------------------------------------------")

生成器(generator)：一种一边循环一边计算的机制。
实际上是迭代器的一种实现。迭代器需要去定义一个类，而生成器只需要在普通函数里加上一个 yield即可。
程序执行到yield时会暂停并保存当前所有的运行信息，返回 yield 的值, 并在下一次执行 next() 方法时从当前位置继续运行。
def myGen():
	print("生成器执行")
	yield 1
	yield 2

执行效果：
>>> m=myGen()
>>> next(m)
生成器执行
1
>>> next(m)
2

--------
def lib():
	a = 0
	b = 1
	while True:
		a,b = b,a+b
		yield a
#调用lib()
for each in lib():
	if each > 100:
		break
	#end表示在一个迭代完成后显示的内容
	print(each,end='   ')

结果如下：
1   1   2   3   5   8   13   21   34   55   89   

>>>---------------------
列表推导式：在列表里加一个for语句
例如：100以内能被2整除不能被3整除的数
a = [i for i in range(100) if not(i % 2) and i % 3]
>>> a
[2, 4, 8, 10, 14, 16, 20, 22, 26, 28, 32, 34, 38, 40, 44, 46, 50, 52, 56, 58, 62, 64, 68, 70, 74, 76, 80, 82, 86, 88, 92, 94, 98]
--------------
字典推导式：要加冒号
例如：10以内能被2整除的数
b = {i:i % 2 ==0 for i in range(10)}
 >>>b
{0: True, 1: False, 2: True, 3: False, 4: True, 5: False, 6: True, 7: False, 8: True, 9: False}
----------
集合推导式：无序，重复的元素会被剔除
c = {i for i in [1,1,2,3,4,4,5,6,3,8,6,2]}
>>> c
{1, 2, 3, 4, 5, 6, 8}

-----------------
生成器推导式：用()括起来的就是生成器推导式

e = (i for i in range(10))
>>> next(e)
0
>>> for each in e:
	print(each)

	
1
2
3
4
5
6
7
8
9
生成器推导式如果作为函数的参数，不用加圆括号也可以
常规方法：
>>> sum((i for i in range(10) if i %2))
25
省略圆括号：
>>> sum(i for i in range(20) if i % 2)
100


print("----------------------------------------------------over----------------------------------------------")

模块 ：模块就是程序。例如一个后缀名为.py的文件就是一个模块。
 	容器 ->数据的封装
 	函数 ->语句的封装
 	类 ->方法和属性的封装
 	模块 ->程序 ，封装组织python的代码
 命名空间：模块都放在同一个文件夹下，在导入模块时可以直接  import 模块名 ;在调用模块里的类时，可能就需要制定该类的模块名
例如 hello.py模块里有一个函数hi(),在调用时：c = hello.hi()，如果觉得麻烦，那么在导入时就要明确导入的函数名。

导入模块：
	one    -> import 模块名
	two    -> from 模块名  import  函数名
	three  -> import 模块名 as  新名字

 print("----------------------------------------------------over----------------------------------------------")
测试模块：
if __name__ == "__main__":
	test()

测试模块：在代码的后面一般要写个test()，来验证前面的代码是否正确。但是在调用该模块时又不想让测试的方法被调用，
就可以加一句上述代码即可。

搜索路径：假如模块和模块不在一个文件夹下，那么需要了解搜索路径。
搜索路径是一组列表，假如需要导入的模块不在搜索路径里，那么就加进去。

import sys
sys.path.append("E:\\......模块所在文件夹")
sys.path     #就可以看到路径中有


包（package）：创建一个文件夹，存放相关模块，文件夹的名字即包的名字
		在文件夹里创建一个__init__.py的文件，可以是空文件

print("----------------------------------------------------over----------------------------------------------")
python有很多现成的模块，在需要用到的时候，可以去python文档里搜索
	打开idle，help  -->Docs-->索引里输入要查找的模块名
	或者在idle里 先导入模块，然后打印出其文档
	>>>import timeit
	>>>timeit.__doc__    #这个打印出来是没有格式的
	>>>print(timeit.__doc__)    #这个会有格式，方便查看
	>>dir(timeit)    #查看里面定义了哪些函数，变量，方法等
	>>>timeit.__all__   #显示这个模块可用于外界调用的所有东西（类/函数）（不是所有的模块都有__all__,
			     #如果使用  from timeit import * 导入，只有在__all__里出现的名字，才能被导入
			     
	  __file__        #指明了模块的源代码所在的位置


 print("----------------------------------------------------over----------------------------------------------")

 爬虫
 1、python如何访问互联网？  urllib  包 里的  urllib.request

 import urllib.request
 r = urllib.request.urlopen("https://123.sogou.com/")
 html = r.read()
 print(html)     #返回的是一个二进制的字符串,需要进行解码操作
 html = html.decode("utf-8")
 print(html)

---------------------
import urllib.request

#open url既可以是一个地址也可以是一个实例化对象
response = urllib.request.urlopen('http://placekitten.com/200/200')
#所以除了上面的办法，还可以用下面这种
# res = urllib.request.Request('http://placekitten.com/200/200')
# response = urllib.request.urlopen(res)

#读取到指定的内容,除了用read方法，还可以用  geturl(),   info(),  getcode() 方法
cat_img = response.read()

#使用geturl()
# response.geturl()
#使用info()
# response.info()
# print(response.info())
#使用getcode(),返回的是请求的状态码
# response.getcode()

#给图片命名，所有文件都是二进制，所以可以用写入的方式将图片’保存‘
#“wb”指：二进制格式
with open('cat2_200_200.jpg','wb') as f:
    f.write(cat_img)

-----------------------------------
	2、利用有道进行在线翻译


import urllib.request
import urllib.parse
import json

#复制网址
url= 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
#下面的信息都是form data里的，前面加上data[],所有内容用引号引起来
#data参数如果赋值，就是以post方式发起请求
data = {}
data['type'] = 'AUTO'
data['i'] = '我爱中国！'
data['doctype'] = 'json'
data['version'] = '2.1'
data['keyfrom'] =  'fanyi.web'
#这一参数“ue”在有道的信息里是没有的
data['ue'] = 'UTF-8'
data['typoResult'] = 'false'
#利用parse模块（这是一点单独模块，需要导入）将结果编码成utf-8，并赋值给data
#encode: 将Unicode编码成后面跟着的形式
#decode: 将所有编码形式解码成Unicode
#      decode                          encode
#str ---------> str(Unicode) ---------> str
data = urllib.parse.urlencode(data).encode('utf-8')

response = urllib.request.urlopen(url,data)
html = response.read().decode('utf-8')

print(html)

>>>----------------

上面的代码返回的是一串字典格式的字符串，不太直观；下面是改进的版本
# 将需要翻译的内容参数化
url= 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
content = input("请输入想要翻译的内容：")
data = {}
data['type'] = 'AUTO'
data['i'] = content
data['doctype'] = 'json'
data['version'] = '2.1'
data['keyfrom'] =  'fanyi.web'
data['ue'] = 'UTF-8'
data['typoResult'] = 'false'
data = urllib.parse.urlencode(data).encode('utf-8')

response = urllib.request.urlopen(url,data)
html = response.read().decode('utf-8')

#将结果以json格式付给target，然后只打印翻译结果tgt参数
target = json.loads(html)
print("翻译结果：%s" % (target['translateResult'][0][0]['tgt']))


>>>----------------
 在进行爬虫时，浏览器会检查是正常浏览器请求还是爬虫，所以需要隐藏。
 最简单的方法就是修改浏览器的headers参数。

 headers参数 必须是一个字典，一个办法，直接设置一个字典作为参数传给request；
 						另一种是request生成之后，调用add_header()把header加进去。

 url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
 content = input("请输入想要翻译的内容：")

 # 获取到header里的信息
 head = {}
 head[
	 'User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36'

 data = {}
 data['type'] = 'AUTO'
 data['i'] = content
 data['doctype'] = 'json'
 data['version'] = '2.1'
 data['keyfrom'] = 'fanyi.web'
 data['ue'] = 'UTF-8'
 data['typoResult'] = 'false'
 data = urllib.parse.urlencode(data).encode('utf-8')

 # 使用第一种办法：通过Request的headers参数修改，直接将header信息以字典形式传入
 # 将head信息传入request
 req = urllib.request.Request(url, data, head)

 '''
 #第二种办法：先生成req，再利用Request.add_header()增加header
 req = urllib.request.Request(url,data)
 req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36')
 '''
 response = urllib.request.urlopen(req)
 html = response.read().decode('utf-8')

 # 将结果以json格式付给target，然后只打印翻译结果tgt参数
 target = json.loads(html)
 print("翻译结果：%s" % (target['translateResult'][0][0]['tgt'])) head['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36'

 如何对一个网址抓取内容过于频繁，会导致被屏蔽。
 一个办法是降低访问频率，延迟提交时间；
 一个办法是代理。

延迟提交时间，需要time模块
 # 修改headers的user-agent信息
 while True:
	 content = input('请输入想要翻译的内容(退出程序请按"q!")：')
	 if content == 'q!':
		 break

	 url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
	 # 获取到header里的信息
	 head = {}
	 head[
		 'User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36'

	 data = {}
	 data['type'] = 'AUTO'
	 data['i'] = content
	 data['doctype'] = 'json'
	 data['version'] = '2.1'
	 data['keyfrom'] = 'fanyi.web'
	 data['ue'] = 'UTF-8'
	 data['typoResult'] = 'false'
	 data = urllib.parse.urlencode(data).encode('utf-8')

	 # 使用第一种办法：通过Request的headers参数修改，直接将header信息以字典形式传入
	 # 将head信息传入request
	 req = urllib.request.Request(url, data, head)

	 # #第二种办法：先生成req，再利用Request.add_header()增加header
	 # req = urllib.request.Request(url,data)
	 # req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36')
	 #
	 response = urllib.request.urlopen(req)
	 html = response.read().decode('utf-8')

	 # 将结果以json格式付给target，然后只打印翻译结果tgt参数
	 target = json.loads(html)
	 print("翻译结果：%s" % (target['translateResult'][0][0]['tgt']))

	 time.sleep(5)

	 使用代理：代理ip可直接搜索出可用的ip
	 步骤：
	 1.参数是一个字典{'类型':'代理ip：端口号'}
proxy_support = urllib.request.ProxyHandler({})

2. 定制、创建一个 opener，opener相当于一个私人订制
opener = urllib.request.build_opener(proxy_support)

3a. 安装 opener
urllib.request.install_opener(opener)
3b. 调用 opener
opener.open(url)





print("----------------------------------------------------over----------------------------------------------")

正则表达式：re

 import re

 语法：
 1、寻找某个字符串，如果没有符合条件的会返回none
 	re.search(r'想要寻找的字符串','源字符串：想要寻找的字符串在这里')
返回值为：
<re.Match object; span=(5, 13), match='想要寻找的字符串'>

如果要匹配比如ip的数字,()表示分组（下面这个不太对）
re.search(r'(([01]{0,1}\d\d|2[0-4]{0,1}\d|25[0-5]{0,1})\.){3}([01]{0,1}\d\d|2[0-4]{0,1}\d|25[0-5]{0,1})','192.168.2.45')

 #-*- coding: utf-8 -*-
# #!/usr/bin/env python
print "hello"    #  python2的语法，python3不支持

print ("hello")  #  python3的语法

print (5+3)

print(154563884552424*13245453121)

print ("hello\n" *5)     # 打印了5遍hello   "\n"表示换行

print('----------------------------------over--------------------------------------------')


# 第一个小游戏？？？
print('.................YOYO工作室.........................')
temp = input("来猜猜小公主我现在心里想的是哪一个数字：")
guess = int(temp)
if guess == 2:
	print("我擦，你是小公主我肚子里的蛔虫吗？？！！")
	print("哼，猜中了也没有奖励！")
else:
	print("猜错了，我现在心里想的是2！")
print("游戏结束！")


# 一个=是赋值，两个==是表示等于
# int(temp) 将字符串变量转化为整型
# 内置函数：BIF==Built-in function，想知道有多少bif，在idle里输入#  dir(__builtins__)
# 使用help（BIF）可以查看该BIF的使用方法
 
print('---------------------------------------------over---------------------------------')
print('...............第一个小程序.................')

name=input("请输入你的姓名：")
print("你好，"+ name)
print('---------------------------------------------over---------------------------------')

#如果在字符串里有出现‘，可以用转义字符 \ 。
#比如 Let' go!这句话，可以用print( 'Let\' go!' )来打印
#如果字符串里本身含有 \，要使其显示出来，不被作为转义字符处理，可以用\对自身进行转义
#比如：‘C:\\work'   第一个\是转义字符，转义了后面的\,保证后面的\能正常显示
#但假如一个字符串里有很多\，那么使用上面的方式是不合理的，直接在字符串前面加上 r
#比如：r表示原始字符串     r’C:\work\news\first'
print('---------------------------------------------over---------------------------------')

str="""一片两片三四片，
五片六片七八片，
九片十片千万片，
飞入花丛皆不见。"""
print(str)
# 用三个引号"""可以将输入的字符串的格式完整保留，类似HTML里的 pre
print('---------------------------------------------over---------------------------------')

# 第一个小游戏的改进版1.1

import random      #导入随机数模块
secret= random.randint(0,9)  # 给答案赋值，在1-10里随机生成一个数字
print('.................YOYO工作室.........................')
temp = input("来猜猜小公主我现在心里想的是哪一个数字：")
guess = int(temp)
if guess == secret:
            print("我擦，你是小公主我肚子里的蛔虫吗？？！！")
            print("哼，猜中了也没有奖励！")
while guess !=secret:
    temp=input("哎呀，猜错了啦，再给你一次机会：")
    guess=int(temp)
    if guess == secret:
            print("终于猜对了呀，哼，真是的，居然不是一次就中，你根本不爱我！")
            print("哼，猜中了也没有奖励！")
    else:
            if guess > secret:
                    print("大了大了~~~")
            else:	
                    print("小了小了！！")
print("游戏结束！")

# 如果要求答案是随机的，需要引入random模块。
# random模块里有一个函数：randint（） 可以返回一个随机整数。
# 引入模块要在代码前面导入  import random

print('---------------------------------------------over---------------------------------')

# int将浮点型转化为整型时，会采取直接截断的方式，比如5.99，转化为int是5
a=5.99
b=str(a)
print(b)  #b会显示  '5.99' 因为会将a作为一个字符串

#获取数据类型，可以用 type(值) ，isinstance() 

a= '客户'
isinstance(a,str)  　＃将会返回Ｔｒｕｅ
# #表示整数除以整数，获得的也是整数部分
# ** 表示幂运算。 3**2表示3的2次方。 -3**2=-9,3**-2=0.111111111
print('---------------------------------------------over---------------------------------')

# 打飞机小游戏编程思路：

加载背景音乐
播放背景音乐（单曲循环）
我方飞机诞生
juli = 0
while True：
	if 用户是否点击了关闭按钮：
		退出程序

	juli +=1
	if juli ==50：	#防止小飞机生成的太多，每50个距离产生一个小飞机
		juli=0      #重新开始计算
	小飞机诞生

小飞机移动一个位置    #这个不能放在上面的循环里面
屏幕刷新

	if 用户鼠标产生移动：
		我方飞机中心位置 = 用户鼠标位置
		屏幕刷新

	if 我方飞机与小飞机产生触碰：
		我方飞机死亡，播放死亡音乐
		修改我方飞机图案
		打印‘Game Over’
		停止背景音乐（淡出）
print('---------------------------------------------over---------------------------------')

#根据输入的分数自动给出ABCD不同等级：

score = int(input('请输入分数：'))
while score < 0 or score > 100:
	score=int(input('输入错误，请重新输入：'))
if 100 >= score >= 90:
	print('A')
elif 90 > score >= 80:
	print('B')
elif 80 > score >=60:
	print('C')
elif 60 > score >=0:
	print('D')
print('---------------------------------------------over---------------------------------')



# range(start,stop,step=1) range这个BIF的作用是生成一个从start（包含）开始到stop（不包含）结束的数字序列。start，step都是可选，只有stop必填。
'''
range(5)  --->range(0, 5)
list(range(5))  --->[0, 1, 2, 3, 4]   最后一个是不包含的
for i in range(1,10,2)  --->打印出来会是1,3,5,7,9

print('---------------------------------------------over---------------------------------')

shuzu = ['a','客户',123,[2,1,2]]     # 列表：里面可以包含多个类型的值
empty = []    #也可以创建一个空列表

python没有数据类型，所以可以说python没有数组，只有列表。

***给列表添加值的三种方法：append()   extend([])   insert()

1.如果要给列表增加一个值，可以用 append   ： shuzu.append('司机')
2.但是append()只能添加一个值，如果要添加多个，则需要用 extend ：shuzu.extend([])
需要注意的是：extend的作用是扩展列表，所以它的格式是用列表的形式扩展原列表。
3.以上两种方式都是在列表的末尾添加值，如果要在其他位置添加，需要 insert()
insert() 有2个参数，一个是在插入列表里的位置，一个是要插入的值
'''
效果如下：
>>> shuzu = ['a','客户',123,[2,1,2]]
>>> shuzu
['a', '客户', 123, [2, 1, 2]]
>>> shuzu.append('司机')             #给列表增加单个值
>>> shuzu
['a', '客户', 123, [2, 1, 2], '司机']

>>> shuzu.extend(['竹林','河水'])      #给列表增加多个值，用[]将增加的值括起来
>>> shuzu
['a', '客户', 123, [2, 1, 2], '司机', '竹林', '河水']
>>> shuzu.insert(0,'小可爱')              #第一个参数0表示在第一个位置插入
>>> shuzu
['小可爱', 'a', '客户', 123, [2, 1, 2], '司机', '竹林', '河水']

--------------------------------------------
# 数据交换
>>> temp = shuzu[0]                         #通过这种方式，将‘小可爱’暂时复制给 temp
>>> shuzu[0] = shuzu[1]                   #让第一位的值等于第二位
>>> shuzu
['a', 'a', '客户', 123, [2, 1, 2], '司机', '竹林', '河水']
>>> shuzu[1] = temp                         #再将第二位的值等于temp，达到了将两个值调换顺序的效果
>>> shuzu
['a', '小可爱', '客户', 123, [2, 1, 2], '司机', '竹林', '河水']
--------------------------------------------------
# 从列表删除元素
#三种方式： remove()   del     pop()
#  remove() 加上要删除的值，即可删除；如果在列表中没有该值，会报错
#  del  是一个语句，del +列表[下标]  即可删除；如果不加上下标，就表示删除整个列表
#  pop()   从列表中取出一个值并返回该值

>>> shuzu.remove('司机')                    
>>> shuzu
['a', '小可爱', '客户', 123, [2, 1, 2], '竹林', '河水']

>>> del shuzu[4]                                                                                              
>>> shuzu
['a', '小可爱', '客户', 123, '竹林', '河水']

>>> shuzu.pop()                                      #如果不加下标，就默认删除最后一个
'河水'
>>> shuzu
['a', '小可爱', '客户', 123, '竹林']
>>> name= shuzu.pop(3)                       #可以把删除的值赋给一个变量
>>> name
123
>>> shuzu
['a', '小可爱', '客户', '竹林']
------------------------------------------------------------------------
# 列表分片(slice)
# 如果需要一次性从列表里获取多个元素，就需要利用列表分片

>>> shuzu[0:3]                # 包含0，不包含3
['a', '小可爱', '客户']
>>> shuzu[:]               # 不写前后值，相当于拷贝原列表
['a', '小可爱', '客户', '竹林']

# list1=list2  和  list1=list2[:]   是不同的。前者相当于给list1多贴了一个标签；后者是实打实的拷贝了一个列表。假如修改list1，前者的list2也会同步修改，但后者list1和list2会是两个独立的不同的列表。
---------------------------------------------------------------------------
# 列表的常用操作符
# 列表之间的比较大小，是比较列表的长度大小
# 列表之间的相加，是将两个列表的内容拼接在一起
# 使用  in  可以查看某个元素是否在某个列表里

>>> list5
[123, 1111, 123, 1111, 123, 1111, 123, 1111, 123, 1111]
>>> 123 in list5
True
>>> 456 not in list5
True

#使用 in ，not in 只能查看一层，如果列表里含有列表，就查不出来
>>> list6 = [123,['玫瑰','芍药'],456]
>>> '玫瑰' in list6
False
#这个时候需要引入索引
>>> '玫瑰' in list6[1]
True
# 对于列表中的列表的值，可以用两个索引来访问
>>> list6[1][0]           # [1]表示一层列表里第1个元素；[0]表示这个元素列表里第0个元素
'玫瑰'
----------------------------------------------------------
# 列表的其他内置函数（调用时使用 . ）
#  count   计算参数在列表中出现的次数
>>> list6.count(123)
1

# index   可以返回参数在列表中的位置
>>> list6.index(456)
2
# 假如列表里有多个同样的参数，默认返回第一个位置
# index 还能指定在列表里一段范围里寻找
>>> list = list6*5
>>> list
[123, ['玫瑰', '芍药'], 456, 123, ['玫瑰', '芍药'], 456, 123, ['玫瑰', '芍药'], 456, 123, ['玫瑰', '芍药'], 456, 123, ['玫瑰', '芍药'], 456]
>>> list.index(456,3,8)      # 在列表的第3位到第8位之间寻找 456元素
5

# reverse   将列表翻转。
>>> list6.reverse()
>>> list6
[456, ['玫瑰', '芍药'], 123]

# sort       用指定的方式对列表进行排序（这个需要列表里是同类型的元素）
>>> num = [1,3,5,8,23,12,53,24]
>>> num.sort()                                   #  有一个参数，reverse=fault，默认从小到大
>>> num
[1, 3, 5, 8, 12, 23, 24, 53]

# 想要从大到小，可以先用sort() 排序,再用 reverse()翻转
#  sort() 有三个参数  sort(func,key,reverse)
#  sort(reverse=fault)   将值改成 True，即可从大到小排列
>>> num.sort(reverse=True)
>>> num
[53, 24, 23, 12, 8, 5, 3, 1]

print('---------------------------------------------over---------------------------------')

#  元组（tuple） ：受到限制的列表，元组通常用（）
#  如果一个元组只有一个元素，在其值后面要加一个  ,  这样才是元组。
'''
>>> a =()
>>> type(a)
<class 'tuple'>
>>> b = (1,)
>>> type(b)
<class 'tuple'>
>>> c=(1)              # 如果不加逗号，类型就是int
>>> type(c)
<class 'int'>
>>> e=1,                # 哪怕不要（），只要有逗号，也可以创建元组
>>> type(e)
<class 'tuple'>
'''
#  要在元组里插入一个元素，需要采用以下方法：
>>> temp = ('腊梅','百合','秋菊','玫瑰')
>>> temp = temp[:2] + ('枇杷',) + temp[2:]          # 插入的元素括号和逗号缺一不可
>>> temp
('腊梅', '百合', '枇杷', '秋菊', '玫瑰')

# 如果要删除某一个元素，也可以采用上述方法。
# 如果要删除整个元组，可以用  del temp

print('---------------------------------------------over---------------------------------')
#  字符串
>>> str1 = 'I love you , you are my dear'
>>> str1[:6]
'I love'
>>> str1[5]    # 利用索引，找出字符串中某个字符
'e'
#  要插入一个字符到原来的字符串

>>> str1 = str1[:21] + ('y') + str1[21:]
>>> str1
'I love you , you are ymy dear'
-------------------------------
#  capitalize()          将字符串的第一个字母变成大写，只是返回新字符串，原字符串不变
#  casefold()            将字符串全部变成小写，只是返回新字符串，原字符串不变
#  center(width)      将字符串居中，会使用空格填充
#  count(sub,[start],[end])    可以统计sub在字符串里出现的次数
#  endswith(sub,[start],[end])   检查字符串是否以sub结尾，如果是，返回True
#  expandtabs([tabsize=8])    把tab符号(＼t)转换为空格，默认空格数是8
#  find(sub,[start],[end])    监测sub是否包含在字符串中，如果有，返回索引值；没有返回-1
#  index(sub,[start],[end])   跟find一样，但是如果sub不在字符串中，会产生异常
#  join(sub)        用原字符串作为分隔符，插入到sub中的所有字符之间

>>> a = 'i\tlove'
>>> a
'i\tlove'
>>> a.expandtabs()
'i       love'
>>> str1.join('12345')
'1I love you , you are ymy dear2I love you , you are ymy dear3I love you , you are ymy dear4I love you , you are ymy dear5'
-----------------------------------------------------------------
# format()  字符串的格式化方法
>>> "{0} love {1} . {2}".format('i','you',"baby")
'i love you . baby'
>>> "{0:.1f}{1}".format(28.3763,"kb")
'28.4kb'

#  %         格式化字符及其ASII码
#  %s       格式化字符串
#  %d       格式化整数
#  %o       格式化无符号八进制数
#  %x        格式化无符号十六进制数
#  %X        格式化无符号十六进制数（大写）
#  %f         格式化定点数，可指定小数点后的精度（默认6位）
#  %e        用科学计数法格式化定点数
#  %E        作用同%e，用科学计数法格式化定点数
#  %g        根据值的大小决定使用%f or %e
#  %G       作用同%g，根据值的大小决定使用%f or %E

>>> '%c' % 5
'\x05'
>>> '%c %c %c' % (87,54,25)
'W 6 \x19'
>>> '%c %c %c' % (97,98,99)
'a b c'
>>> '%d +%d = %d' % (4,5,4+5)
'4 +5 = 9'
>>> '%o' % 12
'14'
>>> '%x' % 12
'c'
>>> '%X' % 12
'C'
>>> '%f' % 27.658
'27.658000'
-------------------------------
#  格式化操作辅助命令
#  m.n      m是显示的最小总宽度，n是小数点后的位数
#  -           用于左对齐
#  +          在正数前面显示加号（+）
#  #          在八进制数前面显示0，在十六进制数前面写显示 0x  或  0X
#  0           显示的数字前面填充 0  取代空格

>>> '%f' % 27.658
'27.658000'
>>> '%5.1f' % 27.658
' 27.7'
>>> '%6.3f' % 27.658
'27.658'
>>> '%6.2f' % 27.658
' 27.66'
>>> '%+d' % 5
'+5'
>>> '%#x' % 160
'0xa0'
------------------------------------------
# 字符串转义字符
#    \'                 单引号
#    \"                 双引号
#    \b                退格符
#    \n                换行符
#    \t                  横向制表符
#    \v                  纵向制表符
#    \r                   回车符
#    \f                    换页符
#    \o                  八进制代表的字符（字母o）
#    \x                  十六进制代表的字符
#    \0                  表示空字符（零0）
#    \\                    反斜杠\

------------------------------------------------------------
#  列表、元组、字符串的共同点（都称作序列）
#  ----->  都可以通过索引得到每一个元素
#  ----->    默认索引总是从0开始
#  ----->    可以通过分片的方法得到一个范围内的元素的集合
#  ----->     有很多共同的操作符（重复操作符 *、拼接操作符 +、成员关系操作符 in /not in
--------------------------------------------------------------------

#序列常见BIF

list
# list 有两种形态，一种不带参数，生成空列表
list()     --->  空列表

list(iterable)  -->有一个参数，迭代器
#    迭代：重复反馈过程的活动，目的是为接近或达到所需的目标或结果。每一次对过程的重复称之为迭代。每一次迭代的结果都会被当做下一次迭代的初始值。
#    序列天生就可迭代
----------
>>> a = list()
>>> a
[]
>>> b = 'i love you'
>>> b = list(b)
>>> b
['i', ' ', 'l', 'o', 'v', 'e', ' ', 'y', 'o', 'u']      #把字符串变成了一个列表
>>> c= (1,1,2,3,5,8,13,21,34)
>>> c
(1, 1, 2, 3, 5, 8, 13, 21, 34)
>>> c= list(c)
>>> c
[1, 1, 2, 3, 5, 8, 13, 21, 34]              # 将元组变成了列表

print('------------------------------------over-------------------------------')

tuple([iterable])    ---> 把一个可迭代对象转换为元组
str(object)   -->将参数对象转换为字符串
len( )   -->返回参数的长度
max( )  -->返回参数里的最大值，如果是序列，会按照ASII码来返回
min()  -->返回参数里的最小值
sum(iterable,[start=0])  -->返回序列所有元素之和，和可选参数start的总和
sorted()  -->返回排序 跟sort()一样
reversed()  --> 逆转列表
enumerate()  --> 把列表里每一个元素都和自身的索引值组成一个元组
zip()    -->  返回各个参数的序列组成的元组
>>> len(b)
10
>>> max(b)
'y'
>>> sum(c)
88
>>> sum(c,2)
90
>>> sum(c)
88
>>> sum(c,2)
90
>>> sorted(num)            #默认从小到大
[-43, -34, 2, 12, 34, 54, 65, 324]
>>> reversed(num)
<reversed object at 0x000002A9D6AC3048>
>>> list(reversed(num))                       #  翻转列表，要转化成list
[-34, 12, 54, 324, 65, 34, -43, 2]
>>> list(enumerate(num))                  #前面的值是每个元素对应的索引值
[(0, 2), (1, -43), (2, 34), (3, 65), (4, 324), (5, 54), (6, 12), (7, -34)]

>>> aa = (1,2,3,4,5,6)
>>> bb = (7,8,9,0,11)
>>> list(zip(aa,bb))
[(1, 7), (2, 8), (3, 9), (4, 0), (5, 11)]

print('------------------------------------over-------------------------------')

#   python的组成模块：函数，对象，模块

#   函数  ：完成某一个功能的代码块，创建函数用def

def  myFunction():
	print('这就是一个函数。')

#  调用函数   -->函数只有在被调用的时候才会被执行。
myFunction()

#   为了函数能返回不同的值，需要引入参数。

def myName(name):                                     #  name  是形参，占据一个参数位置
	print(name + 'i love you')

>>> myName('一声')
一声i love you
----------------------------
 def add(num1,num2):
	result = num1 + num2
	print(result)

	
>>> add(2,2)
4

#  函数的返回值  return
--------------------------------------
def add(num1,num2):
	return( num1 + num2)

>>> print(add(4,5))
9
------------------------------------------
#  函数文档  ，利用  myFunction.__doc__  可以把函数文档打印出来
#  函数文档的作用：解释参数，备注等

def add(num1,num2):
	'这里是文档部分，在正常情况下是不会出现在结果里的'
	return( num1 + num2)

>>> print(add(2,2))
4
>>> add.__doc__
'这里是文档部分，在正常情况下是不会出现在结果里的'
--------------------
# 使用 help  也可以看到函数文档

>>> help(add)
Help on function add in module __main__:

add(num1, num2)
    这里是文档部分，在正常情况下是不会出现在结果里的

    ------------------------------------
    # 默认参数 ：定义了默认值的参数
    
    def add(num1 = 2,num2 = 2):       #赋默认值
	print(num1+num2)

	
>>> add()
4
>>> add(3)
5
>>> add(1,4)
5
---------------------------------------------------------------------
# 可变参数   不确定需要多少参数的情况下

def test(*params):
	print('参数的长度：',len(params));
	print('第二个参数是：',params[1]);

	
>>> test(1,'祖国','eee',333)
参数的长度： 4
第二个参数是： 祖国

print('------------------------------------over-------------------------------')
#  返回值
def hello():
	print('hello world!')

	
>>> temp = hello()
hello world!
>>> temp
>>> print(temp)
None
>>> type(temp)
#  <class 'NoneType'>

-----------------------------------
# 变量的作用域 ： 局部变量(local variable)  和 全局变量(global variable)
# 局部变量
def money(price,num):
	account = price * num
	return account

price = float(input('请输入价格：'))
num = int(input('请输入数量：'))
new_money = money(price,num)
print('最后总价是：',new_money)
print(account)           -->这个会报错，因为account是局部变量，只在money()里有效

#全局变量,尽量不要在函数内去修改全局变量
#如果修改，python只是创建一个和全景变量一样名字的值，但不是全景变量
def money(price,num):
	account = price * num
	print('这里试图打印全局变量price的值：',price)
	return account

price = float(input('请输入价格：'))
num = int(input('请输入数量：'))
new_money = money(price,num)
print('最后总价是：',new_money)
--->>>
请输入价格：2
请输入数量：2
这里试图打印全局变量price的值： 2.0
最后总价是： 4.0
------------------
>>> count = 5
 def myfun():
	count = 10
	print(count)

	
>>> myfun()
10
>>> print(count)
5
--------------------------------------------------------------------
# global 关键字：可以在函数内修改全局变量

>>> a = 1
 def mm():
	global a
	a = 2
	print(a)

	
>>> mm()
2
>>> print(a)
2
print('------------------------------------over-------------------------------')

# 内嵌函数:内部函数整个作用域都在外部函数内，即只能在fun1里调用fun2.
def fun1():
	print('fun1正在被调用......')
	def fun2():
		print('fun2正在被调用......')
	fun2()          #'这里一定要加上调用fun2函数，不然fun2不会被执行'

>>> fun1()
	      
fun1正在被调用......
fun2正在被调用......

print('------------------------------------over-------------------------------')
# 闭包 :如果在一个内部函数里，对在外部作用域（但不是在全局作用域)的变量进行引用，内部函数就是一个闭包
def  funx(x):
	def funy(y):
		return x*y
	return funy

>>> funx(9)	      # 返回了一个函数
<function funx.<locals>.funy at 0x000001A778547400>

>>> type(funx(9))	      
# <class 'function'>

>>> i = funx(9)
>>> i(8)	      #i是函数，给函数传递参数
72
>>> funx(9)(8)         #上面的方法就等同于这个，直接赋2个参数	      
72

# nonlocal   让内部函数在调用外部变量时不报错
def  myt():
	x =5
	def myy():
		x * = x
		return x
	return myy()
#  上述函数在调用myt()时会报错
--------------------------------------------------------
def  myt():
	x =5
	def myy():
		nonlocal x
		x * = x
		return x
	return myy()

>>> myt()	      
25

print('------------------------------------over-------------------------------')

#      lambda   表达式：代替函数
#       在写一写简单脚本时，可以用lambda代替定义函数，省去给函数命名的问题，增强代码可读性，避免阅读函数时还要挑到开头去看def 部分

>>> l = lambda x : 2*x + 1
>>> l(3)
7
>>> q = lambda a : a+9
>>> q(3)
12

print('------------------------------------over-------------------------------')
#    filter
#   filter     :  过滤器
#   该函数用于过滤序列，过滤掉不符合条件的元素，返回由符合条件元素组成的新列表
#   该函数接收两个参数，第一个为函数，第二个为序列，序列的每个元素作为参数传递给函数进行判，然后返回 True 或 False，最后将返回 True 的元素放到新列表中。
#   语法： filter(function,iterable)  --->函数，可迭代对象

filter(None,[1,0,False,True])
<filter object at 0x0000021B29110A58>

>>> list(filter(None,[1,0,False,True]))
[1, True]
--------------------------------------
#  过滤出所有奇数
def odd(x):
	return x % 2                                 #  odd--奇数，如果是偶数，x%2会返回0

>>> temp = range(10)                                # 给一个0-9的序列

>>> a =filter(odd,temp)
>>> list(a)
[1, 3, 5, 7, 9]
------------------------------------------
#  利用filter来写这个函数
>>>list(filter(lambda x: x % 2,range(10)))  # 利用filter、lambda写这个函数，就会非常简洁
[1, 3, 5, 7, 9]

print('------------------------------------over-------------------------------')
#map( )
# map()  会根据提供的函数对指定序列做映射
# 第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表
# 语法：map(function, iterable, ...)  --> 函数 一个或多个序列

#  计算序列的平方
>>>list(map(lambda x:x * 2,range(10)))
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# 计算两个列表的加法
>>>list(map(lambda x,y:x+y,[0,1,3,5,6,7],[4,4,4,4,2,3]))
[4, 5, 7, 9, 8, 10]

print('------------------------------------over-------------------------------')
#  递归
#  递归即一个函数可以调用自身。
#  但是，使用递归是要付出代价的。与直接的语句(如while循环)相比，递归函数会耗费更多的运行时间，并且要占用大量的栈空间。递归函数每次调用自身时，都需要把它的状态存到栈中，以便在它调用完自身后，程序可以返回到它原来的状态。未经精心设计的递归函数总是会带来麻烦。
#  解决问题的方法相同，调用函数的参数每次不同（有规律的递增或递减），如果没有规律也就不能适用递归调用。
#  一定要能够在适当的地方结束递归调用。不然可能导致系统崩溃。
#  可以给递归设置层数。import sys    sys.setrecursionlimit(100)

#  使用普通方式来计算一个数的阶乘：

def didi(n):
	result = n
	for i in range(1,n):               #  这里不包含5，那为什么能算到5的阶乘？
		result *=i               # 这个是i，不是n
	return result

num = int(input('输入整数：'))
result = didi(num)
print(result)                                                     # 这3种打印方式结果一样，但最后 一种有点不太懂
print(num, "的阶乘是：" ,result)
print("%d 的阶乘是：%d"%(num,result))
>>>
输入整数：10
3628800
10 的阶乘是： 3628800
10 的阶乘是：3628800
----------------------------------------------
# 使用递归方法来计算阶乘：

def d2(n):
	if n ==1:                                                     # 结束条件，当n=1时，就直接返回1，不再继续下去
		return 1
	else:
		return n * d2(n-1)      # 这里是n*函数自身，函数自身的参数是n-1

num = int(input('输入整数：'))
result = d2(num)
print(result)                                                     
print(num, "的阶乘是：" ,result)
print("%d 的阶乘是：%d"%(num,result))
>>>
输入整数：5
120
5 的阶乘是： 120
5 的阶乘是：120
----------------
# 斐波那契数列
f(n)
n=1,  1
n=2,  1
n>2, f(n-1)+f(n-2)
>>>------------------>>>
#使用递归方法：
def  f1(n):
	if n <1:
		print("输入错误")
		return -1

	if n ==1 or n == 2:
		return 1
	else:
		return f1(n-1) + f1(n-2)
n = int(input("请输入正整数："))
result = f1(n)
print(result)
>>.-------------------->>>
#使用迭代方法：
def f2(n):
	n1 = 1
	n2 = 1
	n3 = 1
	
	if n<1:
		print("输入错误")
		return -1
	while (n-2) > 0:
		n3 = n2 + n1
		n1=n2 
		n2 = n3
		n -=1                             #  太复杂，看不懂
	return n3
n = int(input("请输入正整数："))
result = f2(n)
print(result)
-------------
#  经过测试，当n = 40时，采用递归方法，结果需要28秒！才出现；迭代在一秒之内。
>>>---------------------------->>>
# 汉罗塔
# 
def hlt(n,x,y,z):             # n表示有多少个盘子，x,y,z表示三根柱子
		if n == 1:
			print(x,"---->",z)    # 直接从原位置移到目标位置
		else:
			hlt(n-1,x,z,y)       # 将前n-1个盘子从x移动到y上
			print(x,"---->",z)   # 将最底下的盘子从x移动到z
			hlt(n-1,y,x,z)          #将y上n-1个盘子移动到z上
n = int(input("请输入汉罗塔的盘子数量："))
hlt(n,'x','y','z')                          # 因为x，y，z模拟的是柱子，所以这里可以直接传递字符串
>>>
请输入汉罗塔的盘子数量：3
x ----> z
x ----> y
z ----> y
x ----> z
y ----> x
y ----> z
x ----> z
# 直接告诉我们的是移动盘子的顺序。堪称外挂。

print('------------------------------------over-------------------------------')

#  字典dict{key,value} 
people = ['习大大','景甜','黄晓明','吴亦凡']
words = ['慈祥','单纯','教主','帅']
print('吴亦凡',words[people.index('吴亦凡')])

#  利用字典 字典是映射，要用{}括起来
#  在序列中如果给一个不存在的位置赋值会报错，但在字典中会自动添加一条
dict1 = {'习大大':'慈祥','景甜':'美','黄晓明':'教主','吴亦凡':'帅'}
print("吴亦凡：",dict1['吴亦凡'])
dict2 = dict((('a',10),('b',20),('c',30),('d',40)))         # 也可以用元组，列表来创建字典
# 可以通过键来查找值
dict3 = dict(我 = '小可爱',你 = '大混蛋')              #  键不能加引号！！
>>> dict3
{'我': '小可爱', '你': '大混蛋'}
>>> dict3['我'] = '我是大美女'            # 可以通过这种方式来改变值
>>> dict3
{'我': '我是大美女', '你': '大混蛋'}
-------------------------------------------------------------------------
fromkeys(...)   函数用于创建一个新字典,两个参数，一个键，一个值
>>>dict = {}
>>>dict.fromkeys((1,2,3))
{1: None, 2: None, 3: None}
>>> dict.fromkeys((1,2,3),'000')
{1: '000', 2: '000', 3: '000'}
>>>dict.fromkeys((1,2,3),('000','111','222'))    # 这样是无法分别给123赋值的
{1: ('000', '111', '222'), 2: ('000', '111', '222'), 3: ('000', '111', '222')}
>>> dict.fromkeys((1,3),('numbe'))              #这样达不到修改原字典的内容的目的，它会创建一个新的字典
{1: 'numbe', 3: 'numbe'}
>>>dict1 = dict1.fromkeys(range(20),'good')
>>> dict1
{0: 'good', 1: 'good', 2: 'good', 3: 'good', 4: 'good', 5: 'good', 6: 'good', 7: 'good', 8: 'good', 9: 'good', 10: 'good', 11: 'good', 12: 'good', 13: 'good', 14: 'good', 15: 'good', 16: 'good', 17: 'good', 18: 'good', 19: 'good'}
>>>for eachkey in dict1.key():
	print(eachkey)                                              #打印键
>>>for eachvalue in dict1.value():
	print(eachvalue)                                            #打印值
>>>for eachitem in dict1.items():
	print(eachitem)                                             #打印键值对
------------------------------------------
#访问字典中的值
# 使用get()
>>>dict1.get(22)                #该值不存在,返回none
>>>dict1.get(22,'没有')     #  会返回没有
#  使用get()方法时，前面写想要获取的位置索引，后面跟上如果没有该索引，想要返回的值
-----------------------------------------------
#  clear()      清空字典的值   
>>>dict1,clear()
-----------------------------------------------
# copy    拷贝
a = {1:'a',2:'s',3:'w'}
b = a.copy()                 #全拷贝
c = a                                  #赋值
#虽然现在看起来他们a,b,c看起来值是一样的，但是存放的位置不一样
#copy() 是对对象的真实的拷贝，将对象复制一份放在另一个地方，原对象的改变对其不影响
------------------------------------------------------
#  setdefault()   可利用这个对字典赋值
>>> a.setdefault('q')
>>> a
{1: 'a', 2: 's', 3: 'w', 'q': None}
>>> a.setdefault(8,'girl')
'girl'
>>> a
{1: 'a', 2: 's', 3: 'w', 'q': None, 8: 'girl'}
------------------------------------------------------
>update()    #更新字典
>>>ds = {'旺旺','狗'}
>>>a.update(ds)
>>>a
{1: 'a', 2: 's', 3: 'w', 'q': None, 8: 'girl', '旺旺': '狗'}
print('------------------------over-------------------------------------------')
>  set   集合  #集合和字典很相似，如果一个列表没有体现出明显的映射关系，那么它就是集合
>>> num = {}	
>>> type(num)	  
# <class 'dict'>
>>> num2 = {1,2,3,4,5}	  
>>> type(num2)	  
# <class 'set'>
>>--------------------
#集合里面，重复的元素会被剔除
>>> num2 = {1,1,2,4,5,3,5,3,6,3,6,3}	  
>>> num2	  
{1, 2, 3, 4, 5, 6}
----------------------------------------------------------------------
#集合是无序的，无法通过索引来找到某一个值
#创建集合：直接用{}把元素括起来；使用set()工厂函数
>>> set1 = set([1,2,3,4,5,5,5])	  
>>> set1	  
{1, 2, 3, 4, 5}
-------
#如果要把一个列表里的重复元素去除，在不使用集合的情况下：
>>>list = [1,2,3,2,1,3,2,3,2,53,6,7]
>>>temp = []
for i in list:
	if i not in temp:
		temp.append(i)
temp
[1, 2, 4, 5, 6, 3, 7, 75]
#使用集合方法：
>>>temp1 = set(list)
temp1
{1, 2, 4, 5, 6, 3, 7, 75}      #如果要把集合转换成列表格式，外面再加层list()即可
#因为集合无序，所以在转换时如果对元素顺序有要求，就要注意
-----------------------------------
# 不可变集合  frozenset
>>>num0 = frozenset([1,2,3])    #这样创建的集合是不可变集合，不能对其增改删

print('------------------------over-------------------------------------------')

>文件 
#打开文件   open(file)
#   "r"       以只读方式打开文件（默认）
#   "w"     以写入的方式打开文件，会覆盖已存在的文件
#   "x"       如果文件已经存在，使用此模式会引发异常
#   "a"       以写入模式打开，如果文件存在，则在末尾追加写入
#   "b"       以二进制模式打开
#   "t"        以文本模式打开（默认）
#   "+"       可读写模式
#   "U"       通用换行符支持
----------------
#   读取文件
>>> f = open('E:\\桌面\练习HTML页面.html')
>>> f
<_io.TextIOWrapper name='E:\\桌面\\练习HTML页面.html' mode='r' encoding='cp936'>
--------------------------
#  文件操作方法
#       f.close()                                 关闭文件
#       f.read(size=-1)                   从文件读取size个字符，默认为-1，读取剩余所有字符，返回字符串
#       f.readline()                         以写入模式打开，如果文件存在，则在末尾追加写入
#       f.write(str)                          将字符串str写入文件
#       f.writelines(seq)             向文件写入字符串序列seq，seq是一个返回字符串的可迭代对象
#       f.seek(offset,from)        指针从from(0:起始位置；1:当前位置；2:文件末尾)偏移offset个字节
#       f.tell()                                      返回当前在文件中的位置
      
       
>>> f=open('E:\\桌面\w.txt',encoding= 'UTF-8')
>>> f.read()
'#       f.close()                                 关闭文件\n#       f.read(size=-1)                   从文件读取size个字符，默认为-1，读取剩余所有字符，返回字符串\n#       f.readline()                         以写入模式打开，如果文件存在，则在末尾追加写入\n#       f.write(str)                          将字符串str写入文件\n#       f.writelines(seq)             向文件写入字符串序列seq，seq是一个返回字符串的可迭代对象\n#       f.seek(offset,from)        指针从from(0:起始位置；1:当前位置；2:文件末尾)偏移offset个字节\n#       f.tell()                                      返回当前在文件中的位置\n'

#这时候读出来的文件是没有格式的，如果要每行每行按照文件里的格式来显示，可以用下面的方法。
for each_line in file:
	print(each_line)


---------------------------
新建文件也要用打开的方式
>>> w = open('E:\\桌面\\test1.txt','w')
>>> w.write('我是测试工程师')
7
>>> w.close()

就可以看到桌面上有一个文件。
-------------------------------------------------
# split(sep=none,maxsplit=-1)  不带参数默认以空格为分隔符切片字符串，否则分割maxsplit个子字符串
# 比如‘#       f.close()                             关闭文件 ’ 这一句，想要把#去掉，那么分隔符默认为空格，切片1

将文件里的内容分开保存。
f=open('E:\\桌面\w.txt',encoding= 'UTF-8')

one = []
two = []
count = 1
#把保存文件的代码封装成函数
def save_file(one,two,count):
        file_name_one = 'one_' + str(count) + '.txt'
        file_name_two = 'two_' + str(count) + '.txt'
        one_file = open(file_name_one,'w')
        two_file = open(file_name_two,'w')

        one_file.writelines(one)
        two_file.writelines(two)

for each_line in f:
	if each_line[:6] !=  '==== ':
		# 这里进行字符串分割操作
		(role,line_begin) = each_line.split(1)
		if role =='a':
			one.append(line_begin)
		if role == 'b':
			two.append(line_begin)

	else:
		#  文件分别保存操作
		#  调用保存文件的函数
		save_file(one,two,count)

		one_file.close()
		two_file.close()

		one = []  #初始化
		two = []
		count +=1

save_file(one,two,count)

f.close()

print('------------------------over-------------------------------------------')
模块：模块是一个包含所有你定义的函数和变量的文件，后缀名是.py。模块可以被别的程序引用，以使用该模块中的函数等功能。
OS: Operating System操作系统   导入这个模块后可以使用其函数
pick le  泡菜技术，将所有内容以二进制存放，主要用于某些内容太长的文件，使用pickle可以让代码更简洁
存放：pickling
读取：unpickling
import pickle
list = [1,2,3,24,'sheus',['时间','空间']]
pickle_file = open('list.pickle','wb')   #一定要用'wb'
pickle.dump(list,pickle_file)   #把列表倒进泡菜缸list
pickle_file.close()

pickle_file = open('list.pickle','rb')     #一定要用'rb'
list2 = pickle.load(pickle_file)
>>> print(list2)
[1, 2, 3, 24, 'sheus', ['时间', '空间']]

print('------------------------over-------------------------------------------')

异常处理：exception
file_name = input('请输入文件名：')
f = open(file_name)
print('文件的内容是：')
for each_line in f:
	print(each_line)
如果输入的文件路径不对，或者没有后缀名，就会有异常抛出。

try-except语句
语法：
try:
	监测范围
except Exception[as reason]:
	出现异常后的处理代码
finally:
	无论如何都会被执行的代码
>>>
f = open('我是一个文件.txt')
print(f.read())
f.close()
>>>
#当这个文件不存在时，程序就会报错
#Traceback (most recent call last):
  File "E:\桌面\pythontest\test.py", line 1, in <module>
    f = open('我是一个文件.txt')
FileNotFoundError: [Errno 2] No such file or directory: '我是一个文件.txt'

使用try-except来处理异常
try:
	f = open('我是一个文件.txt')
	print(f.read())
	f.close()
except OSError as reason:                                     #FileNotFoundError这个异常属于OSError
	print('文件错误，错误原因：'+str(reason))        #这样可以将具体的错误打印出来，方便调试程序
这样写，即只有提到的错误类型，才会按照代码处理，如果遇到其他的错误类型，还是会报错
#可以直接这样：except:    这样只要有异常就会按照处理的执行-----但是这样不建议，如果出现了一些没有考虑到的情况，程序员也很难发现。
#两个以上的异常情况，也可以用：except(OSError,TypeError):   这样
---------------
raise语句   引发异常
语法：raise 异常名称--->让程序主动引发一个异常

print('------------------------over-------------------------------------------')

else语句
1、if... else ...  要么怎样，要么不怎样
 if 条件:
 	执行代码
 else:
 	执行代码
2、else 和 while,for 配合使用，else语句只有在顺利完成循环时才执行。如果循环中使用了break，else语句就不会被执行
#   //   除法，取整数 ；% 取余
例：求最大公约数
>>>
def maxFactor(num):
	count = num // 2
	while count >1:
		if num % count == 0:
			print('%d最大的约数是%d' %(num,count))
			break
		count -=1                  #这一句有什么用？好像没有用
	else:
		print('%d是素数' % num)

num = int(input('请输入一个数：'))
maxFactor(num)
>>>
3、没有问题，那就执行吧
>>>
try:
	int(123)
except ValueError as reason:
	print('出错了')
else:
	print('没有问题')
>>>
print('------------------------over-------------------------------------------')
easygui

from easygui import *
import sys

while 1:
	msgbox('您好，欢迎进入第一个界面小游戏^_^')

	msg = "请问你想玩什么游戏呢？"
	title = "小游戏互动"
	choices = ["飞机大战","植物大战僵尸","推箱子","吃鸡"]

	choice = choicebox(msg,title,choices)

	magbox("你的选择是:" + str(choice),"结果")

	msg = "您希望重新开始小游戏吗？"
	title = "请选择"

	if ccbox(msg,title):
		pass
	else:
		sys.exit(0)
print('------------------------over-------------------------------------------')

对象=属性+方法
属性：对象静态的 特征
方法：对象动态的特征
类：首字母默认大写
面向对象的特征：
1.封装---信息隐蔽技术----可以利用方法实现，但不知道如何实现；
2.继承---类继承方法的属性
3.多态---不同对象对同一方法响应不同的行动
例如：
class A:
	def fun(self):
		print('i am A')

class B: 
	def fun(self):
		print("i am B")

a=A()
b=B()
>>>
>>> a.fun()
i am A
>>> b.fun()
i am B

print('------------------------over-------------------------------------------')
面向对象编程：OOP
self：     类似C里的指针,对象的方法都会有一个self。
	当一个对象的方法被调用的时候，对象会将自身作为第一个参数，传给self参数。
	在类的定义的时候，把self写进第一个参数
class Ball:
	def setName(self,name):
		self.name = name
	def kick(self):
		print("我叫%s，是谁在踢我？"% self.name)

>>> a = Ball()
>>> a.setName("小足球")
>>> a.kick()
我叫小足球，是谁在踢我？

--------------
构造方法：__init__(self)---可以重写这个方法，重写定义方法的初始参数
class Ball:
	def __init__(self,name):
		self.name = name
	def kick(self):
		print("我叫%s，是谁在踢我？"% self.name)

>>> b = Ball('小土豆')
>>> b.kick()
我叫小土豆，是谁在踢我？

---------------------
公有/私有：为了实现私有的特征，python采用了 name mangling---名字改编/重整的技术
	         python中，定义私有变量，只需要在变量名或函数名前加上"__"2个下划线即可。
class Person:
	name = "小仙女"

>>> n = Person()
>>> n.name
'小仙女'
-------->
class Person:
	__name = "小仙女"

>>> n = Person()
>>> n.name
这样会抛出异常，找不到变量，除非从内部访问
class Person:
	__name = "小仙女"
	def getName(self):
		return self.__name

>>> n = Person()
>>> n.getName()         #调用内部方法获得变量名
'小仙女'
-------------
name mangling实际上是将变量名改变成：_类名__变量
上面的名字通过下面的方法也能直接访问
>>> n._Person__name
'小仙女'

什么时候需要__init__(self)什么时候不需要，需要看 需求
比如定义一个矩形，需要长宽，这时候就需要初始化参数
__init__()应该返回none
class rectangle:
	def __init__(self,x,y):
		self.x = x
		self.y = y
		#获取周长
	def getPeri(self):
		return (self.x+self.y) * 2
		#获取面积
	def getArea(self):
		return self.x * self.y

>>> re = rectangle(5,6)
>>> re.getPeri()
22
>>> re.getArea()
30
-----------------------------------------------
__new__(class)   对象实例化调用的第一个方法，需要返回一个对象


class newStr(str):
	def __new__(cls,string):
		#调用string的内置方法，将str转变为大写
		string = string.upper()
		return str.__new__(cls,string)

>>> s = newStr("I love my contry!!!")
>>> s
'I LOVE MY CONTRY!!!'

---------------------------------------------
__del__(self)   垃圾回收机制，当一个对象所有的引用都没有时，自动调用该方法
----------------------------------------------
python支持对工厂函数自定义


print('------------------------over-------------------------------------------')
#  继承：class 子类名(父类名)
	

class Parent:
	def myFunction(self):
		print('正在调用父类的方法...')

class child(Parent):
	pass

>>> a = Parent()
>>> b = child()
>>> b.myFunction()
正在调用父类的方法...
>>>
如果子类中定义与父类同名的方法或属性，则会自动覆盖父类对应的方法或属性。
class Parent:
	def myFunction(self):
		print('正在调用父类的方法...')

class child(Parent):
	def myFunction(self):
		print('正在调用子类的方法...')
>>> b = child()
>>> b.myFunction()
正在调用子类的方法...
>>> a = Parent()
>>> a.myFunction()
正在调用父类的方法...

--------------------------------------
import random 
class Fish: 
	def __init__(self):
		self.x = random.randint(0,10)
		self.y = random.randint(0,10)
	def move(self):
		self.x -= 1
		self.y -= 1
		print("我现在的位置在：", self.x,self.y)

class GoldFish(Fish):
	pass
class Carp(Fish):
	pass
class Shark(Fish):
	def __init__(self):
		Fish.__init__(self)              #调用未绑定 的父类的方法，除此还可以用super方法
		super().__init__()                #用super不需要写出父类的名字
		self.hungry = True

	def eat(self):
		if self.hungry:
			print("我饿了。。我得去吃东西了......")
			self.hungry = False
		else:
			print("我现在不饿，去晒会太阳！")


-------------------------
多重继承：继承多个父类的方法
>>>
class One:
	def hello(self):
		print("I AM hello, I AM one")
class Two:
	def hi(self):
		print("I AM hi, I AM two")

class Three(One,Two):
	pass

>>> a = Three()
>>> a.hello()
I AM hello, I AM one
>>> a.hi()
I AM hi, I AM two

print('------------------------over-------------------------------------------')

与类相关的BIF
>#    issubclass(class,classinfo)     如果class是classinfo的一个子类，则返回True；classinfo可以是一个元组；自身被认为是自身的子类
>#     isinstance(object,classinfo)  如果一个实例对象object是属于类classinfo的，则返回true；如果第一个参数传入的不是对象，则返回false
>#     hasattr(object,'name')   attr=attribute:属性   如果object的属性是name，则返回是true
>#     getattr(object,'name',default)   检验object的属性值有无；可选default写假如结果为否，将打印的内容
>#     setattr(object,'name',value)   给特定对象添加属性，同时设置默认值
>#      delattr(object,name)  删除对象的属性，如果属性不存在，则抛出异常
>#      property(fget=none,fset=none,fdel=none,doc=none)  通过属性来设置属性
>>>
class C:
	def __init__(self,size=10):
		self.size = size
	def getSize(self):
		return self.size
	def setSize(self,value):
		self.size = value
	def delSize(self):
		del self.size
	x = property(getSize,setSize,delSize)

>>> c1 = C()
>>> c1.getSize()
10
>>> c1.x
10
>>> c1.x =20
>>> c1.x
20
>>> c1.size
20
>>> c1.getSize()
20
>>> del c1.x

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
			result.append(self.laseted[index] + other.lasted[index])
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
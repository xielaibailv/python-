score = int(input('请输入分数：'))
while score < 0 or score > 100:
	score=int(input('输入错误，请重新输入：'))
if 100 >= score >= 90:
	print('A')
elif 90 > score >= 80:
	print('B')
elif 80 > score >=60:
	print('C')
else:
	print('D')



#写代码时需要考虑代码执行性能，尽量的优化。一般来说，分数服从正太分布，在60--80之间的人最多
#这样写就保证了大多数成绩输进去只用走到第一个判断就执行完成
score = int(input('请输入分数：'))
if 80 > score >= 60:
	print("C")
elif 90 > score >= 80:
	print('B')
elif 100 >= score >= 90:
	print('A')
elif 60 > score >=0:
	print("D")
else:
	print("输入错误！")



# 缩减代码 可以写成  A(条件成立时) if else B(条件不成立时),这样可以更省事
# 为了方便观看可以将代码换行，用 [] 将代码包裹起来，比用反斜杠方便
level = [("c") if 60<= score <= 80 else
	("B") if 80 < score <= 90 else
	("A") if 90 < score <= 100 else
	("D") if 0 < score < 60 else
		 print("输入错误")]
print(level)
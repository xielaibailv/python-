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
'''
 打飞机小游戏编程思路：

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
'''
# 在写程序前先要有思路，框架，即所谓的编程思维。
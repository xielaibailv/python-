while 1:
    number = input("请输入一个整数（输入q结束程序）")


    if number == 'q':
        print("退出程序")
        break

    while not number.isdigit():
        print("请输入整数：", end='')
        number = input()

        num = int(number)
        eight = '{:o}'.format(num)
        sixteen ='%x' % num
        two = bin(num)


        print("十进制 --> 十六进制 ：",end='')
        print(str(num) + '-->' + str(sixteen))
        print("十进制 --> 八进制 ：",end='')
        print(str(num) + '-->' + str(eight))
        print("十进制 --> 二进制 ：",end='')
        print(str(num) + '-->' + str(two))

#上面的程序有一个bug，只有第一次输入的不是整数才会被正确检测到，不能重复测试。


# 教程的代码：

q = True
while q:
    num = input('请输入一个整数(输入Q结束程序)：')
    if num != 'Q':
        num = int(num)
        print('十进制 -> 十六进制 : %d -> 0x%x' % (num, num))
        print('十进制 -> 八进制 : %d -> 0o%o' % (num, num))
        print('十进制 -> 二进制 : %d -> ' % num, bin(num))
    else:
        q = False

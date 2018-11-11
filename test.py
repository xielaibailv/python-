while 1:
    number = input("请输入一个整数（输入q结束程序）")

    if number == 'q':
        break
    elif hasattr(number,'Error'):
        print("请输入整数：",end='')
        number = int(input())
    else:
        eight = '%o' % number
        sixteen ='%x' % number
        two = bin(int(number))


        print("十进制 --> 十六进制 ：",end='')
        print(eight)
        print("十进制 --> 八进制 ：",end='')
        print(sixteen)
        print("十进制 --> 二进制 ：",end='')
        print(two)



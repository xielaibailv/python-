#水仙花数。
#如果一个 3 位数等于其各位数字的立方和，则称这个数为水仙花数。
for i in range(100,999):
    sum = 0
    temp = i
    while temp:
        #  % 取模，返回除法的余数
        sum = sum + (temp%10) **3
        #// 取整除，返回商的整数部分
        temp //= 10
    if sum == i:
        print(i)


    #看不懂。

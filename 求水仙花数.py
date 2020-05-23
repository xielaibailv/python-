#水仙花数。
#如果一个 3 位数等于其各位数字的立方和，则称这个数为水仙花数。
def no1():
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

# --------------------打印的列表一直是空的，不明白为什么----------------------------------------
def hh():
    h = []

    for each in range(100, 1000):
        if each == ((each / 100)**3 + ((each / 10) % 10) ** 3 + (each % 10) ** 3):
            h.append(each)

    return h

# --------------------------------------网上的教程也是这样区分个十百位，一样是空--------------
def nn():
    x = []
    for i in range(100, 1000):
        a = i % 10
        b = (i / 10) % 10
        c = i/100
        if (a**3 + b**3 + c**3) == i:
            x.append(i)

    print(x)

# -------------------------------小甲鱼代码，可以得出水仙花数，但是看不懂-------------
def mm():
    x = []
    for i in range(100, 1000):
        temp = i
        sum = 0
        while temp:
            sum = sum + (temp % 10) ** 3
            temp = temp // 10  # 注意这里用地板除

        if sum == i:
            x.append(i)

    print(x)
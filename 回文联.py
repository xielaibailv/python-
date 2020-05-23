def hw():
    while 1:
        str = input("请输入一句话：")
        str1 = list(str)
        STR =list(reversed(str1))
        if str1 == STR:
            print("是回文联")
        else:
            print("不是回文联")
hw()


# ----------------重写-----------------------------------------------------------

def hwl():
    str = input('请输入一句话：')

    list = []

    for i in str:
        list.append(i)

    list1 = list[::-1]

    if list == list1:
        print('是回文联')
    else:
        print('不是回文联')

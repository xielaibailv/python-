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


# hwl()


def  sad(*args):
    a = 0
    for i in args:
        letter = 0
        space = 0
        nums = 0
        el = 0
        for x in i:
            if x.isdigit():
                nums += 1
            elif x == ' ':
                space += 1
            elif x.isalpha():
                letter += 1
            else:
                el += 1
        a += 1
        print('第{}个字符串共有：英文字母{}个，数字{}个，空格{}个，其他字符{}个。' .format(a, letter, nums, space, el))


sad('qwert12345 7(*^^%', '124335435','03847dhj  hwekd')
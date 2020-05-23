# 密码安全性检查代码

# 低级密码要求：
#   1. 密码由单纯的数字或字母组成
#   2. 密码长度小于等于8位

# 中级密码要求：
#   1. 密码必须由数字、字母或特殊字符（仅限：~!@#$%^&*()_=-/,.?<>;:[]{}|\）任意两种组合
#   2. 密码长度不能低于8位

# 高级密码要求：
#   1. 密码必须由数字、字母及特殊字符（仅限：~!@#$%^&*()_=-/,.?<>;:[]{}|\）三种组合
#   2. 密码只能由字母开头
#   3. 密码长度不能低于16位

#分析：之前的思路是直接来if判断，后来发现这样无法判断完整
#           正确的思路是拆分，将密码需要的元素拆开，分别判断

#将能使用的特殊符号列出来
symbols = r'''~!@#$%^&*()_=-/,.?<>;:[]{}|\ '''
#将所有字母列出来
words = 'abcdefghijklmnopqrstuvwsyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
#将所有数字列出来
numbers = '0123456789'

pwd = input("请输入需要检查的密码组合：")

#长度判断
length = len(pwd)

#密码为空的判断
#isspace()为真不用写出== True
while (pwd.isspace()  or length == 0):
    pwd = input('密码不能为空，请重新输入：')
    length = len(pwd)

if length <= 8:
    len = 1
elif 8 < length < 16:
    len = 2
else:
    len = 3

#除了长度判断，密码的组合类型的判断均可以采用遍历的方法
#那么我们需要创建一个变量，使得密码里有数字是一个值，有字母是一个值，有符号是一个值

flag_con = 0

#判断是否包含特殊字符
for each in pwd:
    if each in symbols:
        flag_con += 1
        break            #只要发现一个就可以不再继续判断了

#判断是否包含字母
for each in pwd:
    if each in words:
        flag_con += 1
        break

#判断是否含有数字
for each in pwd:
    if each in numbers:
        flag_con += 1
        break

#打印结果
while 1:
    print("您的密码安全级别评定为：",end='')
    if len == 1 or flag_con == 1:
        print("低")
    elif len == 3 and flag_con == 3 and (pwd[0] in words):
        print("高")
        print("请继续保持")
        break
    else:
        print("中")

#将下面的内容放出来是因为级别为中和低的都要打印，这样可以使代码简洁
#  \n ：换行     \t：tab键
    print("请按以下方式提升您的密码安全级别：\n\
    \t1. 密码必须由数字、字母及特殊字符三种组合\n\
    \t2. 密码只能由字母开头\n\
    \t3. 密码长度不能低于16位")
    break

    #为啥要用 while 1 呢？
    # 主要是为了实现“如果结果是低或中则打印如何提升密码安全级别的提示，而高则直接退出”

    #为啥把“高”放中间呢？
    # 因为其判断最为麻烦（注意还要求必须是字母开头）
    # 所以很有可能满足了“中”却因为额外的条件满足不了“高”
    # 因此我们把事儿比较多的高放中间判断，满足不了“高”，那就只能是最后的 else“中”了。


    #--------------------------很久之后重写的分割线------------------------------------------------------------------------------------
def check():
    content = '''
     密码安全性检查代码

低级密码要求：
  1. 密码由单纯的数字或字母组成
  2. 密码长度小于等于8位

 中级密码要求：
  1. 密码必须由数字、字母或特殊字符（仅限：~!@#$%^&*()_=-/,.?<>;:[]{}|\）任意两种组合
   2. 密码长度不能低于8位

 高级密码要求：
   1. 密码必须由数字、字母及特殊字符（仅限：~!@#$%^&*()_=-/,.?<>;:[]{}|\）三种组合
   2. 密码只能由字母开头
   3. 密码长度不能低于16位'''

    pwd = input('请输入需要检查的密码组合：')
    pwd_level = level(pwd)
    print('您的密码安全级别评定为：{}'.format(pwd_level))
    if pwd_level == '高':
        print('请继续保持')
    else:
        print("请按以下方式提升您的密码安全级别：\n\
    \t1. 密码必须由数字、字母及特殊字符三种组合\n\
    \t2. 密码只能由字母开头\n\
    \t3. 密码长度不能低于16位")


# 判断密码级别
def level(pwd):
    symbols = r'''`!@#$%^&*()_+-=/*{}[]\|'";:/?,.<>'''
    letter = 'zxcvbnmasdfghjklqwertyuiopZXCVBNMASDFGHJKLQWERTYUIOP'
    nums = '01234567890'
    length = len(pwd)

    # 判断长度

    if length <= 8:
        flag1 = 1
    elif 8 < length <= 16:
        flag1 = 2
    else:
        flag1 = 3

    # 判断复杂度
    flag2 = 0
    # 判断符号，一旦找到一个就跳出
    for each in pwd:
        if each in symbols:
            flag2 += 1
            break

    for each in pwd:
        if each in letter:
            flag2 += 1
            break

    for each in pwd:
        if each in nums:
            flag2 += 1
            break

    if flag1 == 1 or flag2 == 1:
        level = '低'
    elif flag1 == 3 and flag2 == 3 and pwd[0].isalpha():
        level = '高'
    else:
        level = '中'
    return level

check()
# -*- coding:utf-8 _*-
""" 
#   author : YOYO
#   time :  2020/5/20 16:37
#   email : youyou.xu@enesource.com
#   project_name :  python-study
#   file_name :  递归
#   function： 利用递归算阶乘
"""


def power(n):
    if n == 1:
        return n
    else:
        return n * power(n-1)


n = int(input('输入一个数字：'))
print('% d 的阶乘是：% d ' % (n,power(n)))


def hannuota(n,x,y,z):
    if n == 1:
        print(x + '--->'+ z)
    else:
        hannuota(n-1,x,z,y)  # 将n-1ge盘子从x移动到y上 这个步骤需要递归，要调用自己，因为需要重复
        print(x + '--->' + z) # 将最后一个盘子移动到z上，这一步因为不需要递归，不需要调用自己，所以直接打印步骤即可
        hannuota(n-1,y,x,z) # 将n-1ge盘子从y移动到z上


n = int(input('请输入汉诺塔的层数：'))
hannuota(n, 'x轴', 'y轴', 'z轴')

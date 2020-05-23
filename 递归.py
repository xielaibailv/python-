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

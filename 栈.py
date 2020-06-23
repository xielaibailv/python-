# -*- coding:utf-8 _*-

#   author : YOYO
#   time :  2020/6/10 14:32
#   email : youyou.xu@enesource.com
#   project_name :  python-study
#   file_name :  栈
#   function： 定义一个栈（Stack）类，用于模拟一种具有后进先出（LIFO）特性的数据结构
'''
方法名	       含义
isEmpty()	   判断当前栈是否为空（返回 True 或 False）
push()	       往栈的顶部压入一个数据项
pop()	       从栈顶弹出一个数据项（并在栈中删除）
top()	           显示当前栈顶的一个数据项
bottom()	   显示当前栈底的一个数据项
'''


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, obj):
            self.stack.append(obj)

    def isempty(self):
        if self.stack :
            return False
        else:
            return True

    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            print("栈为空")

    def top(self):
        if self.stack:
            return self.stack[-1]
        else:
            print("栈为空")

    def bottom(self):
        if self.stack:
            return self.stack[0]
        else:
            print("栈为空")

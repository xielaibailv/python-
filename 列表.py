#ctrl + alt + i  自动缩进
#编写一个不可改变的列表，记录列表中每个元素被访问的次数

class Countlist:
    #定义列表，因为不确定会传入多少个数，所以使用*args
    #*args 表示任何多个无名参数，类型是一个元组tuple
    def __init__(self,*args):
        #args中的 x(参数) 依次循环出来，赋给self.values列表
        self.values = [x for x in args]
        #count()是列表的一个内置函数，计算元素出现的次数
        #将该数值保存在一个字典中,下标：访问次数，默认是0
        #fromkeys：用于创建一个新字典
        self.count = {}.fromkeys(range(len(self.values)),0)

    def __len__(self):
        return len(self.values)

    def __getitem__(self, key):
        self.count[key] += 1
        return self.values[key]

#创建一个 可变列表（注释Ctrl+/,再按一次去掉注释）
# class Changelist:
#     def __init__(self,*args):
#         self.values = [x for x in args]
#         self.count =
#
#     def __len__(self):
#         return len(self,values)
#     def __getitem__(self,key):
#         self.count += 1
#         return self.values
#     def __setitem__(self,key,values):
#         self.values[key] = values
#     def __delitem__(self,key):
#         del self.values[key]

#测试
def test():
    a = Countlist(2,3,4,6,4,5,8)
    print('test:' ,a[2],a.count)

test()

if __name__ == __main__:
    test()

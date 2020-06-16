# -*- coding:utf-8 _*-
""" 
#   author : YOYO
#   time :  2019/7/15 17:52
#   email : youyou.xu@enesource.com
#   project_name :  python-study
#   file_name :  定制序列
#   function： 
"""

# 定制一个列表，实现记录列表中每个元素被访问的 次数。


class CountList:
    def __init__(self,*args):
        self.values = [x for x in args]  # 把参数存进列表
        self.count = {}.fromkeys(range(len(self.values)), 0)  # 按元素下标：访问次数存进字典

    def __len__(self):
        return len(self.values)

    def __getitem__(self, key):
        self.count[key] += 1  # 一旦该方法被调用，对应下标的元素的访问次数（字典的值）就要+1
        return self.values[key]


# 拓展：还是上面的功能，但更全面，需要支持append()、pop()、extend() 原生列表所拥有的方法。
# 一旦需要支持删除等方法，就不能用字典来存放了，因为列表里的参数的下标会随着操作改变
# 可以用列表来存放对应的元素的计数（然并卵，下面看不懂）
class CountList2(list):
    def __init__(self, *args):
        super().__init__(args)
        self.count = []
        for i in args:
            self.count.append(0)

    def __len__(self):
        return len(self.count)

    def __getitem__(self, key):
        self.count[key] += 1
        return super().__getitem__(key)

    def __setitem__(self, key, value):
        self.count[key] += 1
        super().__setitem__(key, value)

    def __delitem__(self, key):
        del self.count[key]
        super().__delitem__(key)

    def counter(self, key):
        return self.count[key]

    def append(self, value):
        self.count.append(0)
        super().append(value)

    def pop(self, key=-1):
        del self.count[key]
        return super().pop(key)

    def remove(self, value):
        key = super().index(value)
        del self.count[key]
        super().remove(value)

    def insert(self, key, value):
        self.count.insert(key, 0)
        super().insert(key, value)

    def clear(self):
        self.count.clear()
        super().clear()

    def reverse(self):
        self.count.reverse()
        super().reverse()
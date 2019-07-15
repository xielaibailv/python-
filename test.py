import time

# 这是小甲鱼的代码，但是测试发现一样行不通，没有生成文件
# class Record:
#     def __init__(self, initval=None, name=None):
#         self.val = initval
#         self.name = name
#         self.filename = "record.txt"
#
#     def __get__(self, instance, owner):
#         with open(self.filename, 'a', encoding='utf-8') as f:
#             f.write("%s 变量于北京时间 %s 被读取，%s = %s\n" % \
#                     (self.name, time.ctime(), self.name, str(self.val)))
#         return self.val
#
#     def __set__(self, instance, value):
#         filename = "%s_record.txt" % self.name
#         with open(self.filename, 'a', encoding='utf-8') as f:
#             f.write("%s 变量于北京时间 %s 被修改, %s = %s\n" % \
#                     (self.name, time.ctime(), self.name, str(value)))
#         self.val = value


class MyDes:
    def __init__(self, initval=None, name=None):
        self.name = name
        self.val = initval
        self.filename = "record.txt"

        def __get__(self, instance, owner):
            with open(self.name, 'a', encoding='utf-8') as f :
                f.write(self.name + " 变量于北京时间 " + str(time.ctime()) + " 被读取，" + self.name + "=" + self.val )
            return self.val

        def __set__(self, instance, value):
            # self.__dict__[name] = self.value
            with open(self.filename, 'a', encoding='utf-8') as f:
                f.write(self.name + " 变量于北京时间 " + str(time.ctime()) + " 被修改，" + self.name + "=" + self.val)
            self.val = value


class Test:
    x = MyDes(10, 'x')
    y = MyDes(5.5, 'y')





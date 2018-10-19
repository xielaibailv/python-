#温度计
#定义两个描述符类用于描述摄氏度和华氏度两个属性
#两个属性会自动转换
# 华氏度= 摄氏度 *1.8 + 32

#描述符  :  将某种特殊类型的类的实例指派给另一个类的属性。
#描述符类会设计到__get__,__set__,__del__

#定义摄氏度
class Celsius:
    #定义一个初始温度
    def __init__(self,value = 25.0):
        self.value = float(value)              #将数值转换为浮点型
    def __get__(self,instance,owner):
        return self.value
    def __set__(self,instance,value):
        self.value = float(value)

#定义华氏度
class Fahrenheit:
    def __get__(self,instance,owner):
        return instance.cel * 1.8 +32         #instance表示其拥有者类的实例，instance.cel就表示Fahrenheitd 基类temperature里的cel，即调用Celsius()
    def __set__(self,instance,value):
        #当被赋值时，要将此值反转化为摄氏度，被赋的值是float(value)
        instance.cel = (float(value) - 32 )/ 1.8

#定义温度计的两个属性
class Temperature:
    #cel和fah属性各要写一个描述符类
    cel = Celsius()
    fah = Fahrenheit()

def test():
    print("test :  0摄氏度 = %.2f 华氏度" % Celsius(0) )
    print("test : 0华氏度 = %.2f 摄氏度" % Fahrenheit())

test()

if __name__ == "__main__":
    test()

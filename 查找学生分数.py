name = input('请输入待查找的用户名：')
score = [['张三',85],['李四',90],['lucy',88],['lily',99]]
Isfind = False

for each in score:
    #name 一定是在each里面找，不能在score里找，是找不到的
    if name in each:
        print(name + '的得分是' + each[1])
        Isfind = True
        break

#必须要增加一个参数 Isfind,因为下面的if语句获取不到each，只能通过别的值来判断
if Isfind == False:
    print('查无此人')
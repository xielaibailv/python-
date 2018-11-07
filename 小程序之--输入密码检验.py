times = 3
p = '123'
while times:
    pwd = input("请输入密码：")
    if pwd == p:
        print("密码正确，进入程序......")
        break
    elif  '*' in pwd:
        print('密码中不能含有"*"号！您还有' ,times,'次机会！',end='')
        continue
    else:
        times -= 1
        print("密码输入错误，您还有%d 次机会" %(times),end='')
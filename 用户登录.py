#使用if条件循环

class login1:
    print("""
      |---新建用户：n/N---| 
      |---登录账号：e/E---|
      |---退出程序：q/Q---|
    """)

    address_list = dict()



    while 1:
        temp = input("请输入指令：")

        # 注册账号
        if temp == 'n' or temp == 'N':
            name = input("请输入用户名：")
            while 1:       #这一步需要重复判断，所以要再加一个while
                if name not in address_list:
                    pwd = input("请输入密码：")
                    address_list[name] = pwd
                    break
                else:
                    name = input("该用户名已经存在，请重新输入：")
                    # pwd = input("请输入密码：")
                    # address_list[name] = pwd
            print("注册成功，赶紧试试登录吧^_^")

        # 登录账户
        if temp == 'e' or temp == 'E':
            name = input("请输入用户名：")
            while 1:
                if name in address_list:
                    while 1:
                        pwd = input("请输入密码：")
                        if pwd == address_list[name]:
                            print("欢迎进入魔法世界！请点击右上角的 x 结束程序！")
                            break
                        else:
                            print("密码错误哦，请重新尝试!",end='')
                    # 这个break必不可少！！不然就会陷在这个循环里了
                    break
                else:
                    name = input("您输入的用户名不存在，请重新输入：")


        # 退出程序
        if temp == 'q' or temp == 'Q':
            print("正在退出程序...")
            break




#  ------------------------------------------------------------
# 包装成函数

address_list = dict()

def SignIn():
    name = input("请输入用户名：")
    while 1:  # 这一步需要重复判断，所以要再加一个while
        if name not in address_list:
            pwd = input("请输入密码：")
            address_list[name] = pwd
            break
        else:
            name = input("该用户名已经存在，请重新输入：")
    print("注册成功，赶紧试试登录吧^_^")


def LogIn():
    name = input("请输入用户名：")
    while 1:
        if name in address_list:
            while 1:
                pwd = input("请输入密码：")
                if pwd == address_list[name]:
                    print("欢迎进入魔法世界！请点击右上角的 x 结束程序！")
                    break
                else:
                    print("密码错误哦，请重新尝试!", end='')
            break
        else:
            name = input("您输入的用户名不存在，请重新输入：")


def main():
    print("""
          |---新建用户：n/N---| 
          |---登录账号：e/E---|
          |---退出程序：q/Q---|
        """)
    while 1:
        temp = input("请输入指令：")

        if temp not in 'nNeEqQ':
            print("指令输入错误！",end='')
        if temp == 'n' or temp == 'N':
            SignIn()
        if temp == 'e' or temp == 'E':
            LogIn()
        if temp == 'q' or temp == 'Q':
            print("正在退出程序...")
            break


# main()


#------教程-------------------------------------------------
# 下面这种写法，完全避免了我上面那种重复判断输入是否正确的逻辑，它每次都自动结束重新开始
user_data = {}


def new_user():
    prompt = '请输入用户名：'
    while True:
        name = input(prompt)
        if name in user_data:
            prompt = '此用户名已经被使用，请重新输入：'
            continue
        else:
            break

    passwd = input('请输入密码：')
    user_data[name] = passwd
    print('注册成功，赶紧试试登录吧^_^')


def old_user():
    prompt = '请输入用户名：'
    while True:
        name = input(prompt)
        if name not in user_data:
            prompt = '您输入的用户名不存在，请重新输入：'
            continue
        else:
            break

    passwd = input('请输入密码：')
    pwd = user_data.get(name)
    if passwd == pwd:
        print('欢迎进入XXOO系统，请点右上角的X结束程序！')
    else:
        print('密码错误！')


def showmenu():
    prompt = '''
|--- 新建用户：N/n ---|
|--- 登录账号：E/e ---|
|--- 推出程序：Q/q ---|
|--- 请输入指令代码：'''

    while True:
        chosen = False
        while not chosen:
            choice = input(prompt)
            if choice not in 'NnEeQq':
                print('您输入的指令代码错误，请重新输入：')
            else:
                chosen = True

        if choice == 'q' or choice == 'Q':
            break
        if choice == 'n' or choice == 'N':
            new_user()
        if choice == 'e' or choice == 'E':
            old_user()


showmenu()
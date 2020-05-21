def login():
    print("""
          |---新建用户：n/N---| 
          |---登录账号：e/E---|
          |---退出程序：q/Q---|
        """)
    user = {}
    while True:
        code = input('请输入指令代码：')
        if code == 'N' or code == 'n':  # 新建
            name = input('请输入用户名：')
            while name in user:
                name = input('此用户名已经被使用，请重新输入吧：')
            else:
                pwd = input('请输入密码：')
                user[name] = pwd
                print('注册成功，赶紧试试登录吧')

        elif code == 'E' or code == 'e':  # 登录
            name = input('请输入用户名：')
            if name in user:
                pwd = input('请输入密码：')
                if user[name] == pwd:
                    print('欢迎进入登录系统！')
                else:
                    print('密码错误')
            else:
                print('此账号不存在哦')
        elif code == 'Q' or code == 'q':  # 退出
            break
        else:
            print('你输的什么指令哦，人家不懂呢')

login()
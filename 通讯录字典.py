class tongxunlu:
    mydict = dict()
    # 像这种程序运行后首先就打印出来的，不用设置变量，直接打印即可
    print('''                                                     
	 |---欢迎进入通讯录程序---|
	 |---1. 查询联系人资料     ---|
	 |---2. 插入新的联系人     ---|
	 |---3. 删除已有联系人     ---|
	 |---4. 退出通讯录程序     ---|
	 ''')
    while 1:
        temp = int(input("请输入相关的指令代码："))
        if temp == 1:
            name = input("请输入联系人姓名：")
            if name in mydict:
                print(name, ':', mydict[name])
            else:
                print('您输入的姓名不在通讯录中！')

        if temp == 2:
            name = input("请输入联系人姓名：")
            if name not in mydict:
                phone = input("请输入用户联系电话：")
                # mydict.setdefault(name,phone)
                mydict[name] = phone
            else:
                print("您输入的姓名在通讯录中已经存在--->> %s : %s" % (name, mydict[name]))
                if input("是否更新该联系人的联系方式？y/n") == 'y':
                    phone = input("请输入用户联系电话：")
                    mydict[name] = phone
                else:
                    break


        if temp == 3:
            name = input("请输入联系人姓名：")
            if name in mydict:
                mydict.pop(name)
            else:
                print("您输入的姓名不在通讯录中！")

        if temp == 4:
            print('|---感谢使用通讯录程序  ---|')
            break

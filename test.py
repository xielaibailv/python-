class TongXunLu:
    mydict = dict()
    print('''
	 |---欢迎进入通讯录程序---|
	 |---1. 查询联系人资料     ---|
	 |---2. 插入新的联系人     ---|
	 |---3. 删除已有联系人     ---|
	 |---4. 退出通讯录程序     ---|
	 ''')

    def create_user(self):
        name = input('请输入联系人姓名：')
        #
        # if name not in self.mydict:
        #     phone = input('请输入联系电话：')
        #     self.mydict[name] = phone
        # else:
        #     print('您输入的姓名在通讯录中已存在--->> {}：{}'.format(name, self.mydict[name]))
        #     update_user = input('是否修改用户资料（YES/NO）:')
        #     if update_user == 'YES' or update_user == 'yes':
        #         phone = input('请输入联系电话：')
        #         self.mydict[name] = phone
        #         print('已修改成功')
        try:
            print('您输入的姓名在通讯录中已存在--->> {}：{}'.format(name, self.mydict[name]))
            update_user = input('是否修改用户资料（YES/NO）:')
            if update_user == 'YES' or update_user == 'yes':
                phone = input('请输入联系电话：')
                self.mydict[name] = phone
                print('已修改成功')
        except KeyError:
            phone = input('请输入联系电话：')
            self.mydict[name] = phone

    def delete_user(self):
        name = input('请输入想要删除的联系人姓名：')
        # if name in self.mydict:
        #     del self.mydict[name]
        #     print('已删除')
        # else:
        #     print('通讯录查无此人')
        try:
            self.mydict.pop(name)
            print('已删除')
        except KeyError:
            print('通讯录查无此人')


    def select_user(self):# 一次判断是否存在，一次取出值，效率不高
        name = input('请输入想要查询的联系人姓名：')
        # if name in self.mydict:
        #     print('{} : {}'.format(name, self.mydict[name]))
        # else:
        #     print('通讯录查无此人')
        try:
            print('{} : {}'.format(name, self.mydict[name]))
        except KeyError:
            print('通讯录查无此人')

    def userbook(self):
        while 1:
            try:
                flag = int(input('请输入相关的指令代码：'))
            except ValueError:
                print('指令无法识别')
                break
            if flag != 4:
                if flag == 2:
                    self.create_user()
                elif flag == 1:
                    self.select_user()
                elif flag == 3:
                    self.delete_user()
                else:
                    print('指令错误')

            else:
                print('------感谢使用通讯录------')
                break


tongxunlu = TongXunLu().userbook()
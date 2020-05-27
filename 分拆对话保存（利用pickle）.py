#将一个文件里的对话，按 =====分成不同的段落，每个段落里按照说话的角色分为boy，girl，
#使用pickle技术保存文件
# 小甲鱼的对话单独保存为boy_*.txt的文件（去掉“小甲鱼:”）
# 小客服的对话单独保存为girl_*.txt的文件（去掉“小客服:”）
# 分别保存为boy_1.txt, girl_1.txt，boy_2.txt, girl_2.txt, boy_3.txt, gril_3.txt共6个文件


import pickle
def save_file(boy,girl,count):
    #利用pickle保存文件
    name1 = open('boy_' + str(count) + '.txt','wb')
    name2 = open('girl_' + str(count) + '.txt','wb')
    pickle.dump(boy,name1)
    pickle.dump(girl,name2)
    name1.close()
    name2.close()

def split_file(filename):
    count = 1
    boy = []
    girl = []

    f = open(filename)

    for each_line in f:
        if each_line[:6] != '======':  #说明是一个段落里的
            (role,words) = each_line.split(':',1)   #只切一刀
            if role == '小甲鱼':
                boy.append(words)
            else:
                girl.append(words)

        else:   #一个段落已经结束，则应该将前面的对话保存下来
            save_file(boy,girl,count)

            #将boy，girl初始化，准备接收下一段对话
            #这个初始化不能跟else同级，这样会导致每循环一行就会被调用一次
            count += 1
            boy = []
            girl = []
    #这为什么还要调用一遍？因为第三个段落是没有====的！！
    save_file(boy, girl, count)
    f.close()

split_file('record.txt')

# ------------重写---------------------2020.00527-------------------------------------------------

def save_file2(boy, girl, num):
    boy_file = 'boy_' + str(num) + '.pickle'
    girl_file = 'girl_' + str(num) + '.pickle'
    with open(boy_file, 'wb') as bf:
        pickle.dump(boy, bf)
    with open(girl_file, 'wb') as gf:
        pickle.dump(girl, gf)


def splitfile():
    boy = []
    girl = []
    num = 1

    with open('record.txt') as f:
        for each in f:
            if each[:6] != '======':
                (name, content) = each.split(':', 1)
                if name == '小甲鱼':
                    boy.append(content)
                elif name == '小客服':
                    girl.append(content)
            else:
                save_file2(boy, girl, num)
                num += 1
                boy = []
                girl = []
            save_file2(boy, girl, num)


splitfile()


#  ------------分别保存对话-----------------------------------------------------------------------------
def save_file2(boy, girl, num):
    boy_file = ('boy_{}.txt'.format(num))
    girl_file = ('girl_{}.txt'.format(num))
    with open(boy_file, 'w') as file1:
        file1.writelines(boy)
    with open(girl_file, 'w') as file1:
        file1.writelines(girl)


def dofile():
    f = open('record.txt')
    boy = []
    girl = []
    num = 1

    for each in f:
        if each[:6] != '======': # 字符串分割
            (name,content) = each.split(':', 1)  # 1表示分割几次
            if name == '小甲鱼':
                boy.append(content)
            elif name == '小客服':
                girl.append(content)
        else: # 分别保存文件
            save_file2(boy, girl, num)
            num += 1
            boy = []
            girl = []
        save_file2(boy, girl, num) # 在循环后第三段话还需要保存一下

    f.close()


dofile()
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
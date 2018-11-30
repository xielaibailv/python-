#代码尽量按照函数来进行封装
# 1. 编写一个程序，接受用户的输入并保存为新的文件

#因为filename会设置为全局变量，所以是放在了函数外，需要将这个参数传入函数
def write_file(filename):
    f = open(filename, "wt")
    print("请输入内容【单独输入':wq'保存退出】：")

    #输入内容
    while True:
        words = input()
        if words != 'wq':
            #考虑到换行
            f.write("%s\n" % words)
        else:
            break
    #close一定 要和while同级，在循环之外！！！
    f.close()

filename = input("请输入文件名：")
write_file(filename)

#-----------------------------------------------------------------------------

# 2.比较用户输入的两个文件不同的行数

#将比较两个文件的不同放在一个函数里
def different(file1,file2):
    f1 = open(file1)
    f2 = open(file2)
    count = 0           #统计行数
    diff = []                #统计不一样的数量
    for line1 in f1:
        line2 = f2.readline()     #两个文件各读一行
        count += 1
        if line1 != line2:
            diff.append(count)     #这样就能把第几行不一样的信息保存起来

    f1.close()
    f2.close()
    return diff


file1 = input('请输入需要比较的头一个文件名：')
file2 = input('请输入需要比较的另一个文件名：')
#因为上面的函数返回了diff，但需要用变量存起来，下面才能调用
diff = different(file1,file2)

if len(diff) == 0:
    print("两份文件完全一样！")
else:
    print("两个文件总共有%d处不一样" % len(diff))
    for each in diff:                                       #不能直接打印diff
        print("第%d行不一样" % each)



#------------------------------------------------------------------------
#  3. 编写一个程序，当用户输入文件名和行数（N）后，将该文件的前N行内容打印到屏幕上

#number 1

def read_file(filename):
    f = open(filename)
    print("请输入您想要阅读的行数：", end='')
    lines = input()
    line = 0
    for each_line in f:
            line += 1
            if line <= int(lines):
                print(each_line)
            else:
                break
    f.close()

filename = input("请输入文件名：")
read_file(filename)


#number 2,更简洁
def read_file(filename,lines):
    f = open(filename)
    #这时候就不能用each_line在文件里循环了，而是在行数里循环
    for i in range(int(lines)):
        print(f.readline())

    f.close()


filename = input("请输入文件名：")
lines =input("请输入您想要阅读的行数：")
read_file(filename,lines)


#number 3,  教程
def file_view(file_name, line_num):
    print('\n文件%s的前%s的内容如下：\n' % (file_name, line_num))
    f = open(file_name)
    for i in range(int(line_num)):
        print(f.readline(), end= '')

    f.close()

file_name = input(r'请输入要打开的文件（C:\\test.txt）：')
line_num = input('请输入需要显示该文件前几行：')
file_view(file_name, line_num)


#----------------------------------------------------------------------------------

# 4. 在上一题的基础上扩展，用户可以随意输入需要显示的行数
#因为这个输入的形式有多种，所以需要一一考虑到
#首先要定义开始和结束两个变量

def read_file(filename,lines):
    #将begin，end从用户输入的内容里提取出来
    (begin,end) = lines.split(':')

    # Python strip()方法用于删除首尾指定字符（默认是空格和换行符）或字符序列
    # 这里代码的意义：假如用户输的是 :，则分别给begin，end赋值
    #其实也没有都无所谓，不影响结果
    # if lines.strip() == ':':
    #     begin = '1'
    #     end = '-1'

    if begin == '':
        begin = '1'
    if end == '':
        end = '-1'

    if begin == '1' and end == '-1':
        prompt = '的全文'
    elif begin == '1':
        prompt = '从开始到%s行' % end
    elif end == '-1':
        prompt = '从%s行到末尾' % begin
    else:
        prompt = '从%s 行到 %s行' % (begin,end)

    print("\n%s文件%s内容如下：\n" %(filename,prompt))

    begin = int(begin) - 1
    end = int(end)
    len = end - begin

    f = open(filename)
    #这里的作用是假如begin不为1，这里就把begin前面的内容消耗掉
    for i in range(begin):
        f.readline()
    #主要是为了防止抛出异常
    if len < 0:
        print(f.read())
    else:
        for j in range(len):
            print(f.readline(),end='')

    f.close()


filename = input("请输入文件名：")
lines =input("请输入您想要阅读的行数位置【格式如 13:21 或 :21 或 21: 或 : 】：")
read_file(filename,lines)



#------------------------------------------------------------------------

# 4.编写一个程序，实现“全部替换”功能

def file_replace(file_name, rep_word, new_word):
    f_read = open(file_name)

    content = []
    count = 0

    for eachline in f_read:
        if rep_word in eachline:
            count = eachline.count(rep_word) #count感觉应该用这个
            eachline = eachline.replace(rep_word, new_word)
        content.append(eachline)

    decide = input('\n文件 %s 中共有%s个【%s】\n您确定要把所有的【%s】替换为【%s】吗？\n【YES/NO】：' \
                   % (file_name, count, rep_word, rep_word, new_word))

    if decide in ['YES', 'Yes', 'yes']:
        f_write = open(file_name, 'w')
        f_write.writelines(content)
        f_write.close()

    f_read.close()


file_name = input('请输入文件名：')
rep_word = input('请输入需要替换的单词或字符：')
new_word = input('请输入新的单词或字符：')
file_replace(file_name, rep_word, new_word)


#------------------------------------------------------------------------

# 4. 将一个文件里的内容按某种方式分成两个文件保存

f=open('E:\\桌面\w.txt',encoding= 'UTF-8')

one = []
two = []
count = 1
#把保存文件的代码封装成函数
def save_file(one,two,count):
    file_name_one = 'one_' + str(count) + '.txt'
    file_name_two = 'two_' + str(count) + '.txt'
    one_file = open(file_name_one,'w')
    two_file = open(file_name_two,'w')

    one_file.writelines(one)
    two_file.writelines(two)

    one_file.close()
    two_file.close()

for each_line in f:
    if each_line[:6] !=  '==== ':
        # 这里进行字符串分割操作
        (role,line_begin) = each_line.split(':')
        if role =='a':
            one.append(line_begin)
        if role == 'b':
            two.append(line_begin)

    else:
        #  文件分别保存操作
        #  调用保存文件的函数
        save_file(one,two,count)

        # one_file.close()
        # two_file.close()

        one = []  #初始化
        two = []
        count +=1

save_file(one,two,count)

f.close()
def CountStr(*params):
    #获取参数的长度，这个长度对于字符串来说，就是获取有几个字符串（不是几个字母）
    length = len(params)
    #这里开始对每个字符串进行处理
    #所有的参数，都可转化为一个参数如何处理*n次
    #i  是从0 开始，所以后面打印是第几个参数时要写  i  +1
    for i in range(length):
        words = 0            #字母，英语渣就不要在意细节了
        numbers = 0       #数字
        kg = 0                    #空格
        others = 0              #特殊字符
        #在每个字符串里面开始循环，这一回是针对每个字母了
        for each in params[i]:
            if each.isalpha():
                words += 1
            elif each.isdigit():
                numbers += 1
            elif each.isspace():
                kg += 1
            else:
                others += 1
        print('第%d 个字符串共有：%d个字母，\
        %d个数字，%d个空格，%d个特殊字符。' %(i+1,words,numbers,kg,others))

CountStr('I love fishc.com.', 'I love you, you love me.')
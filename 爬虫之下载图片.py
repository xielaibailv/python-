import urllib.request
import easygui


def save_cat1():
    # open url既可以是一个地址也可以是一个实例化对象
    response = urllib.request.urlopen('http://placekitten.com/200/200')
    # 所以除了上面的办法，还可以用下面这种，实例化request
    # res = urllib.request.Request('http://placekitten.com/200/200')
    # response = urllib.request.urlopen(res)

    # 读取到指定的内容,除了用read方法，还可以用  geturl(),   info(),  getcode() 方法
    cat_img = response.read()

    # 使用geturl()
    # response.geturl()
    # 使用info()
    # response.info()
    # print(response.info())
    # 使用getcode(),返回的是请求的状态码
    # response.getcode()

    # 给图片命名，所有文件都是二进制，所以可以用写入的方式将图片’保存‘
    # “wb”指：二进制格式
    with open('cat2_200_200.jpg','wb') as f:
        f.write(cat_img)


# 添加UI界面，让用户选择存放位置和下载图片大小
def save_cat2():
    size = easygui.multenterbox('请填写想下载的喵喵的尺寸', title='下载一只喵', fields=['宽', '高'], values=[400, 600])
    save_dir = easygui.diropenbox('请选择存放图片的文件夹')

    # 用户输入的数字保存下来是str格式，得转换
    url = 'http://placekitten.com/%d/%d' % (int(size[0]), int(size[1]))
    # 拼接图片保存地址
    save_file = save_dir + '/cat_%d_%d.jpg' % (int(size[0]), int(size[1]))
    response = urllib.request.urlopen(url, timeout=100)
    cat_img = response.read()

    # save cats'photos
    with open(save_file, 'wb') as f:
        f.write(cat_img)



save_cat2()
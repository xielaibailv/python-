#将图片转换为字符画
'''
步骤：
1、将图片转换为灰度模式
2、根据图像中每个像素的灰度值（灰度深浅）找到不同复杂度的 ASCII 字符一一映射
3、复杂的字符串（@#￥%&）看上去比较“黑”，简单的字符串（-+=）看上去比较“白”
4、使用类：pillow.需要先安装
'''
from PIL import Image

def pictureToAscii(picture,asciis,zoom,vscale):
    img = Image.open(picture)
    # convert("L")  方法：将彩色图片转换为灰度模式
    out = img.convert("L")
    #获取图片的宽度和高度
    #Image对象的size 属性即宽高度
    width,height = out.size
    #需要重新调整下宽高度，不然像素太多导致文件太大
    #利用 resize() 方法
    #将缩放值zoom参数化
    #这一定要两个括号！！！！！
    out = out.resize((int(width * zoom),int(height * zoom * vscale)))
    ascii_len = len(asciis)
    texts = ''

    #灰度模式的图像，每个像素有一个灰度值，值的范围是 0~255（0是纯黑色，255是纯白色）
    for row in range(out.height):
        for col in range(out.width):
            #利用 getpixel()  获取每个像素的灰度值
            #这一定要两个括号！！！！！
            gray = out.getpixel((col,row))
            #根据灰度值选择不同复杂度的ASCII字符
            texts += asciis[int((gray / 255) * (ascii_len - 1))]
        texts += '\n'
    return texts

def main():
    picture = input("请输入需要转换的图片名称/地址：")
    #字符按照“灰度级别”从高到底排列
    asciis = '@%#*+=-:.'
    #因为图片太大会导致像素点太多，一个像素就是一个字符 ，需要将图片进行缩放
    #如果图片不大就不用设置这个参数
    #设置缩放系数
    zoom = 0.5
    #因为字符的长宽不等
    #设置垂直比例系数
    vscale = 0.5
    texts = pictureToAscii(picture,asciis,zoom,vscale)

    with open("ascii.txt","w") as file:
        file.write(texts)

if __name__ == "__main__":
    main()

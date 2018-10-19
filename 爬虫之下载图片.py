import urllib.request

#open url既可以是一个地址也可以是一个实例化对象
response = urllib.request.urlopen('http://placekitten.com/200/200')
#所以除了上面的办法，还可以用下面这种
# res = urllib.request.Request('http://placekitten.com/200/200')
# response = urllib.request.urlopen(res)

#读取到指定的内容,除了用read方法，还可以用  geturl(),   info(),  getcode() 方法
cat_img = response.read()

#使用geturl()
# response.geturl()
#使用info()
# response.info()
# print(response.info())
#使用getcode(),返回的是请求的状态码
# response.getcode()

#给图片命名，所有文件都是二进制，所以可以用写入的方式将图片’保存‘
#“wb”指：二进制格式
with open('cat2_200_200.jpg','wb') as f:
    f.write(cat_img)
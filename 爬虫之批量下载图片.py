import urllib.request
import os


def open_url(url):
    # head = {}
    # head['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36'
    # req = urllib.request.Request(url, head)
    # response = urllib.request.urlopen(url)
    # html = response.read()
    # return html
    # req = urllib.request.Request(url)
    # req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36')
    # 为什么下面括号里一会是url,一会是req，不明白
    response = urllib.request.urlopen(url)
    html = response.read()   # open_url单独作为一个函数，这里就不能加decode
    return html

# 获取当前页面所在的页码数
# 为什么不能直接写入URL，因为不同的页数URL不同，所以URL需要参数传递
def get_page(url):
    html = open_url(url).decode('utf-8')
    a = html.find('span class="current-comment-page">[') +35
    b = html.find(']</span>', a)
    return html[a:b]


# 获取每张图片地址
# 经过测试就是这里没有正确工作，不是程序的问题，是网站改变了
def find_img(url):
    html = open_url(url).decode('utf-8')
    # 因为有很多 个地址，所以需要把地址放到一个列表存起来
    # 同时因为一页有很多个图片，所以需要一个循环；
    # 同时寻找元素会遇到找完最后一个后找不到的情况，此时需要跳出
    img_address = []

    a = html.find('a href=')

    while a != -1:                # 假如没有找到img src=，a会返回-1
        b = html.find('.jpg',a,a+255)           # 最后一个参数表示如果找不到，需要给一个最大的寻找范围，即最多找255个字符
        if b != -1:
            img_address.append(html[a+9:b+4])   # a+16,b+4是指分别不要img src='和要.jpg
        else:
            b = a + 9

        # 寻找下一张图片
        a = html.find('a href=',b)

    return img_address
    # 测试该函数能否正确运行，因为结果是一个列表，需要用for循环
    # for each in img_address:
    #     print(each)




# 按图片地址保存图片在文件夹
def save_imgs(folder, img_address):
    for each in img_address:
        filename = each.split('/')[-1]  # 按照图片地址里的/进行切片,然后取最后一个片段
        with open(filename,'wb') as f:
            img = open_url(each)
            f.write(img)




# 主函数，下载图片，默认文件夹，默认页数
def download_mm(folder = 'girl',pages = 5):
    # 创建文件夹，进入文件夹
    os.mkdir(folder)
    os.chdir(folder)

    # 进入页面，发起请求，获得第一页的页数
    url = "http://jandan.net/ooxx/"
    # 获取当前页面所在的页码数
    page_num = int(get_page(url))

    #遍历不同页码的页面，根据页码拼接URL地址
    for i in range(pages):
        page_num -= i
        page_url = url + 'page-' + str(page_num) + '#comments'
        #获取这个页面上的图片地址
        img_address = find_img(page_url)
        #按图片地址保存图片在文件夹
        save_imgs(folder,img_address)

if __name__ == '__main__':
        download_mm()





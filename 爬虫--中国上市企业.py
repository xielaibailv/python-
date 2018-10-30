from urllib.request import Request,urlopen
import urllib.parse
import csv
import pandas
from urllib.parse import urlencode
from urllib.error import URLError

# url = "http://s.askci.com/stock/1?type="
# req = Request(url)
# response = urlopen(req)
# html = response.read().decode('utf-8')
# tb = pandas.read_html(html)
# tb1 = pandas.DataFrame(tb)
# tb1.to_csv(r'1.csv',  encoding='utf_8_sig')
# print("OK")

#这一段代码虽然想要查询前10页的数据，但实际上只查到了第9页的数据
# for i in range(1,10):
#     url = "http://s.askci.com/stock/%s ?type= " %(str(i))
#     req = Request(url)
#     response = urlopen(req)
#     html = response.read().decode('utf-8')
#     tb = pandas.read_html(html)[0]
#     tb1 = pandas.DataFrame(tb)    #没这个函数下面的to_csv用不了押
#     tb1.to_csv(r'1.csv',  encoding='utf_8_sig',header=1,index=0)
#     # html.to_csv(r'1.csv',mode='a',encoding='utf-8',header=1,index=0)
#     print('第'+str(i)+'页抓取完成')

# for i in range(1,10):
#     url = "http://s.askci.com/stock/ 1?type= "
#     req = Request(url)
#     response = urlopen(req)
#     html = response.read().decode('utf-8')
#     #Pandas的read_html方法能够读取带有table标签的网页中的表格
#     tb = pandas.read_html(html)[0]
#     # tb1 = pandas.DataFrame(url)  #没这个函数下面的to_csv用不了押
#     tb.to_csv(r'1.csv',  encoding='utf_8_sig',header=1,index=0)
#     # html.to_csv(r'1.csv',mode='a',encoding='utf-8',header=1,index=0)
#     print('第'+str(i)+'页抓取完成')

# #网上教程的代码，亲测可用。是该网站另一个页面，url组成不太一样，里面还有些内容没有理解
# for i in range(1,178):  # 爬取全部177页数据
# 	url = 'http://s.askci.com/stock/a/?reportTime=2017-12-31&pageNum=%s' % (str(i))
# 	tb = pandas.read_html(url)[3] #经观察发现所需表格是网页中第4个表格，故为[3]
# 	tb.to_csv(r'1.csv', mode='a', encoding='utf_8_sig', header=1, index=0)
# 	print('第'+str(i)+'页抓取完成')


#第一次，尝试抓取第一页的数据，success
# url = "http://s.askci.com/stock/a/?reportTime=2017-12-31&pageNum=1"
# req = Request(url)
# response = urlopen(req)
# html = response.read().decode('utf-8')
# table = pandas.read_html(html)[3]
# #一定要加上encoding='utf-8-sig'，不知道为什么，少了sig都不行，不然是乱码
# table.to_csv(r'test_one.csv',encoding='utf-8-sig')
# print("ok")



# #第二次，尝试获取全部数据（178页）,faild  试过很多遍，就是不行，只能抓到最后一页的，前面的猜测被覆盖掉了
# #success!!!!!!
# #添加header
# head = {}
# head['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36'
# #打开网页，页码从1-178循环
# for i in range(1,178):
#     url = "http://s.askci.com/stock/a/?reportTime=2017-12-31&pageNum=%s" % (str(i))
#     #如果head以上面的方式写，下面就必须写headers=head，不然response = urlopen(req)会报错
#     req = Request(url,headers=head)
#     # req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36')
#     #下面不需要添加encode,decode
#     response = urlopen(req)
#     html = response.read()
#     # # 获取页面上表格内容
#     table = pandas.read_html(html)[3]
#     # 保存到csv
#     table.to_csv(r'test_two.csv',encoding='utf-8-sig',mode='a')
#     print('爬取第' + str(i) + '页的数据完成！')



#精简代码，并且加上异常处理，写成完整的模块
#写成模块一定一定要记得加测试类，不然根本就跑不起来 T_T
def download_csv():
    try:
        for i in range(1,178):
            url = 'http://s.askci.com/stock/a/?reportTime=2017-12-31&pageNum= %s' %(str(i))
            table = pandas.read_html(url)[3]
            #终于试出来mode=‘a'有什么用了！！！！
            #没有它根本爬取不到多页的信息，只能抓到最后一页！！！！！！
            #为什么不知道！！！！！！
            table.to_csv(r'中国上市企业信息.csv',mode='a',encoding='utf-8-sig',header=1, index=0)
            print('爬取第' + str(i) + '页的数据完成！')
    except URLError as e:
        if hasattr(e, 'reason'):
            print('连接有问题。')
            print('reason:', e.reason)
        elif hasattr(e, 'code'):
            print('请求失败。')
            print('code:', e.code)
    else:
        print("ok")

if __name__ == "__main__":
    download_csv()




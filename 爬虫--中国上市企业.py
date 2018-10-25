from urllib.request import Request,urlopen
import urllib.parse
import csv
import pandas

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
url = "http://s.askci.com/stock/a/?reportTime=2017-12-31&pageNum=1"
req = Request(url)
response = urlopen(req)
html = response.read().decode('utf-8')
table = pandas.read_html(html)[3]
#一定要加上encoding='utf-8-sig'，不知道为什么，少了sig都不行，不然是乱码
table.to_csv(r'test.csv',encoding='utf-8-sig')
print("ok")
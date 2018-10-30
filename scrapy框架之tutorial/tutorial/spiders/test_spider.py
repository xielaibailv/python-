import scrspy

clsss  TestSpider(scrapy.Spider):
	#必须唯一，确定这只蜘蛛的名字
	name = "test"
	#是一个列表，确定要爬取的地址的域名
	allowed_domains = ['sogou.com']
	#从哪里开始爬取
	start_urls = [
	"https://news.jxcn.cn/?from=jx14"
	]
	#分析的函数,接收response，并分析，从里面提取出item
 	def parse(self,response):
 		filename = response.url.split("/")[-2]
 		with open(filename,"wb") as f:
 			f.write(response.body)


import scrspy
from tutorial.items import DmozItem


class TestSpider(scrapy.Spider):
    # 必须唯一，确定这只蜘蛛的名字
    name = "test"
    # 是一个列表，确定要爬取的地址的域名
    allowed_domains = ['sogou.com']
    # 从哪里开始爬取
    start_urls = [
        "https://news.jxcn.cn/?from=jx14"
    ]


    # 分析的函数,接收response，并分析，从里面提取出item
    def parse(self, response):
        # filename = response.url.split("/")[-2]
        # with open(filename,"wb") as f:
        # 	f.write(response.body)
        # 实例化selector对象,selector需要一个参数response
        
        sel = scrapy.selector.Selector(response)
        sites = sel.xpath('//ul[@class="directory-url"]/li')
        items = []
        for site in sites:
            # 实例化item对象
            item = DmozItem()
            item['title'] = site.xpath('a/text()').extract()
            item['link'] = site.xpath('a/@href').extract()
            item['desc'] = site.xpath('text()').extract()
            items.append(item)

        return items


import scrapy,re,time,random
from ..items import ThesaurusItem


class ProSpider(scrapy.Spider):
    name = 'pro'
    allowed_domains = ['httpbin.org']
    page = 0
    max_page = 1000
    delay = 3
    url = 'https://httpbin.org//delay/1?page={}'
    proxy_list=[]

    def start_requests(self):
        for i in range(1, self.max_page + 1):
            yield scrapy.Request(url=self.url.format(i),callback=self.parse, meta={'page': i})
    #http://dev.kdlapi.com/api/getproxy/?orderid=911516928866534&num=20&protocol=1&method=1&sep=2
    # f = open('../enForCrawl.txt', 'r', encoding='utf-8').readline()
    # word_list = f.split(' ')
    # start_urls=['https://www.youdao.com/example/blng/eng/{}/'.format(word) for word in word_list[0:1]]
    # print(start_urls)
    # def __init__(self):
    #     super(ThesaurusSpider, self).__init__(name='youdao_thesaurus')

    def parse(self, response):
        print(response.text[-80:])
        # self.proxy_list = response.text.split('\n')
        # print('这是代理池:',self.proxy_list)
        # proxy = 'http://60.168.206.117:1133'#'http://'+random.choice(self.proxy_list)
        # print('这是当前代理:',proxy)

        #yield scrapy.Request(url='http://httpbin.org/ip', callback=self.category_parse, errback=self.err_parse,dont_filter=True,)# meta={"proxy":proxy})
        #yield scrapy.Request(url='http://dev.kdlapi.com/api/getproxy/?orderid=911516928866534&num=2&protocol=1&method=1&sep=2',callback=self.proxy_parse, errback=self.err_parse, dont_filter=True)
    #     proxy=random.choice(self.proxy_list)
    #     yield scrapy.Request(url='http://httpbin.org/ip',callback=self.category_parse,errback=self.err_parse,dont_filter=True,meta={"proxy":proxy})
    #     while True:
    #         yield scrapy.Request(url='http://dev.kdlapi.com/api/getproxy/?orderid=911516928866534&num=2&protocol=1&method=1&sep=2',callback=self.proxy_parse,errback=self.err_parse,dont_filter=True)
    #         time.sleep(10)
    #
    # def proxy_parse(self,response):
    #     self.proxy_list = response.text.split('\n')
    # def category_parse(self,response):
    #     print(response.text)
    # def err_parse(self,response):
    #     #列表页解析
    #     err_num=0
    #     while err_num<3:
    #         return response
    #
    #
    # def close(spider, reason):
    #     print('scrapy-arstechnica抓取完成,共抓取:',spider.page,'条数据')
    #
    # ##self.crawler.engine.close_spider(self, "关闭spider")
    # #scrapy crawl pro



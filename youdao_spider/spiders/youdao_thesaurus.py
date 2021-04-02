import scrapy,re,time,random
from ..items import ThesaurusItem
#有道同义词

class ThesaurusSpider(scrapy.Spider):
    name = 'youdao_thesaurus'
    allowed_domains = ['youdao.com']
    page = 0
    def __init__(self):
        super(ThesaurusSpider,self).__init__(name='youdao_thesaurus')
        f = open('../enForCrawl.txt', 'r', encoding='utf-8').readline()
        word_list = f.split(' ')
        self.start_urls=['https://www.youdao.com/w/{}/'.format(word) for word in word_list[0:10]]


    def parse(self, response):
        print(response.url[25:-1])
        list_tongyi=response.xpath("//div[@class='trans-container']//li/text()").extract()
        print(list_tongyi)
    def category_parse(self,response):
        #列表页解析
        pass
        #yield scrapy.Request(response.urljoin(next_url), callback=self.category_parse)

    def close(spider, reason):
        print('scrapy-arstechnica抓取完成,共抓取:',spider.page,'条数据')

    ##self.crawler.engine.close_spider(self, "关闭spider")
    #scrapy crawl youdao_thesaurus



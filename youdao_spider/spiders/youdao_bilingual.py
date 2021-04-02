import scrapy,json,time#,requests,re,time,random
from ..items import BilingualItem
#有道双语例句


class BilingualSpider(scrapy.Spider):
    name = 'youdao_bilingual'
    allowed_domains = ['youdao.com',]
    page = 0
    custom_settings = {
        'LOG_FILE':'youdao_bilingual.log',
        'DOWNLOAD_DELAY':1,
        'CONCURRENT_REQUESTS':32,
        'CONCURRENT_REQUESTS_PER_DOMAIN':32,
    }
    # start_urls = ['http://dev.kdlapi.com/api/getproxy/?orderid=911516928866534&num=0&protocol=2&method=1&sep=2']
    def __init__(self):
        super(BilingualSpider, self).__init__(name='youdao_bilingual')
        f = open(r'./bilingual_2021-0331.txt', 'r', encoding='utf-8')
        self.start_urls = ['https://www.youdao.com/example/blng/eng/{}/'.format(word.replace('\n','')) for word in f.readlines()[0:10]] #7040
        print('****',self.start_urls)
        f.close()

    def parse(self, response):
        item = BilingualItem()
        try:
            for data in response.xpath("//div[@id='bilingual']//li"):
                list_en = ''.join(data.xpath("./p[1]//text()").extract()).strip().replace('\n', '')
                list_cn = ''.join(data.xpath("./p[2]//text()").extract()).strip().replace('\n', '')
                item['bilingual_result'] = list_cn+'|||'+list_en
                yield item
            self.page += 1
            print('---------------------------',time.strftime('%Y.%m.%d-%H:%M:%S'), '第', self.page, '条抓取成功 ', response.url,'----------------------')
        except Exception as e:
            print(e)



    def close(self, reason):
        print('scrapy-arstechnica抓取完成,共抓取:',self.page,'条数据')

    ##self.crawler.engine.close_spider(self, "关闭spider")
    #scrapy crawl youdao_bilingual -s JOBDIR=bilingual_received/001



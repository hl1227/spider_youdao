import scrapy,json,time#,requests,re,time,random
from ..items import BilingualItem



class chinese_gratisSpider(scrapy.Spider):
    name = 'chinese_gratis'
    allowed_domains = ['chinese.gratis']
    start_urls = ['https://chinese.gratis/bible/index.php?q=&livre=&chapitre=1&verset=&Submit=Ok&action=recherche']
    page=0
    def parse(self, response):
        list=response.xpath("//center//a/@href").extract()
        for u in list[:1]:
            yield scrapy.Request(response.urljoin(u),callback=self.info)

    def info(self,response):
        en=response.xpath("//div[@id='verset_01O0101']//span/text()").extract_first()
        print(en)
    #
    # def category_parse(self,response):
    #     item = BilingualItem()
    #     json_list = []
    #     try:
    #         json_d = {'start_word': response.url[40:-1]}
    #         json_list.append(json_d)
    #         for data in response.xpath("//div[@id='bilingual']//li"):
    #             js_dict = {}
    #             list_en = ''.join(data.xpath("./p[1]//text()").extract()).strip().replace('\n', '')
    #             list_cn = ''.join(data.xpath("./p[2]//text()").extract()).strip().replace('\n', '')
    #             js_dict[list_cn] = list_en
    #             json_list.append(js_dict)
    #         if len(json_list) >2 and len(json_list[0]['start_word'])>=1:
    #             date = json.dumps(json_list, ensure_ascii=False)
    #             item['bilingual_result'] = date
    #             print(time.strftime('%Y.%m.%d-%H:%M:%S'),'第',self.page,'条抓取成功 ',response.url)
    #             self.page+=1
    #             yield item
    #     except Exception:pass

    # def errback(self, response):
    #     print('这是个错误')
    #     yield scrapy.Request(response.url,callback=self.category_parse,errback=self.errback)
    def close(self, reason):
        print('scrapy-arstechnica抓取完成,共抓取:',self.page,'条数据')

    ##self.crawler.engine.close_spider(self, "关闭spider")
    #scrapy crawl chinese_gratis -s JOBDIR=bilingual_received/001



import scrapy,json,time,random,pymysql,datetime,logging
from hashlib import md5
from ..items import TranslateItem
import scrapy.downloadermiddlewares.retry
#有道翻译 英语-中文
class TranslateSpider(scrapy.Spider):
    name = 'youdao_translate'
    allowed_domains = ['youdao.com']
    custom_settings = {
        'LOG_FILE': 'youdao_translate.log',
        # 'DOWNLOAD_DELAY': 1,
        # 'CONCURRENT_REQUESTS': 32,
        # 'CONCURRENT_REQUESTS_PER_DOMAIN': 32,
    }
    # mysql------------------------------------------
    def __init__(self):
        super(TranslateSpider,self).__init__(name='youdao_translate')
        self.conn = pymysql.Connect(
            host='154.212.112.247',
            port=13006,
            # 数据库名：
            db='test',
            user="root",
            passwd='itfkgsbxf3nyw6s1',
            charset='utf8')
        self.cur = self.conn.cursor()
        self.post_url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'

    def start_requests(self):
        for id_num in range(60000,70000):
            find_sql = 'select id,content from Data_Content_665 where id = {}'.format(id_num)
            self.cur.execute(find_sql)
            content = self.cur.fetchone()
            if content ==None:
                continue
            id_count=0
            print('#############################开始获取数据 id为:', id_num)
            try:
                for txt in content[1].replace('\n','').split('" />')[1].split('.')[0:-2]:
                    if len(txt.strip()) >= 40:
                        id_count+=1
                        word = txt.strip()
                        salt, sign, time = self.get_salt_sign_ts(word)
                        formdata = {
                            'i': word,
                            'from': 'AUTO',
                            'to': 'AUTO',
                            'smartresult': 'dict',
                            'client': 'fanyideskweb',
                            'salt': salt,
                            'sign': sign,
                            'doctype': 'json',
                            'version': '2.1',
                            'keyfrom': 'fanyi.web',
                            'action': 'FY_BY_CLICKBUTTION'}
                        headers = {
                            "Cookie": "OUTFOX_SEARCH_USER_ID=1179223152@10.169.0.84; OUTFOX_SEARCH_USER_ID_NCOO=486165313.7169691; _ntes_nnid=d37f109c7e9382d0a82cdbbd07b16dbd,1614847556602; JSESSIONID=abcvIemUPbbvjcX9eu_Gx; DICT_UGC=be3af0da19b5c5e6aa4e17bd8d90b28a|; ___rl__test__cookies={}".format(time),
                            "Referer": "http://fanyi.youdao.com/?keyfrom=dict2.top"}
                        yield scrapy.FormRequest(
                            url=self.post_url,
                            formdata=formdata,
                            headers=headers,
                            callback=self.parse,
                            meta={"id_num":'{}:{}'.format(id_num,id_count)})
                self.id_count=id_num
            except Exception as e:
                print(e)
                continue
            logging.warning('成功获取------------ID为:{}'.format(id_num))
    def get_salt_sign_ts(self, word):
        time1 = str(int(time.time() * 1000))
        salt = time1 + str(random.randint(0, 9))
        string = "fanyideskweb" + word + salt + "Tbh5E8=q6U3EXe+&L[4c@"
        s = md5()
        s.update(string.encode())
        sign = s.hexdigest()
        return salt, sign, time1

    def parse(self, response):
        if response.status == 407:
            self.crawler.engine.close_spider(self, "err:电脑IP改变,关闭spider")
        elif response.status == 200:
            item=TranslateItem()
            data=response.body.decode()
            id_num=response.meta['id_num']
            print('-------------------',datetime.datetime.now(),'ID为:',id_num,'状态码:',response.status,'-------------------')
            if data == '{"errorCode":50}':
                logging.error('有道翻译爬虫参数错误:{} id_num:{}'.format(data,id_num))
            else:
                try:
                    html = json.loads(data)
                    data_cn=html['translateResult'][0][0]['tgt']
                    data_en=html['translateResult'][0][0]['src']
                    item['data_cn']=data_cn
                    item['data_en']=data_en
                    yield item
                except Exception as e:print(e)
        else:
            logging.error('错误状态码:{}'.format(response.status))
            print('***********误状态码:',response.status)

    def close(self, reason):
        self.conn.close()
        print(reason,'抓取至ID:',self.id_count)
        logging.warning('{},抓取至ID:{}'.format(reason,self.id_count))
        logging.warning('-'*40)
    ##self.crawler.engine.close_spider(self, "关闭spider")
    #scrapy crawl youdao_translate





# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json

class YoudaoSpiderPipeline:
    def open_spider(self, spider):
        self.bilingual_file = open(r'./bilingual_2021-0331_result.txt', 'a+', encoding='utf-8')
        self.translate_file = open(r'./tech_translate6_7W.txt','a+', encoding='utf-8')
        print('文件打开成功')
    def process_item(self, item, spider):
        if item.__class__.__name__ == 'TranslateItem':
            self.translate_file.write(item['data_en']+'|||'+item['data_cn']+'\n')
            print(item['data_cn'])
            print(item['data_en'])
        elif item.__class__.__name__ == 'BilingualItem':
            self.bilingual_file.write(item['bilingual_result']+'\n')
            print('存入成功',item['bilingual_result'])
        return item

    def close_spider(self, spider):
        #self.bilingual_file.close()
        self.translate_file.close()
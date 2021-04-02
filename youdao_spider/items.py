# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ThesaurusItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    start_word=scrapy.Field()
    thesaurus_result=scrapy.Field()
    creat_time = scrapy.Field()  # 创建时间
    status = scrapy.Field()  # 状态


class BilingualItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #start_word = scrapy.Field()
    bilingual_result = scrapy.Field()
    # creat_time = scrapy.Field()  # 创建时间
    # status = scrapy.Field()  # 状态

class TranslateItem(scrapy.Item):
    data_cn=scrapy.Field()
    data_en=scrapy.Field()
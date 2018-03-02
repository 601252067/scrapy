# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class DoubanItem(scrapy.Item):
    zh_title = scrapy.Field()
    en_title = scrapy.Field()
    ot_title = scrapy.Field()
    content = scrapy.Field()
    star = scrapy.Field()
    quote = scrapy.Field()
    top = scrapy.Field()

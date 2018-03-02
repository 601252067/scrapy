# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class SpRedisItem(scrapy.Item):
    # 用户名
    username = scrapy.Field()
    # 年龄
    age = scrapy.Field()
    # 头像链接
    header_url = scrapy.Field()
    # 内心独白
    content = scrapy.Field()
    # 籍贯
    place_from = scrapy.Field()
    # 学历
    education = scrapy.Field()
    # 爱好
    hobby = scrapy.Field()
    # 个人主页
    soucrce_url = scrapy.Field()
    # 数据来源网站
    # 一般都得标注这个(或者写成爬虫的名字)
    data_from = scrapy.Field()
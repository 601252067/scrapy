# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ItJuziItem(scrapy.Item):
    # 公司名称
    name = scrapy.Field()
    # 成立时间
    time = scrapy.Field()
    # 地点
    location = scrapy.Field()
    # 分类
    category = scrapy.Field()
    # 简介
    desc = scrapy.Field()
    # 标签
    tag = scrapy.Field()
    # 基本信息
    infos = scrapy.Field()



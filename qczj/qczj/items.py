# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QczjItem(scrapy.Item):
    # 品牌名称
    car_name = scrapy.Field()
    # 汽车最低价格
    car_min_price = scrapy.Field()
    # 汽车最高价
    car_max_price = scrapy.Field()
    # 平均价
    car_avg_price = scrapy.Field()
    # 车身结构
    car_type = scrapy.Field()
    # 用户评分
    car_score = scrapy.Field()

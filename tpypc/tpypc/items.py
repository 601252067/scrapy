# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TpypcItem(scrapy.Item):
    # 汽车名称
    car_name = scrapy.Field()
    # 新车最高价
    car_min_price = scrapy.Field()
    # 汽车最低价
    car_max_price = scrapy.Field()
    # 汽车平均价
    car_avg_price = scrapy.Field()
    # 排量
    car_output = scrapy.Field()
    # 汽车级别
    car_lever = scrapy.Field()
    # 车身类型
    car_type = scrapy.Field()
    # 汽车评分
    car_score = scrapy.Field()
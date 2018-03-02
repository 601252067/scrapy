# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DianpinItem(scrapy.Item):
    # 商户名称
    shop_name = scrapy.Field()
    # 商户评星
    shop_start = scrapy.Field()
    # 商户总评论数目
    comment_num = scrapy.Field()
    # 人均消费
    avg_spend = scrapy.Field()
    # 口味评分
    taste_score = scrapy.Field()
    # 环境评分
    milieu_score = scrapy.Field()
    # 服务评分
    service_score = scrapy.Field()
    # 商户地址
    shop_addr = scrapy.Field()
    # 商户电话
    shop_tel = scrapy.Field()
    # 好评数
    good_comment = scrapy.Field()
    # 中评数
    average_comment = scrapy.Field()
    # 差评数
    bad_comment = scrapy.Field()

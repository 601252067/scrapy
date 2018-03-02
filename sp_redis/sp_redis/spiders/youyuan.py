# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
# from scrapy.spiders import CrawlSpider, Rule

# 这个是导入Redis_crawlSpider
from scrapy_redis.spiders import RedisCrawlSpider
# 导入scrapy的Rule
from scrapy.spiders import Rule
# 导入item
from sp_redis.items import SpRedisItem

class YouyuanSpider(RedisCrawlSpider):
    name = 'youyuan'
    # allowed_domains = ['youyuan.com']
    # start_urls = ['http://youyuan.com/']
    # 这个redis_key相当于start_urls
    redis_key = 'myspider:start_urls'

    # rules延续,保持不变
    rules = (
        Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    )



    def parse_item(self, response):
        print(response.url)



# TODO: .*?可以相当于不指定具体规则,相当于所有
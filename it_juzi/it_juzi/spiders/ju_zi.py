# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

# from scrapy_redis.spiders import RedisCrawlSpider
class JuZiSpider(CrawlSpider):
    name = 'ju_zi'
    allowed_domains = ['itjuzi.com']
    start_urls = ['https://www.itjuzi.com/company?page=1']
    # redis_key = 'juzispider:start_urls'

    rules = (
        Rule(LinkExtractor(allow=r'company/?page=\d+$'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        print(response.url)

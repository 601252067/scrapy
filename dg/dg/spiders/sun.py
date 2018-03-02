# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from dg.items import SunItem


class SunSpider(CrawlSpider):
    name = 'sun'
    allowed_domains = ['sun0769.com']
    start_urls = ['http://wz.sun0769.com/index.php/question/questionType?type=4&page=0']

    rules = (
        Rule(LinkExtractor(allow=r'type=4&page=\d+')),
        Rule(LinkExtractor(allow=r'question/\d+/\d+.shtml'), callback='parse_item', follow=False)
    )

    def parse_item(self, response):
        item = SunItem()

        # 使用 "".join()是为了解决字符串中存在的"xa0"的问题
        item['title'] = "".join(response.xpath("//div[@class='pagecenter p3']/div[@class='greyframe']/div[@class='ctitle']/div[@class='cleft']/strong/text()").extract()[0])#response_data.split(' ')[0]
        item['content'] = response.xpath("//div[@class='c1 text14_2']/text()").extract()[0]
        item['link'] = response.url
        yield item
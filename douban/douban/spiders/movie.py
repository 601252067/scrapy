# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from douban.items import DoubanItem


class MovieSpider(CrawlSpider):
    name = 'movie'
    allowed_domains = ['douban.com']
    start_urls = ['https://movie.douban.com/top250?start=0']

    rules = (
        Rule(LinkExtractor(allow=r'start=\d+'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = DoubanItem()
        for each in response.xpath("//div[@class='item']"):
            item['zh_title'] = each.xpath("./div[@class='info']/div[@class='hd']/a/span[1]/text()").extract()[0]
            item['en_title'] = each.xpath("./div[@class='info']/div[@class='hd']/a/span[2]/text()").extract()[0].replace('\xa0',' ').replace('/','')
            item['ot_title'] = each.xpath("./div[@class='info']/div[@class='hd']/a/span[@class='other']/text()").extract()[0].replace('\xa0',' ').replace('/','')
            item['content'] = each.xpath("./div[@class='info']/div[@class='bd']/p/text()").extract()[0].replace('\xa0',' ')
            item['star'] = each.xpath("./div[@class='info']/div[@class='bd']/div[@class='star']/span[@class='rating_num']/text()").extract()[0]
            quote = each.xpath("./div[@class='info']/div[@class='bd']/p[@class='quote']/span/text()").extract()

            if len(quote) != 0:
                item['quote'] = quote[0]
            else:
                item['quote'] = 'Nothing'

            item['top'] = each.xpath("./div[@class='pic']/em/text()").extract()[0]
            # yield item
            print(item)


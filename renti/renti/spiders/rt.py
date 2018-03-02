# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from renti.items import RentiItem


class RtSpider(CrawlSpider):
    name = 'rt'
    allowed_domains = ['www.666rt.co']
    start_urls = ['http://www.666rt.co/ArtZG/']

    rules = (
        Rule(LinkExtractor(allow=r'list\d+.html')),
        Rule(LinkExtractor(allow=r'ArtZG/\d+/$'),callback='parse_item', follow=True),
        #Rule(LinkExtractor(allow=r'www.666rt.co/ArtZG/\d+/\d+.html'), callback='parse_item', follow=True),
    )


    def parse_item(self, response):
        print(response.url)
        # item = RentiItem()
        # item['img_path'] = response.xpath("//title/text()").extract()[0].split('-')[0]
        # item['img_name'] = response.xpath("//div[@class='imgbox']/a/img/@alt").extract()[0]
        # item['img_url'] = 'http://www.666rt.co%s'%response.xpath("//div[@class='imgbox']/a/img/@src").extract()[0]
        # yield item
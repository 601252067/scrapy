# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from scrapy.http.cookies import CookieJar


from dianpin.items import DianpinItem

class DpSpider(CrawlSpider):
    name = 'dp'
    allowed_domains = ['dianping.com']
    start_urls = ['http://www.dianping.com/shanghai/ch10/p1']
    rules = (
        Rule(LinkExtractor(allow=r'/ch10/p\d+$'), callback='parse_item', follow=True),
        #Rule(LinkExtractor(allow=r'/shop/\d+$'), callback='parse_item', follow=True)
    )




    def parse_item(self, response):
        print(response.url)



    def test(self, response):
        item = DianpinItem()
        # 商户名称
        shop_name = response.xpath("//h1[@class='shop-name']/text()").extract()  # 聚酒锅(金虹桥国际中心店)
        # 商户评星
        shop_start = response.xpath("//div[@class='brief-info']/span/@title").extract()  # 五星商户
        # 商户总评论数目
        comment_num = response.xpath("//span[@id='reviewCount']/text()").extract()  # 804条评论
        # 人均消费
        avg_spend = response.xpath("//span[@id='avgPriceTitle']/text()").extract()  # 人均：562元
        # 口味评分
        taste_score = response.xpath("//span[@id='comment_score']/span[1]/text()").extract()  # 口味：9.1
        # 环境评分
        milieu_score = response.xpath("//span[@id='comment_score']/span[2]/text()").extract()  # 环境：9.3
        # 服务评分
        service_score = response.xpath("//span[@id='comment_score']/span[3]/text()").extract()  # 服务：9.0
        # 商户地址
        shop_addr = response.xpath(
            "//div[@class='expand-info address']/span[2]/@title").extract()  # 茅台路179号金虹桥国际中心L3楼310-311-312
        # 商户电话
        shop_tel = response.xpath("//p[@class='expand-info tel']/span[2]/text()").extract()  # 021-52310131
        # 好评数
        good_comment = response.xpath(
            "//div[@class='comment-filter-box clearfix J-filter']/label[3]/span/text()").extract()  # (734)
        # 中评数
        average_comment = response.xpath(
            "//div[@class='comment-filter-box clearfix J-filter']/label[4]/span/text()").extract()  # (43)
        # 差评数
        bad_comment = response.xpath(
            "//div[@class='comment-filter-box clearfix J-filter']/label[5]/span/text()").extract()  # (27)

        item['shop_name'] = shop_name
        item['shop_start'] = shop_start
        yield item


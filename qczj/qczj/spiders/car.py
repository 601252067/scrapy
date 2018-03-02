# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import time
from qczj.items import QczjItem


class CarSpider(CrawlSpider):
    name = 'car'
    allowed_domains = ['car.autohome.com.cn']
    start_urls = ['https://car.autohome.com.cn/zhaoche/jiage/']


    # https://www.autohome.com.cn/4077/
    # rules = (
    #     Rule(LinkExtractor(allow=r'www.autohome.com.cn/\d+/'), callback='parse_item', follow=True),
    # )

    link_extractor = {
        'follow_url': LinkExtractor(allow=r'www.autohome.com.cn/\d+/$'),
        # 'content': LinkExtractor(allow='bbscon,board,\w+,file,M\.\d+\.A\.html$'),
    }

    cookies = {
        "fvlid=1516887699506whI4hEHufF; sessionid=57397AFE-4D52-4280-B761-EA48E447EC1B%7C%7C2018-01-25+21%3A41%3A40.131%7C%7Cwww.baidu.com; ahpau=1; Hm_lvt_9924a05a5a75caf05dbbfb51af638b07=1516887708; sessionuid=57397AFE-4D52-4280-B761-EA48E447EC1B%7C%7C2018-01-25+21%3A41%3A40.131%7C%7Cwww.baidu.com; ahsids=872_3157_75_3343_81_3839; sessionip=66.112.212.8; sessionvid=29D7F5AA-1E05-4E88-A830-F7C16F25B1EE; area=999999; ahpvno=3; ref=www.baidu.com%7C0%7C0%7C0%7C2018-01-27+00%3A31%3A12.856%7C2018-01-25+21%3A41%3A40.131; Hm_lpvt_9924a05a5a75caf05dbbfb51af638b07=1516984275"
    }






    def start_requests(self):
        yield scrapy.FormRequest(self.start_urls[0], cookies=self.cookies, callback=self.parse)

    def parse(self, response):
        # for link in self.link_extractor['follow_url'].extract_links(response):
        for link in self.link_extractor['follow_url'].extract_links(response):
            print(link.url)
            yield scrapy.Request(url=link.url, callback=self.data_handle)
        #yield scrapy.Request(url=)

    def data_handle(self, response):
        test = response.xpath("//div[@class='autoseries-info']/dl/dt[1]/a[1]/text()").extract()
        if len(test) == 0:
            print('---None---')
        else:
            print(test[0])

    def parse_item(self, response):
        print('---start---')
        body = response.body
        str_time = str(time.time())
        file_name = '%s.html'%str_time.split('.')[0]
        with open(file_name,'w+') as f:
            f.write(response.url)
            f.close()
        print('---end---')
        #print(response.url)
       # print('qweqweqw')
        # item = QczjItem()
        # item['car_name'] = response.xpath("//div[@class='subnav-title-name']/a/h1/text()").extract()[0]
        # car_price = response.xpath("//div[@class='autoseries-info']/dl/dt[1]/a[1]/text()").extract()[0].replace('万','').split('-')
        # item['car_min_price'] = car_price[0]
        # item['car_max_price'] = car_price[1]
        # item['car_avg_price'] = (car_price[0] + car_price[1]) / 2
        # item['car_type'] = response.xpath("//div[@class='autoseries-info']/dl/dd[3]/a[3]").extract()[0]
        # item['car_score'] = response.xpath("//div[@class='koubei-score']/div[1]/a[2]/text()").extract()[0]
        # yield item

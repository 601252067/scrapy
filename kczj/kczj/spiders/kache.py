# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from kczj.items import KczjItem

class KacheSpider(CrawlSpider):
    name = 'kache'
    allowed_domains = ['360che.com']
    start_urls = ['https://dealer.360che.com/dealer_0_0_0_0_0_0_c1.html']

    rules = (
        Rule(LinkExtractor(allow=r'/dealer_0_0_0_0_0_0_c\d+.html'), callback='dealer_info', follow=True),
        #Rule(LinkExtractor(allow=r'product.360che.com/s\d+/\d+_\d+_index.html'), callback='info_handle', follow=True),
    )

    def dealer_info(self, response):
        item = KczjItem()
        print(response.url)
        for each in response.xpath("//div[@class='inside']/ul[@class='dealers']/li/div[@class='detail']"):
            shop_name = each.xpath("./h2/a/text()").extract()[0]

            shop_tag_1_data = response.xpath("./span[1]/text()").extract()
            if len(shop_tag_1_data) > 0:
                shop_tag_1 = shop_tag_1_data[0]
            else:
                shop_tag_1 = 'None'

            shop_tag_2_data = response.xpath("./span[2]/text()").extract()
            if len(shop_tag_2_data) > 0:
                shop_tag_2 = shop_tag_2_data[0]
            else:
                shop_tag_2 = 'None'

            shop_tag_3_data = response.xpath("./span[3]/text()").extract()
            if len(shop_tag_3_data) > 0:
                shop_tag_3 = shop_tag_3_data[0]
            else:
                shop_tag_3 = 'None'

            shop_addr_data = response.xpath("./p[2]/text()").extract()
            if len(shop_addr_data) > 0:
                addr = shop_addr_data[0].replace(' ','')
                if len(addr) > 0:
                    shop_addr = addr.replace('\r','').replace('\n','')
                else:
                    shop_addr = response.xpath("./p[1]/text()").extract()[0].replace(' ','').replace('\r','').replace('\n','')
            else:
                # shop_addr =
                addr = response.xpath("./p[1]/text()").extract()
                if len(addr) > 0:
                    shop_addr = addr[0].replace(' ','').replace('\r','').replace('\n','')
                else:
                    shop_addr = 'None'

            shop_tel_data = response.xpath("./p[3]/span/text()").extract()
            if len(shop_tel_data) > 0:
                tel = shop_tel_data[0]
                if len(tel) > 0:
                    shop_tel = tel
                else:
                    shop_tel = 'None'
            else:
                shop_tel = 'None'

            item['shop_name'] = shop_name
            item['shop_tag_1'] = shop_tag_1
            item['shop_tag_2'] = shop_tag_2
            item['shop_tag_3'] = shop_tag_3
            item['shop_addr'] = shop_addr
            item['shop_tel'] = shop_tel
            print(item)
            yield item

    # def info_handle(self, response):
    #     item = KczjItem()
    #     print(response.url)
    #     for each in response.xpath("//div[@class='price-wrap']/table/tbody/tr"):
    #         car_name_data = each.xpath("./td[1]/a/text()").extract()
    #         if len(car_name_data) > 0:
    #             car_name = car_name_data[0].replace('\n','').replace('\t','')
    #         else:
    #             car_name = '页面无此项'
    #
    #         car_tag_1_data = each.xpath("./td[1]/div/span[1]/text()").extract()
    #         if len(car_tag_1_data) > 0:
    #             car_tag_1 = car_tag_1_data[0]
    #         else:
    #             car_tag_1 = '页面无此项'
    #
    #         car_tag_2_data = each.xpath("./td[1]/div/span[2]/text()").extract()
    #         if len(car_tag_2_data) > 0:
    #             car_tag_2 = car_tag_2_data[0]
    #         else:
    #             car_tag_2 = '页面无此项'
    #
    #         car_tag_3_data = each.xpath("./td[1]/div/span[3]/text()").extract()
    #         if len(car_tag_3_data) > 0:
    #             car_tag_3 = car_tag_3_data[0]
    #         else:
    #             car_tag_3 = '页面无此项'
    #
    #
    #         car_tag_4_data = each.xpath("./td[1]/div/span[4]/text()").extract()
    #         if len(car_tag_4_data) > 0:
    #             car_tag_4 = car_tag_4_data[0]
    #         else:
    #             car_tag_4 = '页面无此项'
    #
    #         car_hot = each.xpath("./td[2]/span/var/@style").extract()[0].replace('width:','')
    #         car_factory_price = each.xpath("./td[3]/span/text()").extract()[0]
    #         car_location_price = each.xpath("td[4]/a[1]/text()").extract()[0]
    #
    #         item['car_name'] = car_name
    #         item['car_tag_1'] = car_tag_1
    #         item['car_tag_2'] = car_tag_2
    #         item['car_tag_3'] = car_tag_3
    #         item['car_tag_4'] = car_tag_4
    #         item['car_hot'] = car_hot
    #         item['car_factory_price'] = car_factory_price
    #         item['car_location_price'] = car_location_price
    #         print(item)
    #         yield item

    # def parse_item(self, response):
    #     item = KczjItem()
    #     print(response.url)
    #     for each in response.xpath("//div[@id='tractor_price']/ul/li/div[@class='content']"):
    #         car_name = each.xpath("./div[@class='caption']/h2/a/text()").extract()[0] # 车名
    #         car_drive = each.xpath("./div[@class='config']/p[1]/a/text()").extract()[0] # 驱动形式
    #         car_engine = each.xpath("./div[@class='config']/p[2]/a/text()").extract()[0] # 发动机
    #         car_horsepower = each.xpath("./div[@class='config']/p[3]/a/text()").extract()[0] # 马力
    #         car_emission = each.xpath("./div[@class='config']/p[4]/text()").extract()[0].replace('\n','').replace('\t','').replace('\xa0','').replace(' ','') # 排放标准
    #         car_price = each.xpath("./span[@class='guidance-price']/em/a/text()").extract()[0].replace(' ','').replace('\xa0','') # 价格
    #
    #         item['car_name'] = car_name
    #         item['car_drive'] = car_drive
    #         item['car_engine'] = car_engine
    #         item['car_horsepower'] = car_horsepower
    #         item['car_emission'] = car_emission
    #         item['car_price'] = car_price
    #         print(item)
    #         yield item







    # def parse(self, response):
    #     for link in self.link_extractor['page_one'].extract_links(response):
    #         yield scrapy.Request(url=link.url, callback=self.handle)
    # //div[@id='tractor_price']/ul/li/div[@class='content']/div[@class='caption']/h2/a/text()
    def handle(self, response):
        for each in response.xpath("//div[@class='content']/ul/li/div[@class='content']"):
            # 车名
            car_name = each.xpath("./div[@class='caption']/h2/a/text()").extract()[0]
            # 驱动形式
            drive_type = each.xpath("./div[@class='config']/p[1]/a/text()").extract()[0]
            print(car_name)
            print(drive_type)
        # for each in self.link_extractor['page_two'].extract_links(response):
        #     #print(each.url)
        #     yield scrapy.Request(url=each.url, callback=self.handle)

    # def handle(self, response):
    #     for url in self.link_extractor['page_three'].extract_links(response):
    #         yield scrapy.Request(url=url.url, callback=self.result)

    # def result(self, response):
    #     item = KczjItem()
    #     print(response.url)
    #
    #     # 汽车名称
    #     car_name = response.xpath("//div[@class='parameter-detail']/table/thead/tr/th/div/h5/a/text()").extract()
    #     # 汽车价格
    #     # .replace('\r','').replace('\n','').replace('\t','')
    #     car_price = response.xpath("//div[@class='parameter-detail']/table/thead/tr[2]/td[text()!='厂商指导价：']/text()").extract()
    #     # 驱动形式
    #     car_power = response.xpath("//tbody/tr[3]/td/div/text()")
    #     # 轴距
    #     # .replace('\r','').replace('\n','').replace('\t','')
    #     car_wheelbase = response.xpath("//tbody/tr[4]/td/div/text()").extract()
    #     # 发动机
    #     # .replace('\r','').replace('\n','').replace('\t','')
    #     car_engine = response.xpath("//tbody/tr[5]/td/div/text()").extract()
    #     # 变速箱
    #     # .replace('\r','').replace('\n','').replace('\t','')
    #     car_gearbox = response.xpath("//tbody/tr[6]/td/div/text()").extract()
    #     # 后桥速比
    #     # .replace('\r','').replace('\n','').replace('\t','')
    #     car_ratio = response.xpath("//tbody/tr[7]/td/div/text()").extract()
    #     # 车身长度
    #     # .replace('\r','').replace('\n','').replace('\t','')
    #     car_long = response.xpath("//tbody/tr[8]/td/div/text()").extract()
    #     # 车身宽度
    #     # .replace('\r','').replace('\n','').replace('\t','')
    #     car_width = response.xpath("//tbody/tr[9]/td/div/text()").extract()
    #     # 车身高度
    #     # .replace('\r','').replace('\n','').replace('\t','')
    #     car_height = response.xpath("//tbody/tr[10]/td/div/text()").extract()
    #     # 轮距
    #     # .replace('\r', '').replace('\n', '').replace('\t', '')
    #     car_track = response.xpath("//tbody/tr[11]/td/div/text()").extract()
    #     # 整车重量
    #     # .replace('\r','').replace('\n','').replace('\t','')
    #     car_weight = response.xpath("//tbody/tr[12]/td/div/text()").extract()
    #     # 总重量
    #     # .replace('\r','').replace('\n','').replace('\t','')
    #     total_weight = response.xpath("//tbody/tr[13]/td/div/text()").extract()
    #     # 牵引总重量
    #     # .replace('\r','').replace('\n','').replace('\t','')
    #     traction_total_weight = response.xpath("//tbody/tr[14]/td/div/text()").extract()
    #     # 最高车速
    #     # .replace('\r','').replace('\n','').replace('\t','')
    #     max_speed = response.xpath("//tbody/tr[15]/td/div/text()").extract()
    #     # 最小转弯直径
    #     # .replace('\r','').replace('\n','').replace('\t','')
    #     min_turn_diameter = response.xpath("//tbody/tr[15]/td/div/text()").extract()














            # if len(car_name) > 0:
            #     item['car_name'] = car_name[0]
            # else:
            #     item['car_name'] = 'None'

            # 价格

            # if len(car_price) > 0:
            #     item['car_price'] = car_price[0].replace('\r','').replace('\n','').replace('\t','')
            # else:
            #     item['car_price'] = 'None'

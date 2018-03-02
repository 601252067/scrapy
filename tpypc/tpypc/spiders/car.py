# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
# from scrapy.http import HtmlResponse

from tpypc.items import TpypcItem

# 导入SplashRequest
# from scrapy_splash import SplashRequest

# from selenium import webdriver
# from scrapy.xlib.pydispatch import dispatcher
# from scrapy import signals
#  from pydispatch import dispatcher

class CarSpider(CrawlSpider):
    name = 'car'
    allowed_domains = ['price.pcauto.com.cn']
    start_urls = ['http://price.pcauto.com.cn/cars/']

    # rules = (
    #     Rule(LinkExtractor(allow=r'price.pcauto.com.cn/sg\d+/$'), follow=True),
    # )

    link_extractor = {
        'follow_url': LinkExtractor(allow=r'price.pcauto.com.cn/sg\d+/$'),
        # 'content': LinkExtractor(allow='bbscon,board,\w+,file,M\.\d+\.A\.html$'),
    }

    # def __init__(self):
    #     self.brower = webdriver.PhantomJS(executable_path='D:/phantomjs/bin/phantomjs.exe')
    #     super(CarSpider, self).__init__()
    #     # 绑定信号量，当spider关闭时调用我们的函数
    #     # dispatcher.connect(self.spider_closed, signals.spider_closed)

    def parse(self, response):
        # 提取符合规则的链接,重新发送请求,让PhantomJS渲染页面
        for link in self.link_extractor['follow_url'].extract_links(response):
            yield scrapy.Request(url=link.url, callback=self.result_handdle)

    # 因为我写好了中间件,所有request由 JSPageMiddleware 中间件渲染,在此不体现
    # 从PhantomJS渲染过的页面中提取数据
    def result_handdle(self, response):
        print('---start---')
        link = response.url
        print(link)
        test = response.xpath("//div[@class='price']/p[2]/em[3]/a/text()").extract()
        if len(test) == 0:
            print('---N---')
        else:
            print(test[0])
        print("---end---")
        # file_name = './html/%s.html'%str(link).split('/')[3]
        # print('---write start---')
        # with open(file_name,'w+') as f:
        #     f.write(response.body)
        #     f.close()

        # print('---start file---')
        # file = open('./html/%s.html'%link,'wb')
        # file.write(data)
        # file.close()
        # print('---start end---')

    # 关闭浏览器
    # def spider_closed(self, spider):
    #     print('spider closed')
    #     self.brower.quit()

        # 获取加载后的页面
        # test = driver.find_element_by_xpath("//div[@class='price']/p[2]/em[3]/a/text()").extract()
        # if len(test) == 0:
        #    print('---N---')
        # else:
        #    print(test[0])

        # item = TpypcItem()
        #
        # car_name_list = response.xpath("//div[@class='title']/h1/text()").extract()
        # if len(car_name_list) > 0:
        #     car_name = car_name_list[0].split('-')[1]
        # else:
        #     car_name = 'None'
        #
        # car_price_list = response.xpath("//p[@class='p1']/em[1]/text()").extract()
        # if len(car_price_list) == 0:
        #     car_min_price = 'None'
        #     car_max_price = 'None'
        #     car_avg_price = 'None'
        #     car_output = 'None'
        #     car_lever = 'None'
        #     car_type = 'None'
        #     car_score = 'None'
        #
        #     print('---len=0---')
        # else:
        #     print('---is test---')
        #     test = response.xpath("//div[@class='price']/p[2]/em[3]/a/text()").extract()
        #     if len(test) == 0:
        #         print('---N---')
        #     else:
        #         print(test[0])
        #
        #
        #     car_output = response.xpath("//ul[@class='des']/li[1]/p[1]/em/a/text()").extract()[0]
        #     car_lever = response.xpath("//ul[@class='des']/li[1]/p[2]/a/text()").extract()[0]
        #     car_type = response.xpath("//ul[@class='des']/li[2]/p[2]/em/a[1]/text()").extract()[0]
        #     car_score = response.xpath("//div[@class='processBar-txt']/a/p/text()").extract()[0]
        #
        #     price_data = car_price_list[0].replace('万','').split('-')
        #     if len(price_data) == 1:
        #         car_min_price = float(price_data[0])
        #         car_max_price = float(price_data[0])
        #         car_avg_price = float(price_data[0])
        #     else:
        #         car_min_price = float(price_data[0])
        #         car_max_price = float(price_data[1])
        #         car_avg_price = (car_min_price + car_max_price) / 2
        #
        # item['car_name'] = car_name
        # item['car_min_price'] = car_min_price
        # item['car_max_price'] = car_max_price
        # item['car_avg_price'] = car_avg_price
        # item['car_output'] = car_output
        # item['car_lever'] = car_lever
        # item['car_type'] = car_type
        # item['car_score'] = car_score
        # yield item



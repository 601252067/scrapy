# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

# 这两个包是实现模拟登陆要用到的包
from scrapy import Request,FormRequest

class RRSpider(CrawlSpider):
    name = 'r_r'
    allowed_domains = ['renren.com']
    start_urls = ['http://renren.com/']

    rules = (
        Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    )


    # 构造登录页面请求
    def start_requests(self):
        # 以下列举了Request对象所需的参数和说明
        # url 就是需要请求，并进行下一步处理的url
        # callback 指定该请求返回的Response，由那个函数来处理
        # method 此参数定义请求类型(GET, POST, PUT, 等)
        # headers 请求时，包含的头文件。一般不需要(处理登录机制比较复杂的站点时使用headers)
        # meta 比较常用，在不同的请求之间传递数据使用的。字典dict型
        # encoding 使用默认的 'utf-8' 就行
        # dont_filter 表明该请求不由调度器过滤。这是当你想使用多次执行相同的请求,忽略重复的过滤器。默认为Fals
        # errback 指定错误处理函数
        return [Request("http://www.renren.com", callback=self.login_handle)]

    # 发送POSt登录请求
    def login_handle(self, response):
        return [FormRequest.from_response(
            response,
            formdata={"email":"13572449775", "password":"a601252067"},
            callback = self.after_login
        )]

    # 登录成功后执行的操作
    def after_login(self, response):
        with open("r.html", "wb") as f:
            f.write(response.body)

    def parse_item(self, response):
        pass
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()

# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from uu134.items import Uu134Item
from scrapy.selector import Selector



class DowmloadSpider(CrawlSpider):
    name = 'dowmload'
    allowed_domains = ['www.289aa.com']
    start_urls = ['https://www.134uu.com/htm/vodlist3/1.htm']

    rules = (
        Rule(LinkExtractor(allow=r'/htm/vodlist3/\d+.htm')),
        Rule(LinkExtractor(allow=r'/htm/vod3/\d+.htm'), follow=True, callback='test_handle'),
    )


    def test_handle(self, response):
        print(response.url)
        from selenium import webdriver
        from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
        profile = webdriver.FirefoxProfile()
        profile.set_preference('network.proxy.type',1)
        profile.set_preference('network.proxy.http', '127.0.0.1')
        profile.set_preference('network.proxy.http_port',1083)
        profile.set_preference('network.proxy.ssl', '127.0.0.1')
        profile.set_preference('network.proxy.ssl_port', 1083)
        profile.update_preferences()
        binary = FirefoxBinary('C:/Program Files/Mozilla Firefox/firefox.exe')
        browser = webdriver.Firefox(firefox_binary=binary)
        browser.get(response.url)
        data = Selector(browser.page_source)
        print(data)
        print('---end---')
    # link_extractor = {
    #     'one_lever_link': LinkExtractor(allow=r'/htm/vodlist3/\d+.htm'),
    #     'two_lever_link': LinkExtractor(allow=r'/htm/vod3/\d+.htm'),
    #     # 'content': LinkExtractor(allow='bbscon,board,\w+,file,M\.\d+\.A\.html$'),
    # }

    # def parse(self, response):
    #     for link in self.link_extractor['one_lever_link'].extract_links(response):
    #         yield scrapy.Request(url=link.url, callback=self.parse_page)
    #
    # def parse_page(self, response):
    #     for link in self.link_extractor['two_lever_link'].extract_links(response):
    #         yield scrapy.Request(url=link.url, callback=self.parse_page)
    #
    # def parse_handle(self, response):
    #         print(response.url)
            #print(link.url)
    # def parse_item(self, response):
    #     print("---start---")
    #     ua = random.choice(self.user_agent_list)  # 随机选择一个User-Agent
    #     dcap = dict(DesiredCapabilities.PHANTOMJS)  # 导入PhantomJS的设置
    #     dcap["phantomjs.page.settings.userAgent"] = (ua)  # 设置PhantomJS的随机User-Agent
    #     dcap["phantomjs.page.settings.loadImages"] = False  # 禁止加载图片
    #     browser = webdriver.PhantomJS(executable_path='D:/phantomjs/bin/phantomjs.exe', desired_capabilities=dcap)
    #
    #     browser.get(response.url)
    #     data = Selector(browser.page_source)
    #
    #     str_time = str(time.time())
    #     file_name = '%s.html'%str_time.split('.')[0]
    #     with open(file_name, 'w+') as f:
    #         f.write(data)
    #         f.close()
    #
    #
    #     name = data.xpath("//div[@id='main']/div[@class='container']/h3/text()").extract()
    #     if len(name) > 0:
    #         print(name[0])
    #     else:
    #         print('name null')
    #
    #     thunder = data.xpath("//div[@class='endpage clearfixpage']/div[2]/ul/div/a[1]/@href").extract()
    #     if len(thunder) > 0:
    #         print(thunder[0])
    #     else:
    #         print('thunder null')
    #
    #     print("---end---")

        #print(response.url)
        # item = Uu134Item()
        # name = response.xpath()
        # if len(name) > 0:
        #     item['name'] = name[0]
        #     print(item['name'])

    user_agent_list = [
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
        "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/531.21.8 (KHTML, like Gecko) Version/4.0.4 Safari/531.21.10",
        "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/533.17.8 (KHTML, like Gecko) Version/5.0.1 Safari/533.17.8",
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5",
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-GB; rv:1.9.1.17) Gecko/20110123 (like Firefox/3.x) SeaMonkey/2.0.12",
        "Mozilla/5.0 (Windows NT 5.2; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1",
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_8; en-US) AppleWebKit/532.8 (KHTML, like Gecko) Chrome/4.0.302.2 Safari/532.8",
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_4; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.464.0 Safari/534.3",
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_5; en-US) AppleWebKit/534.13 (KHTML, like Gecko) Chrome/9.0.597.15 Safari/534.13",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_2) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.186 Safari/535.1",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.54 Safari/535.2",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7",
        "Mozilla/5.0 (Macintosh; U; Mac OS X Mach-O; en-US; rv:2.0a) Gecko/20040614 Firefox/3.0.0 ",
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10.5; en-US; rv:1.9.0.3) Gecko/2008092414 Firefox/3.0.3",
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.5; en-US; rv:1.9.1) Gecko/20090624 Firefox/3.5",
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.6; en-US; rv:1.9.2.14) Gecko/20110218 AlexaToolbar/alxf-2.0 Firefox/3.6.14",
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10.5; en-US; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1"
    ]
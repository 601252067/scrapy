# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector

from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

class Aa289Spider(scrapy.Spider):
    name = 'aa289'
    allowed_domains = ['www.289aa.com']
    start_urls = ['https://www.289aa.com/htm/vod5/6018.htm']

    def parse(self, response):
        binary = FirefoxBinary('C:/Program Files/Mozilla Firefox/firefox.exe')
        browser = webdriver.Firefox(firefox_binary=binary)
        browser.get(response.url)

        print(browser.page_source)


# -*- coding: utf-8 -*-

import scrapy

class RentiItem(scrapy.Item):
    img_path = scrapy.Field()
    img_name = scrapy.Field()
    img_url = scrapy.Field()

# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class DgPipeline(object):
    def __init__(self):
        self.file = open('sun.txt', 'wb')

    def process_item(self, item, spider):
        text = str(item).encode("UTF-8") + b"\n"
        self.file.write(text)

    def close_spider(self, spider):
        self.file.close()
# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
class KczjPipeline(object):

    def __init__(self):
        # 连接数据库
        self.connect = pymysql.connect(
            host="127.0.0.1",
            port=3306,
            db="kczj",
            user="root",
            passwd="",
            charset="utf8",
            use_unicode=False,
        )
        # 通过cursor执行增删查改
        self.cursor = self.connect.cursor()


    def process_item(self, item, spider):
        try:
            # 插入数据
            sql = """INSERT INTO dealer_info(shop_name,shop_tag_1,shop_tag_2,shop_tag_3,shop_addr,shop_tel) VALUES(%s,%s,%s,%s,%s,%s)"""
            params = (item['shop_name'],item['shop_tag_1'],item['shop_tag_2'],item['shop_tag_3'],item['shop_addr'],item['shop_tel'])
            self.cursor.execute(sql, params)

            # 提交数据
            self.connect.commit()

        except Exception as error:
            # 错误处理
            print(error)

        return item


# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql

class QczjPipeline(object):

    def __init__(self):
        # 连接数据库
        self.connect = pymysql.connect(
            host="127.0.0.1",
            port=3306,
            db="spider_data",
            user="root",
            passwd="",
            charset="utf8",
            use_unicode=True,
        )
        # 通过cursor执行增删查改
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        try:
            # 插入数据
            sql = 'INSERT INTO qczj(car_name,car_min_price,car_max_price,car_avg_price,car_type,car_score) VALUES("%s","%s","%s","%s","%s","%s")'
            params = (
                item['car_name'].replace("'",""),
                item['car_min_price'].replace("'",""),
                item['car_max_price'].replace("'",""),
                item['car_avg_price'].replace("'",""),
                item['car_type'].replace("'",""),
                item['car_score'].replace("'","")
            )

            # 执行sql语句
            self.cursor.execute(sql, params)

            # 提交数据
            self.connect.commit()

        except Exception as error:
            # 错误处理
            print(error)

    def close_spider(self, spider):
        self.connect.close()
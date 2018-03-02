# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class TpypcPipeline(object):
    def __init__(self):
        # 连接数据库
        self.connect = pymysql.connect(
            host="127.0.0.1",
            port=3306,
            db="spider_data",
            user="root",
            passwd="",
            charset="utf8",
            use_unicode=False,
        )
        # 通过cursor执行增删查改
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        # print(item)
        # car_name = item['car_name'].strip("'")
        # car_min_price = item['car_min_price'].strip("'")
        # car_max_price = item['car_max_price'].strip("'")
        # car_avg_price = item['car_avg_price'].strip("'")
        # car_output = item['car_output'].strip("'")
        # car_lever = item['car_lever'].strip("'")
        # car_type = item['car_type'].strip("'")
        # car_score = item['car_score'].strip("'")

        try:
            # 插入数据
            # sql = "INSERT INTO tpyqc(car_name,car_min_price,car_max_price,car_avg_price,car_output,car_lever,car_type,car_score) \
            #        VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
            # params = (item['car_name'],item['car_min_price'],item['car_max_price'],item['car_avg_price'],item['car_output'],item['car_lever'],item['car_type'],item['car_score'])
            # 执行sql语句
            # self.cursor.execute(sql, params)

            sql = """INSERT INTO tpyqc(car_name,car_min_price,car_max_price,car_avg_price,car_output,car_lever,car_type,car_score) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"""
            params = (item['car_name'],item['car_min_price'],item['car_max_price'],item['car_avg_price'],item['car_output'],item['car_lever'],item['car_type'],item['car_score'])
            self.cursor.execute(sql, params)
            # self.cursor.execute("""
            #             INSERT INTO tpyqc(car_name,car_min_price,car_max_price,car_avg_price,car_output,car_lever,car_type,car_score) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)
            #             """, )

            # 提交数据
            self.connect.commit()

        except Exception as error:
            # 错误处理
            print(error)

        return item

    def close_spider(self, spider):
        self.connect.close()

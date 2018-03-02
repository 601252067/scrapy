# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


import pymysql

class DoubanPipeline(object):
    def __init__(self):
        # 链接数据库
        self.connect = pymysql.connect(
            host = "127.0.0.1",
            port = 3306,
            db = "dou_ban",
            user = "root",
            passwd = "",
            charset = "utf8",
            use_unicode = True,
        )

        # 通过cursor执行增删查改
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):

        try:
            # 插入数据
            sql = 'INSERT INTO movies_data(zh_title,en_title,ot_title,content,star,quote,top) VALUES("%s","%s","%s","%s","%s","%s","%s")'
            params = (item['zh_title'],item['en_title'],item['ot_title'],item['content'],item['star'],item['quote'],item['top'])

            # 执行sql语句
            self.cursor.execute(sql, params)

            # 提交数据
            self.connect.commit()

        except Exception as error:
            # 错误处理
            print(error)

        # return item

    def close_spider(self, spider):
        # 爬虫结束后,关闭数据库链接
        self.connect.close()
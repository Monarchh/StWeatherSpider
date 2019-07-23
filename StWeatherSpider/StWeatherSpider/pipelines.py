# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import mysql.connector

class StweatherspiderPipeline(object):
    # 定义构造器，初始化要写入的文件
    def __init__(self):
        self.conn = mysql.connector.connect(user = 'root', password = '85757770', host = 'localhost',
            port = '3306', database = 'python', use_unicode = True)
        self.cur = self.conn.cursor()
    # 重写close_spider回调方法，用于关闭数据库资源
    def close_spider(self, spider):
        print("--------关闭资源--------")
        # 关闭游标
        self.cur.close()
        # 关闭连接
        self.conn.close()
    def process_item(self, item, spider):
        self.cur.execute("INSERT INTO stweather VALUES(null, %s, %s, %s, %s)",(item['date'], item['weather'],
            item['temp'], item['wind']))
        self.conn.commit()

# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class StweatherspiderItem(scrapy.Item):
    # 日期
    date = scrapy.Field()
    # 天气状况
    weather = scrapy.Field()
    # 气温
    temp = scrapy.Field()
    # 风力风向
    wind = scrapy.Field()

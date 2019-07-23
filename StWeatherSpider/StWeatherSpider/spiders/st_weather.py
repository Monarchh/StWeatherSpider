# -*- coding: utf-8 -*-
import scrapy
from StWeatherSpider.items import StweatherspiderItem

class StWeatherSpider(scrapy.Spider):
    name = 'st_weather'
    allowed_domains = ['tianqihoubao.com']
    start_urls = ['http://www.tianqihoubao.com/lishi/shantou/month/201101.html']

    def parse(self, response):
        xx = response.xpath('//table[@class="b"]/tr')       
        for tr in xx:
            item = StweatherspiderItem()
            # 由于里面的数据放在一个表格里，tr都是长得一样，所以标题栏用if语句过滤掉避免抓取到无用数据
            if tr.xpath('./td[1]/b/text()').extract_first() == "日期":
                pass
            else:
                item['date'] = tr.xpath('normalize-space(./td[1]/a/text())').extract_first()
                item['weather'] = tr.xpath('normalize-space(./td[2]/text())').extract_first()
                item['temp'] = tr.xpath('normalize-space(./td[3]/text())').extract_first()
                item['wind'] = tr.xpath('normalize-space(./td[4]/text())').extract_first()
                yield item
            new_links = response.xpath('//p/a[2]/@href').extract()
            if new_links and len(new_links) > 0:
                new_link = new_links[0]
                yield scrapy.Request("http://www.tianqihoubao.com" + new_link, callback=self.parse)

# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
import re
from ..items import Shixun1Item
class Dayinhu(CrawlSpider):
    name = "dayinhu"
    allowed_domains =[]
    start_urls =[
        "http://www.dayinhu.com/news/category/%E7%A7%91%E6%8A%80%E5%89%8D%E6%B2%BF"
    ]
    # rules = (
    #     Rule(LinkExtractor(allow='http://www.dayinhu.com/news/category/%E7%A7%91%E6%8A%80%E5%89%8D%E6%B2%BF/page/\d+'),follow=True),
    #     Rule(LinkExtractor(allow='http://www.dayinhu.com/news/\d{6}\.html'),callback='parse',follow=False)
    #
    # )
    rules = (
        Rule(LinkExtractor(allow='http://www.dayinhu.com/news/category/%E7%A7%91%E6%8A%80%E5%89%8D%E6%B2%BF/page/\d+',),follow=True),
        Rule(LinkExtractor(allow='http://www.dayinhu.com/news/\d{6}\.html'), callback='parse_item', follow=False)
    )
    def parse_item(self, response):
        sel=Selector(response)
        # 标题
        if sel.xpath("//h1[@class='entry-title']/text()").extract():
            title=sel.xpath("//h1[@class='entry-title']/text()").extract()
            # print(title)
        else:
            raise Exception('title is null')
        # 时间
        if sel.xpath("//a[1]/time[@class='entry-date']/text()").extract():
            time=sel.xpath("//a[1]/time[@class='entry-date']/text()").extract()
            # print(time)
        else:
            raise Exception('time is null')
        # 正文
        if sel.xpath("//div[@class='entry-content']/p/text()").extract():
            content=sel.xpath("//div[@class='entry-content']/p/text()").extract()
            # print(content)
        else:
            raise Exception('content is null')
        # 关键字
        if sel.xpath('//meta[@name="keywords"]/@content').extract():
            key=sel.xpath('//meta[@name="keywords"]/@content').extract()
            # print(key)
        else:
            key=''
            # 图片
            html=response.txt
            img=re.compile('img src="(.*?)"',re.S)
            img_er=re.findall(img,html)
            img_urll = img_er[1:]
        #     导读
        if sel.xpath('//*[@id="post-101816"]/footer/a[2]/text()').extract():
            laiyuan=sel.xpath('//*[@id="post-101816"]/footer/a[2]/text()').extract()
            print(laiyuan)
        else:
            laiyuan=''


        # items=Shixun1Item()
        #         # items['title']=title
        #         # items['time']=time
        #         # items['content']=title
        #         # items['key']=key
        #         # return items


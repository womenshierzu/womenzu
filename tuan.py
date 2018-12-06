# -*- coding: utf-8 -*-
import scrapy
import json
from ..items import MeituanItem
class TuanSpider(scrapy.Spider):
    name = 'tuan'
    # allowed_domains = ['l']
    # start_urls = ['https://apimobile.meituan.com/group/v4/poi/pcsearch/1?uuid=65e433033ea047f1be4a.1544077560.1.0.0&userid=-1&limit=32&offset=32&cateId=-1&q=%E7%BE%8E%E9%A3%9F']
    def start_requests(self):
        for i in range(1,320):
            url = 'https://apimobile.meituan.com/group/v4/poi/pcsearch/1?uuid=65e433033ea047f1be4a.1544077560.1.0.0&userid=-1&limit=32&offset='+str(i)+'&cateId=-1&q=%E7%BE%8E%E9%A3%9F'
            yield scrapy.Request(url,self.parse)
    def parse(self, response):
        data = json.loads(response.text).get('data').get('searchResult')
        for i in data:
            name = i.get('title')
            print(name)
            city = i.get('city')
            print(city)
            leibie = i.get('backCateName')
            print(leibie)
            dizhi = i.get('address')
            print(dizhi)
            pingfen = i.get('avgscore')
            print(pingfen)
            pinglunrenshu = i.get('comments')
            print(pinglunrenshu)
            id = i.get('id')
            print(id)
            item = MeituanItem()
            item['name'] = name
            item['city'] = city
            item['leibie'] = leibie
            item['dizhi'] = dizhi
            item['pingfen'] = pingfen
            item['pinglunrenshu'] = pinglunrenshu
            item['id'] = id
            return item

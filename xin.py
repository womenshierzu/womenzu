# -*- coding: utf-8 -*-
import scrapy,json
import re
import execjs
import time


class XinSpider(scrapy.Spider):
    name = 'xin'
    # allowed_domains = ['www.qx.com']
    start_urls = ['https://xin.baidu.com/s/l?q=%E5%B0%8F%E7%B1%B3&t=0&p=2&s=10&o=0&f=undefined&_=1544060901875']

    def parse(self, response):
        data = json.loads(response.text).get('data').get('resultList')
        for d in data:
            # entName = d['entName']
            # validityFrom = d['validityFrom']
            # legalPerson = d['legalPerson']
            # entType = d['entType']
            # openStatus = d['openStatus']
            # titleDomicile = d['titleDomicile']
            pid = d['pid']
        #     print(
        #         '企业名称：'+entName,
        #         '法定代表人：'+legalPerson,
        #         '成立时间：'+validityFrom,
        #         '企业类型：'+entType,
        #         '营业状态：'+openStatus,
        #         '企业地址：'+titleDomicile,
        #     )
        #     print(pid)
            url1 = "https://xin.baidu.com/detail/compinfo?pid="+pid
            yield scrapy.Request(url=url1,callback=self.parse1)
    def parse1(self,response):
        d = response.xpath('//*[@id="baiducode"]/text()').extract()[0]
        pid = eval(re.findall(r'"pid":(.*?)\,.*?"defTags"', response.text, re.S)[0])
        # print(pid)
        id1, att = re.findall(r"document\.getElementById\('(.*?)'\)\.getAttribute\('(.*?)'\)", response.text)[0]
        func = "function mix(" + re.findall(r'mix\((.*?)\(function', response.text, re.S)[0]
        # print(func)
        tk = re.findall(att + r'="(.*?)"\>', response.text)[0]
        # print(tk)
        tk1 = execjs.compile(func).call('mix', tk, d)
        # print(tk1)
        time1 = int(time.time() * 1000)
        url1 = "https://xin.baidu.com/detail/basicAjax?pid={}&tot={}&_={}".format(pid, tk1, time1)
        # print(url1)
        yield scrapy.Request(url1, self.qiye)
    def qiye(self, response):
        # print(response.text)
        # data = json.loads(response.text)['data']['entName']
        data = json.loads(response.text)['data']
        # print(data)
        name = data['entName']
        print(name)
        entType = data['entType']
        print(entType)
        scope = data['scope']
        print(scope)
        regAddr = data['regAddr']
        print(regAddr)
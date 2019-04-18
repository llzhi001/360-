# -*- coding: utf-8 -*-
import scrapy

import re
import json
class CrawlTestSpider(scrapy.Spider):
    name = 'crawl_test'
    allowed_domains = ['qq.com']
    start_urls = ['https://pacaio.match.qq.com/vlike/categories?callback=__jp2']
    siteRightArr = ['digi', 'finance', 'ent', 'sports', 'milite', 'world', 'tech', 'auto', 'fashion', 'games', 'house', 'cul', 'finance_stock', 'emotion', 'health', 'visit', 'food', 'baby', 'pet', 'history', 'society', 'kepu', 'edu', 'photo', 'comic','fx','cul_daoism','cul_ru','finance_licai', 'astro']
    cidData = ['2270554809', '2293392683'];
    #page = [500]
    def parse(self, response):
        response = response.text
        print(response)
        details_url = re.findall(r'__jp2\((.*?)\)',response)
        dict_data = json.loads(details_url[0])['data']
        # print(dict_data)
        for i in dict_data:
            print(i)

        # print('12')
        # pass

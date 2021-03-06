# -*- coding: utf-8 -*-
# 企查查，信息捞取
from scrapy.spiders import Spider

import scrapy

from MoonSpider.items import QiccSpiderItem, QiccSpiderList
from selenium import webdriver
import pandas as pd
import time


class QiccSpider(Spider):
    name = "qicc"
    domain_name = "https://www.qichacha.com"
    allowed_domains = ['www.qichacha.com']
    start_urls = ["https://www.qichacha.com/search_index?key=%E9%A9%AC%E4%BA%91&ajaxflag=1&p=1&"]
    key = "福建"

    def __init__(self):
        # 定义保存登录成功之后的cookie的变量
        self.login_cookies = []

    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip,deflate",
        "Accept-Language": "en-US,en;q=0.8,zh-TW;q=0.6,zh;q=0.4",
        "Connection": "keep-alive",
        "Content-Type": " application/x-www-form-urlencoded; charset=UTF-8",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36",
        "Referer": "https://www.qichacha.com"
    }

    search_key = pd.read_csv("D:/code/MoonSpider/MoonSpider/spiders/qicc/key.csv")

    def get_cookies(self):
        browser = webdriver.Chrome(executable_path="D:/code/MoonSpider/drivers/chromedriver.exe")
        browser.get("https://www.qichacha.com/")
        self.login_cookies = browser.get_cookies()
        browser.close()

    def start_requests(self):
        self.get_cookies()
        # 开始访问登录后的内容
        return [scrapy.Request(self.start_urls[0],
                               headers=self.headers,
                               cookies=self.login_cookies,
                               callback=self.parse)]

    def parse(self, response):

        url = response.request.url
        if url.endswith("&"):
            # 查询列表清单
            page = int(url[-2:-1])
            results = response.xpath('//tbody[@id="search-result"]//a[@class="ma_h1"]')
            vipr = response.xpath('//div[@id="cxjg2VipInsert"]')

            for item in results:
                abs_route = item.xpath("@href").extract_first().strip()
                content_url = self.domain_name + abs_route
                yield scrapy.Request(content_url, headers=self.headers,
                                     cookies=self.login_cookies, callback=self.content_parse)

            # if page <= 3:
            #     next_page = url[:-2] + str(page + 1) + "&"
            #     yield scrapy.Request(next_page)

            i = 0
            for key in self.search_key.values:
                if i < 2000:
                    i += 1
                else:
                    break
                print(key)
                yield scrapy.Request("https://www.qichacha.com/search_index?key=" + key[0] + "&ajaxflag=1&p=1&",
                                     headers=self.headers,
                                     cookies=self.login_cookies,
                                     callback=self.list_parse)

    def list_parse(self, response):
        results = response.xpath('//tbody[@id="search-result"]//a[@class="ma_h1"]')
        if results.extract_first() is None:
            self.get_cookies()
            return None
        vipr = response.xpath('//div[@id="cxjg2VipInsert"]')
        print(response.request.url)
        for item in results:
            abs_route = item.xpath("@href").extract_first().strip()
            content_url = self.domain_name + abs_route
            yield scrapy.Request(content_url, callback=self.content_parse)

    def content_parse(self, response):
        finds = response.xpath('//div[@class="content"]//h1/text()').extract_first()
        if finds is None:
            self.get_cookies()
            return None
        cp_name = finds.strip()
        social_credict = response.xpath('//table[@class="ntable"]//tr[4]/td[2]/text()').extract_first().strip()
        # type = response.xpath('//table[@class="ntable"]//tr[4]/td[1]/text()').extract_first().strip()
        # 统一社会信用代码
        url = response.request.url
        print(url)


        qicc_item = QiccSpiderItem()
        qicc_item['social_credit'] = social_credict
        qicc_item['company_name'] = cp_name
        qicc_item['article'] = response.text
        qicc_item['url'] = url
        return qicc_item

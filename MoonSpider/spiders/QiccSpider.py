# -*- coding: utf-8 -*-
# 企查查，信息捞取
from scrapy.spiders import Spider

import scrapy

from MoonSpider.items import QiccSpiderItem, QiccSpiderList


class QiccSpider(Spider):
    name = "qicc"
    domain_name = "https://www.qichacha.com"
    allowed_domains = ['www.qichacha.com']
    start_urls = ["https://www.qichacha.com/search_index?key=%E9%A9%AC%E4%BA%91&ajaxflag=1&p=1&"]
    key = "福建"

    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip,deflate",
        "Accept-Language": "en-US,en;q=0.8,zh-TW;q=0.6,zh;q=0.4",
        "Connection": "keep-alive",
        "Content-Type": " application/x-www-form-urlencoded; charset=UTF-8",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36",
        "Referer": "https://www.qichacha.com"
    }

    search_key = [ "广西", "赵", "钱", "孙", "李", "周", "物", "计"]

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
                yield scrapy.Request(content_url, callback=self.content_parse)

            # if page <= 3:
            #     next_page = url[:-2] + str(page + 1) + "&"
            #     yield scrapy.Request(next_page)

            for key in self.search_key:
                print(key)
                yield scrapy.Request("https://www.qichacha.com/search_index?key=" + key + "&ajaxflag=1&p=1&",
                                     callback=self.list_parse)

    def list_parse(self, response):
        results = response.xpath('//tbody[@id="search-result"]//a[@class="ma_h1"]')
        vipr = response.xpath('//div[@id="cxjg2VipInsert"]')
        for item in results:
            abs_route = item.xpath("@href").extract_first().strip()
            content_url = self.domain_name + abs_route
            yield scrapy.Request(content_url, callback=self.content_parse)

    def content_parse(self, response):
        cp_name = response.xpath('//div[@class="content"]//h1/text()').extract_first().strip()
        social_credict = response.xpath('//table[@class="ntable"]//tr[4]/td[2]/text()').extract_first().strip()
        # type = response.xpath('//table[@class="ntable"]//tr[4]/td[1]/text()').extract_first().strip()
        # 统一社会信用代码
        url = response.request.url
        qicc_item = QiccSpiderItem()
        qicc_item['social_credit'] = social_credict
        qicc_item['company_name'] = cp_name
        qicc_item['article'] = response.text
        qicc_item['url'] = url
        return qicc_item

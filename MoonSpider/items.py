# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field


class MoonspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class ArticleSpiderItem(scrapy.Item):
    title = Field()
    link = Field()
    recent = Field()
    article = Field()
    domain = Field()
    code = Field()
    article_order = Field()


class ArticleSpiderMainItem(scrapy.Item):
    link = Field()
    article = Field()
    code = Field()


# -*- coding: utf-8 -*-
class QiccSpiderItem(scrapy.Item):
    company_name = Field()
    # 统一社会信用代码
    social_credit = Field()
    # article = Field()
    url = Field()


class QiccSpiderList(scrapy.Item):
    keyword = Field()
    page = Field()


class ZhihuItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = Field()  # 保存抓取问题的url
    title = Field()  # 抓取问题的标题
    description = Field()  # 抓取问题的描述
    answer = Field()  # 抓取问题的答案
    name = Field()  # 个人用户的名称

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


class ZhihuItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = Field()  # 保存抓取问题的url
    title = Field()  # 抓取问题的标题
    description = Field()  # 抓取问题的描述
    answer = Field()  # 抓取问题的答案
    name = Field()  # 个人用户的名称

# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient

from MoonSpider.items import ArticleSpiderItem, ArticleSpiderMainItem


class MoonspiderPipeline(object):
    def process_item(self, item, spider):
        return item


class ArticleSpiderPipeline(object):
    client = MongoClient('localhost', 27017)
    db = client.article
    collection = db.article

    def __init__(self):
        self.fp = None

    def open_spider(self, spider):
        self.collection.remove()
        print('爬虫开始')

    def process_item(self, item, spider):
        if isinstance(item, ArticleSpiderItem):
            article = {
                'title': item['title'],
                'link': item['link'],
                'recent': item['recent'],
                'article': item['article'],
                'domain': item['domain'],
                'code': item['code']
            }
            self.collection.insert(article)
        return item

    def close_spider(self, spider):
        print('爬虫结束')


class ArticleSpiderMainPipeline(object):
    client = MongoClient('localhost', 27017)
    db = client.article
    collection = db.article

    def open_spider(self, spider):
        print('存储文章内容')

    def process_item(self, item, spider):
        if isinstance(item, ArticleSpiderMainItem):
            my_query = {'link': item['link'], 'code': item['code']}
            update_query = {"$set": {'article': item['article']}}
            self.collection.update_one(my_query, update_query)

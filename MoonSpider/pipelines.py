# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class MoonspiderPipeline(object):
    def process_item(self, item, spider):
        return item


class ArticleSpiderPipeline(object):
    def __init__(self):
        self.fp = None

    def open_spider(self, spider):
        print('爬虫开始')

    def process_item(self, item, spider):
        print(item['title'])
        print(item['link'])
        return item

    def close_spider(self, spider):
        print('爬虫结束')

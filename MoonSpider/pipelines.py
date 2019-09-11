# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


from MoonSpider.items import ArticleSpiderItem, ArticleSpiderMainItem, QiccSpiderItem
from MoonSpider.utils2.DbUtils import DbUtils


class MoonspiderPipeline(object):
    def process_item(self, item, spider):
        return item


class ArticleSpiderPipeline(object):
    dbUtil = DbUtils()

    def __init__(self):
        self.fp = None

    def open_spider(self, spider):
        self.dbUtil.remove()
        print('爬虫开始')

    def process_item(self, item, spider):
        if isinstance(item, ArticleSpiderItem):
            article = {
                'title': item['title'],
                'link': item['link'],
                'recent': item['recent'],
                'article': item['article'],
                'domain': item['domain'],
                'code': item['code'],
                'article_order': item['article_order']
            }
            self.dbUtil.insert(article)
        return item

    def close_spider(self, spider):
        print('爬虫结束')


class ArticleSpiderMainPipeline(object):
    dbUtil = DbUtils()

    def process_item(self, item, spider):
        if isinstance(item, ArticleSpiderMainItem):
            print('存储文章内容')
            my_query = {'link': item['link'], 'code': item['code']}
            update_query = {"$set": {'article': item['article']}}
            self.dbUtil.update_one(my_query, update_query)


class QiccSpiderPipeline(object):
    dbUtil = DbUtils()

    def process_item(self, item, spider):
        if isinstance(item, QiccSpiderItem):
            content = {
                'social_credit': item['social_credit'],
                'company_name': item['company_name'],
                'article': item['company_name'],
                'url': item['url']
            }
            self.dbUtil.insert(content)

        return item

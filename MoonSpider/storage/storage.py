# -*- coding: utf-8 -*-
from pymongo import MongoClient


class MongoStorage:

    def __init__(self):
        self.client = MongoClient('localhost', 27017)
        self.db = self.client.article
        self.collection = self.db.article

    def __del__(self):
        self.client.close()

    def insert(self, article):
        self.collection.insert(article)

    def update_one(self, old_query, new_query):
        self.collection.update_one(old_query, new_query)

    def remove(self):
        self.collection.remove()

    def get_recent_article(self, article_code):
        recents = self.db.article.find({'code': article_code}, {'code': 1, 'article_order': 1}).sort(
            'article_order', 1).limit(1)
        for recent in recents:
            return recent
        return {'code': article_code, 'article_order': 0}


# class SqliteStorage:
#     def __init__(self):
#         import sqlite3
#         self.conn = sqlite3.connect("article.db")
#         c = self.conn.cursor()
#         # 'title': item['title'],
#         # 'link': item['link'],
#         # 'recent': item['recent'],
#         # 'article': item['article'],
#         # 'domain': item['domain'],
#         # 'code': item['code'],
#         # 'article_order': item['article_order']
#         c.execute('''CREATE TABLE ARTICLE(
#             title TEXT,
#             link TEXT,
#             recent TEXT,
#             article TEXT,
#             domain TEXT,
#             code TEXT,
#             article_order: TEXT
#         );
#         ''')
#         self.conn.commit()
#
#     def __del__(self):
#         self.conn.close()
#
#     def insert(self, article):
#         self.collection.insert(article)

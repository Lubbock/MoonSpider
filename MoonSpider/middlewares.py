# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import random


class MoonspiderSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class MoonspiderDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class UserAgentDownloadMiddleware(object):
    '''
    下载器中间件
    在发送下载之前要设置请求头
    '''

    def process_request(self, request, spider):
        request.headers["Accept"] = "*/*"
        request.headers["Content-Encoding"]="gzip"
        request.headers["Content-Type"] = "text/html; charset=utf-8"
        request.headers["AX-Powered-By"] = "ThinkPHP"
        request.headers["Connection"] = "keep-alive"
        request.headers["User-Agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36",
        request.headers["Referer"] = "https://www.qichacha.com"
        request.headers["Server"]="Tengine"
        request.headers["EagleId"]="3da0cc9715680913403183308e"
        request.headers["Cookie"]="QCCSESSID=2phqjqj4l870foh7a003dcmnb0; zg_did=%7B%22did%22%3A%20%2216d18ea7aada-0169a7c8fa2605-38637501-fa000-16d18ea7aaeabf%22%7D; UM_distinctid=16d18ea7aee38c-02ef9746773af5-38637501-fa000-16d18ea7aef9f6; hasShow=1; _uab_collina=156808108344687547962534; acw_tc=3da0cca115680810835895588e781c6e508c0a13085ac1d2cf30e2dc24; Hm_lvt_3456bee468c83cc63fb5147f119f1075=1568081097,1568081192,1568081201,1568084051; CNZZDATA1254842228=1159836850-1568077011-https%253A%252F%252Fcn.bing.com%252F%7C1568090293; Hm_lpvt_3456bee468c83cc63fb5147f119f1075=1568093303; zg_de1d1a35bfa24ce29bbf2c7eb17e6c4f=%7B%22sid%22%3A%201568091338446%2C%22updated%22%3A%201568093303376%2C%22info%22%3A%201568081083078%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22%22%2C%22cuid%22%3A%20%2212578f23f4256cf19694919fa5e053f0%22%2C%22zs%22%3A%200%2C%22sc%22%3A%200%7D"
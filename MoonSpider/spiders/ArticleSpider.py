from scrapy.spiders import Spider

class ArticleSpider(Spider):
    name = "article_robot"
    start_urls = ["https://www.biqiuge.com/book/4772/"]

    def parse(self, response):
        titles = response.xpath('//div[@class="listmain"]/text()"]').extract()
        for title in titles:
            print(title.strip())

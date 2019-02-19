from scrapy.spiders import Spider

from MoonSpider.items import ArticleSpiderItem


class ArticleSpider(Spider):
    name = "article_robot"
    start_urls = ["https://www.biqiuge.com/book/4772/"]
    domain_name = "https://www.biqiuge.com"

    def parse(self, response):
        items = []
        recentArticles = response.xpath('//div[@class="listmain"]/dl/dd[position()<=6]/a')
        allArticles = response.xpath('//div[@class="listmain"]/dl/dd[position()>6]/a')
        self.extract_item(items, recentArticles)
        self.extract_item(items, allArticles)
        return items

    def extract_item(self, items, articles):
        for title in articles:
            item = ArticleSpiderItem()
            item['title'] = title.xpath("text()").extract()
            item['link'] = self.domain_name + title.xpath("@href").extract()[0]
            item['recent'] = True
            items.append(item)

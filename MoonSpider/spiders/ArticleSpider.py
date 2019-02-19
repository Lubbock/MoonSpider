from scrapy.spiders import Spider

from MoonSpider.items import ArticleSpiderItem


class ArticleSpider(Spider):
    name = "article_robot"
    start_urls = ["https://www.biqiuge.com/book/4772/"]
    domain_name = "https://www.biqiuge.com"

    def parse(self, response):
        items = []
        recentArticles = response.xpath('//div[@class="listmain"]/dl/dd[position()<6]/a')
        allArticles = response.xpath('//div[@class="listmain"]/dl/dd[position()>6]/a')
        self.extract_item(items, recentArticles, True)
        self.extract_item(items, allArticles, False)
        return items

    def extract_item(self, items, articles, recent):
        for title in articles:
            item = ArticleSpiderItem()
            item['title'] = title.xpath("text()").extract()[0].strip()
            item['link'] = title.xpath("@href").extract()[0].strip()
            item['recent'] = recent
            item['domain'] = self.domain_name
            item['article'] = ""
            items.append(item)

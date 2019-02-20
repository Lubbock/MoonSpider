from scrapy.spiders import Spider

from MoonSpider.items import ArticleSpiderItem


class ArticleSpider(Spider):
    name = "article_robot"
    start_urls = ["https://www.biqiuge.com/book/4772/"]
    domain_name = "https://www.biqiuge.com"
    allowed_domains = ['www.biqiuge.com']

    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip,deflate",
        "Accept-Language": "en-US,en;q=0.8,zh-TW;q=0.6,zh;q=0.4",
        "Connection": "keep-alive",
        "Content-Type": " application/x-www-form-urlencoded; charset=UTF-8",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36",
        "Referer": "https://www.biqiuge.com"
    }

    def parse(self, response):
        items = []
        recent_articles = response.xpath('//div[@class="listmain"]/dl/dd[position()<6]/a')
        all_articles = response.xpath('//div[@class="listmain"]/dl/dd[position()>6]/a')
        self.extract_item(items, recent_articles, True)
        self.extract_item(items, all_articles)
        return items

    def extract_item(self, items, articles, recent=False):
        for title in articles:
            item = ArticleSpiderItem()
            item['title'] = title.xpath("text()").extract()[0].strip()
            item['link'] = title.xpath("@href").extract()[0].strip()
            item['recent'] = recent
            item['domain'] = self.domain_name
            item['article'] = ""
            items.append(item)

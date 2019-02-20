from scrapy.spiders import Spider
import scrapy

from MoonSpider.items import ArticleSpiderItem, ArticleSpiderMainItem


class ArticleSpider(Spider):
    name = "article_robot"
    start_urls = ["https://www.biqiuge.com/book/4772/"]
    domain_name = "https://www.biqiuge.com"
    allowed_domains = ['www.biqiuge.com']
    article_code = 4772

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
        articles = response.xpath('//div[@class="listmain"]/dl/dd/a')
        # all_articles = response.xpath('//div[@class="listmain"]/dl/dd[position()>6]/a')
        i = 0
        links = []
        for title in articles:
            item = ArticleSpiderItem()
            item['title'] = title.xpath("text()").extract_first().strip()
            item['link'] = title.xpath("@href").extract_first().strip()
            item['recent'] = True if i < 6 else False
            item['domain'] = self.domain_name
            item['article'] = ""
            item['code'] = self.article_code
            i += 1
            links.append(item['link'])
            yield item
        temps = [links[0]]
        for link in temps:
            next_page = response.urljoin(link)
            yield scrapy.Request(next_page, callback=self.article_parse)

    def article_parse(self, response):
        item = ArticleSpiderMainItem()
        item['link'] = response.url[len(self.domain_name):]
        article = response.xpath('//div[@class="showtxt"]').xpath('string(.)').extract_first()
        item['article'] = article
        item['code'] = self.article_code
        return item
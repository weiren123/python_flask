import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = {
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/'
        }
        for url in urls:
            scrapy.Request(url=url,callback=self.parse)
    def parse(self, response):
        print(response)
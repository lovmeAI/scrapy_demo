import scrapy
from scrapy.http import HtmlResponse
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule
from scrapy_redis.spiders import RedisCrawlSpider


class AmazonSpider(RedisCrawlSpider):
    name = 'amazon'
    allowed_domains = ['amazon.cn']
    # start_urls = ['https://www.amazon.cn/gp/book/all_category/ref=sv_b_0']
    redis_key = 'amazon'

    rules = (
        Rule(LinkExtractor(restrict_xpaths='//td/a[@class="a-link-nav-icon"]'), follow=True),
        Rule(LinkExtractor(restrict_xpaths='//div[@class="a-section a-spacing-none a-spacing-top-small"]/a'), callback='parse_book_item'),
    )

    def parse_book_item(self, response: HtmlResponse):
        item = {
            'book_price':  response.xpath('//span[@id="kindle-price"]/text()').get().replace('\n', ''),
            'book_title':  response.xpath("//span[@id='productTitle']/text()").get().replace('\n', ''),
            'book_author': ''.join(response.xpath("//span[@class='author notFaded']//text()").getall()).replace('\n', ''),
        }
        print(item)

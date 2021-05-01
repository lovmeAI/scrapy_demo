'''
myspider_redis
继承 from scrapy_redis.spiders import RedisSpider
'''
import scrapy
from urllib.parse import urljoin
from scrapy.http import HtmlResponse
from scrapy_redis.spiders import RedisSpider


class DangdangSpider(RedisSpider):
    name = 'ptwxz'
    allowed_domains = ['ptwxz.com']
    redis_key = 'ptwxz'

    # 分布式爬虫，爬虫不需要 start_urls，如果每个爬虫都定义了start_urls，那就会重复抓取，失去了分布式的意义
    # 需要另外在 redis 服务器中设置 redis_key + 爬取的 url
    # start_urls = ['https://www.ptwxz.com/booksort1/0/1.html']

    def urljoin(self, url):
        return urljoin('https://www.ptwxz.com', url)

    def parse(self, response: HtmlResponse, **kwargs):
        '''获取分类'''
        for level in response.xpath("//div[@class='block'][2]//li")[1:]:
            yield scrapy.Request(
                url=self.urljoin(level.xpath('.//a/@href').get()),
                callback=self.parse_book_list
            )

    def parse_book_list(self, response: HtmlResponse):
        for tr in response.xpath("//table[@class='grid']//tr")[1:]:
            yield scrapy.Request(
                url=self.urljoin(tr.xpath('.//td[1]/a/@href').get()),
                callback=self.parse_book_info
            )
        next_url_obj = response.xpath("//div[@id='pagelink']/strong/following-sibling::a[1]")
        if (next_url := next_url_obj.xpath(".//@href").get()) and next_url_obj.xpath(".//@class").get() != 'ngroup':
            yield scrapy.Request(
                url=self.urljoin(next_url),
                callback=self.parse_book_list
            )

    def parse_book_info(self, response: HtmlResponse):
        def info(num):
            temp = f"//div[@id='content']/table//tr[1]/td/table//tr[2]/td[{num}]/text()"
            _, value = response.xpath(temp).get().split('：')
            return value.replace('\xa0', '').replace(' ', '')

        item = {
            'book_title':    response.xpath("//table[@class='grid']/caption/font/text()").get(),
            'book_category': info(1),
            'book_author':   info(2),
            'book_size':     info(4),
            'book_url':      self.urljoin(response.xpath("//table[@class='grid']/caption/a/@href").get())
        }
        print(item)

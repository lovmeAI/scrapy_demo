import scrapy
from scrapy import Selector
from scrapy.http import HtmlResponse

from scrapy_demo.items import SinaSpiderItem


class SinaSpider(scrapy.Spider):
    name = 'sina'
    allowed_domains = ['sina.com.cn']
    start_urls = ['http://mil.news.sina.com.cn/roll/index.d.html?cid=57918&page=1']

    def parse(self, response: HtmlResponse, **kwargs):
        for li in response.xpath("//ul[@class='linkNews']/li"):
            li: Selector = li
            item = SinaSpiderItem()
            item['title'] = li.xpath(".//a/text()").extract_first()
            item['href'] = li.xpath(".//a/@href").extract_first()
            item['publish_data'] = li.xpath(".//span/text()").extract_first()
            yield scrapy.Request(
                url=item['href'],
                callback=self.parse_detail,
                meta={'item': item}
            )
            url = response.xpath("//span[@class='pagebox_next'][1]/a/@href").extract_first()

            if int(url.rsplit('=')[-1]) <= 25:
                yield scrapy.Request(url=url, callback=self.parse)

    def parse_detail(self, response: HtmlResponse):
        item = response.meta['item']
        item['content'] = response.xpath("//div[@id='article']/p//text()").extract()
        yield item
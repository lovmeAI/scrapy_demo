import scrapy
from scrapy import Selector
from scrapy.http import HtmlResponse

from scrapy_demo.items import IvskySpiderItem


class IvskySpider(scrapy.Spider):
    # 爬虫名称 scrapy crawl ivsky 启动
    name = 'ivsky'
    # 允许爬虫爬取的域名
    allowed_domains = ['ivsky.com']
    # 初始URL
    start_urls = ['https://www.ivsky.com/bizhi/liuyifei_t4443/']

    # 解析器
    def parse(self, response: HtmlResponse, **kwargs):
        for temp in response.xpath('//ul[@class="il"]/li'):
            temp: Selector = temp
            item = IvskySpiderItem()
            item['src'] = temp.xpath(".//div[@class='il_img']/a/img/@src").extract_first()
            item['url'] = temp.xpath(".//p/a/@href").extract_first()
            # yield 到 pipelines.py 处理，需要在配置文件中启动相应的管道配置
            yield item
        next_url = response.xpath("//a[@class='page-next']/@href").extract_first()
        if next_url:
            url_next = f'https://www.ivsky.com{next_url}'
            print(url_next)
            # 自动处理下一个请求，不会 yield 到管道
            yield scrapy.Request(url_next, callback=self.parse)

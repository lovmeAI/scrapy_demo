# Scrapy_Redis

## settings.py

```python
# 配置 scrapy-redis 爬虫信息
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
SCHEDULER_PERSIST = True
# SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderPriorityQueue"
# SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderQueue"
# SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderStack"

# 配置 scrapy-redis 链接信息
REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379
REDIS_ENCODING = 'utf-8'
# REDIS_PARAMS = {'password': 'abcd@1234'}
```

## gushiwen.py 原始的

```python
'''
redis 配置
'''
import re
import scrapy
from urllib.parse import urljoin
from scrapy.http import HtmlResponse

class SwSpider(scrapy.Spider):
    name = 'gushiwen'
    allowed_domains = ['gushiwen.com']
    start_urls = ['https://gushiwen.com/type/n/n/n/n.html']

    def parse(self, response: HtmlResponse, **kwargs):
        for a in response.xpath("//ul[@class='i_gx']/li"):
            href = urljoin(self.start_urls[0], a.xpath(".//div[@class='ycd']/h2/a/@href").get())
            yield scrapy.Request(
                url=href,
                callback=self.parse_xq
            )
        if next_url := response.xpath('//a[contains(text(), "下一页 >")]/@href').get():
            yield scrapy.Request(
                url=urljoin(self.start_urls[0], next_url),
                callback=self.parse
            )

    def parse_xq(self, response: HtmlResponse, **kwargs):
        yield {
            'href':    response.url,
            'author':  re.findall(r'.*?原文、翻译及赏析-.*?-(.*?)-古诗文网', response.xpath("/html/head/title/text()").get())[0],
            'title':   response.xpath("//div[@id='main']/h1/text()").get(),
            'chaodai': response.xpath(f"//div[@class='f12']/p[1]/text()").get().replace('朝代：', ''),
            'content': response.xpath("//div[@class='view']//text()").get().replace('\n', '').replace('\r', '').replace('\r\n', '').replace('\n', '').replace('\u3000', '').replace('\xa0', '').replace(' ', '')
        }
```

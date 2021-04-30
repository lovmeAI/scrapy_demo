# 这是一只不一样的scrapy爬虫(CrawlSpider)

#### 使用命名(请参考demo01)
创建`CrawlSpider`爬虫 `scrapy genspider -t crawl 爬虫名 允许爬取的域名`

```python
class TheorySpider(CrawlSpider):
    name = 'theory'
    allowed_domains = ['people.com.cn']
    # 其实URL
    start_urls = ['http://theory.people.com.cn/GB/82288/419180/419743/index1.html']

    rules = (
        # 提起指定的URL并调用回调函数，在回调函数解析数据
        Rule(LinkExtractor(allow=r'/n1/20\d+/\d+/c40531-\d+\.html'), callback='parse_item'),
        # 提取指定的URL 并循环rules
        Rule(LinkExtractor(allow=r'index\d+\.html'), follow=True),
    )

    def parse_item(self, response: HtmlResponse):
        item = {}
        print(response.xpath("//div[@class='text_c']/h1/text()").get(), response.url)
        return item
```
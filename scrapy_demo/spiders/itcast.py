import scrapy
from scrapy.http import HtmlResponse



class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    # 允许爬取的范围
    allowed_domains = ['itcast.cn']
    # 最开始请求的URL地址
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']

    def parse(self, response: HtmlResponse, **kwargs):
        # 处理start_urls地址对应的响应
        # ret1 = response.xpath("//div[@class='li_txt']/h3/text()").extract()
        # print(ret1)
        for li in response.xpath("//div[@class='tea_con']//li"):
            name = li.xpath(".//h3/text()").extract_first().strip()
            title = li.xpath(".//h4/text()").extract_first().strip()
            # logger.warning({'name': name, 'title': title})
            yield {'name': name, 'title': title}


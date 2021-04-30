import scrapy
from scrapy.http import HtmlResponse


class LovmeSpider(scrapy.Spider):
    name = 'lovme'
    allowed_domains = ['natapp1.cc']
    start_urls = ['http://lovme.natapp1.cc/details/FRhAXNq5conVP2Mx58tvnW']

    # 重写 start_requests 方法
    def start_requests(self):
        proxy = "http://3.224.205.253:80"  # 协议://ip:port
        cookies = "csrftoken=HFLQe5yb4aAu3dA4uXyLpQmZc6rKiyEApp9Kd6zeMgvu5tXkgC47GQeKMSRFMsUn; sessionid=7ldhg5p6ljii5rml9yfvnqu4uje15qxu"
        cookies = {item.rsplit('=')[0].rstrip(): item.rsplit('=')[1].rstrip() for item in cookies.rsplit(';')}
        yield scrapy.Request(
            url=self.start_urls[0],
            callback=self.parse,
            cookies=cookies,  # 使用cookie
            # meta={"proxy": proxy} # 使用代理
        )

    def parse(self, response: HtmlResponse, **kwargs):
        print(response.text)

import scrapy
from scrapy.http import HtmlResponse


class Github2Spider(scrapy.Spider):
    name = 'github2'
    allowed_domains = ['github.com']
    start_urls = ['https://github.com/login']

    def parse(self, response, **kwargs):
        yield scrapy.FormRequest.from_response(
            response=response,
            formdata={'login': 'qingyueheji@qq.com', 'password': 'silvery.0'},
            callback=self.after_login
        )

    def after_login(self, response: HtmlResponse):
        print(response.url)  # 跳转到首页 https://github.com 登录成功，否则登录失败

# POST 登录

## POST一

> 需要自己获得表单数据

```python
import scrapy
from scrapy.http import HtmlResponse


class GithubSpider(scrapy.Spider):
    name = 'github'
    allowed_domains = ['github.com']
    start_urls = ['https://github.com/login']

    def parse(self, response: HtmlResponse, **kwargs):
        def value(name):
            vv = response.xpath(f'//input[@name="{name}"]/@value').get()
            return vv if vv else ''

        def required_field(v='value'):
            vv = response.xpath(f'//input[starts-with(@name,"required_field")]/@{v}').get()
            return vv if vv else ""

        post_data = {
            'login':                   'qingyueheji@qq.com',
            'password':                'sil',
            'commit':                  value('commit'),
            'authenticity_token':      value('authenticity_token'),
            'trusted_device':          value('trusted_device'),
            'webauthn-support':        'supported',
            'webauthn-iuvpaa-support': 'unsupported',
            'return_to':               value('return_to'),
            'allow_signup':            value('allow_signup'),
            'client_id':               value('client_id'),
            'integration':             value('integration'),
            required_field('name'):    required_field(),
            'timestamp':               value('timestamp'),
            'timestamp_secret':        value('timestamp_secret'),
        }

        yield scrapy.FormRequest(
            url='https://github.com/session',
            formdata=post_data,
            callback=self.after_login
        )

    def after_login(self, response: HtmlResponse):
        print(response.url)  # 跳转到首页 https://github.com 登录成功，否则登录失败
```

### 重点

```python
yield scrapy.FormRequest(
    url='https://github.com/session',
    formdata={},
    callback=self.after_login
)
```

## POST二

> 自动提交表单，只需填写关键字段 formdata={}

```python
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
```

### 重点

```python
yield scrapy.FormRequest.from_response(
    response=response,
    formdata={'login': 'qingyueheji@qq.com', 'password': 'silvery.0'},
    callback=self.after_login
)
```
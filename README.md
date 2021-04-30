# middlewares 下载中间件

# middlewares.py

```python
class UserAgentDemoDownloaderMiddleware:
    def process_request(self, request: Request, spider):
        # 自动使用UserAgent
        ua = UserAgent()
        request.headers['User-Agent'] = ua.random

        # 中间件使用代理
        proxy = "http://3.224.205.253:80"  # 协议://ip:port
        request.meta["proxy"] = proxy
        return None


class CheckUserAgentDemoDownloaderMiddleware:
    def process_response(self, request, response, spider):
        # print(request.headers['User-Agent'])
        # for k, v in request.headers.items():
        #     print(k, v)

        return response
```

## settings.py

```python
# Enable or disable downloader middlewares
# 启用或禁用下载器中间件
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'scrapy_demo.middlewares.UserAgentDemoDownloaderMiddleware':      543,
    'scrapy_demo.middlewares.CheckUserAgentDemoDownloaderMiddleware': 544,
}
```
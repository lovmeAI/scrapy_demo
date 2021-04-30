# Scrapy settings for scrapy_demo project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'scrapy_demo'

SPIDER_MODULES = ['scrapy_demo.spiders']
NEWSPIDER_MODULE = 'scrapy_demo.spiders'

# 日志级别
LOG_LEVEL = "WARNING"

# 日志文件
# LOG_FILE = 'log.log'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# 爬取的默认User-Agent，除非被覆盖
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36'

# Obey robots.txt rules
# 如果启用,Scrapy将会采用 robots.txt策略
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# 并发请求(concurrent requests)的最大值,默认: 16
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# 下载器在下载同一个网站下一个页面前需要等待的时间,该选项可以用来限制爬取速度,减轻服务器压力。同时也支持小数:0.25 以秒为单位
# DOWNLOAD_DELAY = 3

# The download delay setting will honor only one of:
# 对单个网站进行并发请求的最大值
# CONCURRENT_REQUESTS_PER_DOMAIN = 16

# 对单个IP进行并发请求的最大值。如果非0,则忽略 CONCURRENT_REQUESTS_PER_DOMAIN 设定,使用该设定。
# 也就是说,并发限制将针对IP,而不是网站。
# 该设定也影响 DOWNLOAD_DELAY: 如果 CONCURRENT_REQUESTS_PER_IP 非0,下载延迟应用在IP而不是网站上。
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# 禁用Cookie（默认情况下启用）
# COOKIES_ENABLED = False

# 禁用Telnet控制台（默认启用）
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# 覆盖默认请求标头
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

# Enable or disable spider middlewares
# 启用或禁用蜘蛛中间件
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'myspider.middlewares.MyspiderSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# 启用或禁用下载器中间件
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'scrapy_demo.middlewares.ScrapyDemoDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# 启用或禁用扩展程序
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# 配置项目管道
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#     'scrapy_demo.pipelines.ScrapyDemoPipeline': 300,  # 300 权重等级
# }

# Enable and configure the AutoThrottle extension (disabled by default)
# 启用和配置自动限速扩展（默认情况下禁用）
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True

# The initial download delay
# 初始下载延迟
# AUTOTHROTTLE_START_DELAY = 5

# The maximum download delay to be set in case of high latencies
# 在高延迟的情况下设置的最大下载延迟
# AUTOTHROTTLE_MAX_DELAY = 60

# The average number of requests Scrapy should be sending in parallel to
# each remote server
# Scrapy请求的平均数量应该并行发送每个远程服务器
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0

# Enable showing throttling stats for every response received:
# 启用显示所收到的每个响应的调节统计信息
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# 启用和配置HTTP缓存（默认情况下禁用）
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'


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

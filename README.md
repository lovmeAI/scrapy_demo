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


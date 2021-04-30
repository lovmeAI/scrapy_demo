# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class IvskySpiderItem(scrapy.Item):
    src = scrapy.Field()
    url = scrapy.Field()


class SinaSpiderItem(scrapy.Item):
    title = scrapy.Field()
    href = scrapy.Field()
    publish_data = scrapy.Field()
    content = scrapy.Field()

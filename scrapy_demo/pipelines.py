# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from pymongo import MongoClient


class ScrapyDemoPipeline:
    def open_spider(self, spider):
        '''第一次打开执行，执行一次'''
        client = MongoClient()
        self.shw = client['spider']['gushiwen']

    # def close_spider(self, spider):
    #     pass

    def process_item(self, item, spider):
        return self.__getattribute__(spider.name)(item)

    def gushiwen(self, item):
        self.shw.insert(item)
        print(f"[{item['author']}]{item['title']}{item['href']}")

    def ptwxz(self, item):
        print(item)

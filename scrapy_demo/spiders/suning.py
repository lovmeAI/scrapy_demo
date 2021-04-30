import scrapy
from scrapy.http import HtmlResponse


class SuningSpider(scrapy.Spider):
    name = 'suning'
    allowed_domains = ['suning.com']
    start_urls = ['https://book.suning.com/?safp=d488778a.homepagev8.126605238652.1&safpn=10001']

    def parse(self, response: HtmlResponse, **kwargs):
        # 总分类
        for index, menu_name in enumerate(response.xpath("//div[@class='menu-list']/div[@class='menu-item']/dl/dt/h3/a/text()").extract(), 1):
            # 子分类
            for son_index, son_name in enumerate(response.xpath(f".//div[@class='menu-list']/div[@class='menu-sub'][{index}]/div[@class='submenu-left']/p[@class='submenu-item']/a/text()").extract(), 1):
                # 小分类
                for items in response.xpath(f".//div[@class='menu-list']/div[@class='menu-sub'][{index}]/div[@class='submenu-left']/ul[@class='book-name-list clearfix'][{son_index}]/li/a"):
                    item = {
                        'cfy1_name': menu_name,
                        'cfy2_name': son_name,
                        'cfy3_name': items.xpath('.//text()').extract_first(),
                        'cfy3_href': items.xpath('.//@href').extract_first()
                    }
                    yield scrapy.Request(
                        url=item['cfy3_href'],
                        callback=self.parse_book_list,
                        meta={'item': item}
                    )
                    break

    def parse_book_list(self, response: HtmlResponse):
        item = response.meta['item']
        for book in response.xpath('//ul[@class="clearfix"]/li/div/div/div'):
            item['book_url'] = 'https:' + book.xpath(".//div[@class='res-info']/p[@class='sell-point']/a/@href").extract_first()
            item['book_name'] = book.xpath(".//div[@class='res-info']/p[@class='sell-point']/a/text()").extract_first()

            yield scrapy.Request(
                url=item['book_url'],
                callback=self.parse_book_dettail,
                meta={'item': item}
            )

            # 下一页
            # //a[@id='nextPage']/@href
            # yield scrapy.Request(
            #     url=book.xpath("//a[@id='nextPage']/@href").extract_first(),
            #     callback=self.parse_book_list,
            #     meta={'item': item}
            # )

    def parse_book_dettail(self, response: HtmlResponse):
        item = response.meta['item']
        item['book_img'] = response.xpath('//a[@id="bigImg"]/img/@src').extract_first()
        item['book_price'] = response.xpath("//div[@id='mainPrice']/dl/dd/del/text()").extract_first()
        item['book_price1'] = response.xpath("//div[@id='mainPrice']/dl/dd/span//text()").extract_first()
        item['book_author'] = response.xpath("//div[@id='proinfoMain']/ul[@class='bk-publish clearfix']/li[1]/text()").extract_first()
        item['book_publisher'] = response.xpath("//div[@id='proinfoMain']/ul[@class='bk-publish clearfix']/li[2]/text()").extract_first()
        item['book_publisher_time'] = response.xpath("//div[@id='proinfoMain']/ul[@class='bk-publish clearfix']/li[3]/span[2]/text()").extract_first()
        for k, v in item.items():
            print('*', k, str(v).replace('\t', '').replace('\n', '').replace(' ', ''))
        print('*' * 100)

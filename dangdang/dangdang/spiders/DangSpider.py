# -*- coding:utf-8 -*-
import scrapy
from scrapy.http import Request
from dangdang.items import DangdangItem

class dangSpider(scrapy.Spider):
    name = 'dangdang'
    allowed_domains = ['dangdang.com']  # 允许域名

    # 爬虫的第一个爬取链接，启动爬虫就执行，并返回一个response交给parse函数
    start_urls = ['http://category.dangdang.com/cid4001075.html']
    def parse(self, response):
        # items = DangdangItem()
        # items['link']  = response.xpath('//a[@class="pic"]/@href').extract()

        url_list  = response.xpath('//a[@class="pic"]/@href').extract();
        for url in url_list:
            yield Request(url, callback=self.parse_name)
        for i in range(2,5):
            page_url = 'http://category.dangdang.com/pg{}.cid4001075.html'.format(i)
            yield Request(page_url, callback=self.parse)

    def parse_name(self, response):
        items = DangdangItem()
        items['title'] = response.xpath('//div[@class="name_info"]/h1/@title').extract()
        items['num'] = response.xpath('//a[@id="comm_num_down"]/text()').extract()
        items['link'] = response.url
        items['price'] = response.xpath('//p[@id="dd-price"]/text()').extract()
        yield items

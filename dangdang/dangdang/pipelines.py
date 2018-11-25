# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DangdangPipeline(object):
    def process_item(self, item, spider):
        print u'商品名称：' + item['title'][0]
        print u'商品评论数：' + item['num'][0]
        print u'商品价格：' + item['price'][0]

        return item

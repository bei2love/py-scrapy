# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SexItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    up_date = scrapy.Field()
    title = scrapy.Field()
    pic_count = scrapy.Field()
    url = scrapy.Field()
    author = scrapy.Field()
    update_time = scrapy.Field()
    image_urls = scrapy.Field()     #保存图片的地址
    images = scrapy.Field()         #保存图片的信息
    image_paths = scrapy.Field()
    path = scrapy.Field()


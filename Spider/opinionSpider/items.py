# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class OItem(scrapy.Item):

    id = scrapy.Field()
    title = scrapy.Field()
    text = scrapy.Field()
    heat = scrapy.Field()
    url = scrapy.Field()
    author = scrapy.Field()
    createdTime = scrapy.Field()
    source = scrapy.Field()


# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html
import scrapy
from scrapy.item import Item, Field

class MovieItem(scrapy.Item):
	name = scrapy.Field()
	year = scrapy.Field()
	category = scrapy.Field()
	link480 = scrapy.Field()
	link720 = scrapy.Field()
	link1080 = scrapy.Field()
	photo = scrapy.Field()

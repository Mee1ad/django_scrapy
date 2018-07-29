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
	image = scrapy.Field()

class SerialItem(scrapy.Item):
	name = scrapy.Field()
	year = scrapy.Field()
	category = scrapy.Field()
	image = scrapy.Field()

class SerialLinkItem(scrapy.Item):
	serial_id = scrapy.Field()
	name = scrapy.Field()
	season = scrapy.Field()
	quality = scrapy.Field()
	link = scrapy.Field()

class MovieLinkItem(scrapy.Item):
	movie_id = scrapy.Field()
	name = scrapy.Field()
	size = scrapy.Field()
	quality = scrapy.Field()
	link = scrapy.Field()

class SoftwareItem(scrapy.Item):
	name = scrapy.Field()
	image = scrapy.Field()
	link = scrapy.Field()

class MusicItem(scrapy.Item):
	name_fa = scrapy.Field()
	name_en = scrapy.Field()
	image = scrapy.Field()
	link128 = scrapy.Field()
	link320 = scrapy.Field()



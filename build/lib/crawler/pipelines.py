# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import dataset
from crawler.items import MovieItem , MovieLinkItem , SerialItem , SerialLinkItem , SoftwareItem , MusicItem

#db = dataset.connect('postgresql://yraitcrdcotuhb:6c41e7f3055517601bffd7be8434801d2bb96234171828dc7f860432705b405d@ec2-107-20-224-137.compute-1.amazonaws.com:5432/d7fi5emvoirfqc')
db = dataset.connect('sqlite:///mysearch.db')
class MoviePipeline(object):
	def process_item(self, item, spider):
		if not isinstance(item , MovieItem):
			return item
		table = db['movie']
		table.insert(dict(name=item['name'] , year=item['year'] , image=item['image'] , category=item['category']))
		return item

class SerialpipeLine(object):
	def process_item(self, item, spider):
		if not isinstance(item , SerialItem):
			return item
		table = db['serial']
		table.insert(dict(name=item['name'] , year=item['year'] , category=f"{item['category']}" , image=item['image'] ))
		return item


class MovieLinkPipeline(object):
	def process_item(self, item, spider):
		if not isinstance(item , MovieLinkItem):
			return item
		table = db['movie']
		result = table.find_one(name=item['name'])
		item['movie_id'] = result['id']
		table = db['movie_link']
		table.insert(dict(serial_id=item['serial_id'] , size=item['size'] , quality=item['quality'] , link=f"{item['link']}" ))
		return item

class SerialLinkPipeline(object):
	def process_item(self, item, spider):
		if not isinstance(item , SerialLinkItem):
			return item
		table = db['serial']
		result = table.find_one(name=item['name'])
		item['serial_id'] = result['id']
		table = db['serial_link']
		table.insert(dict(serial_id=item['serial_id'] , season=item['season'] , quality=item['quality'] , link=f"{item['link']}" ))
		return item

class SoftwarePipeline(object):
	def process_item(self, item, spider):
		if not isinstance(item , SoftwareItem):
			return item
		table = db['software']
		table.insert(dict(name=item['name'] , image=item['image'] , link=item['link']))
		return item

class MusicPipeline(object):
	def process_item(self, item, spider):
		if not isinstance(item , MusicItem):
			return item
		table = db['music']
		table.insert(dict(name_en=item['name_en'] , name_fa=item['name_fa'] , image=item['image'] , link128=item['link128'] , link320=item['link320']))
		return item
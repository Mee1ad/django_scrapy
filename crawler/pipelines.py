# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import dataset

db = dataset.connect('postgresql://yraitcrdcotuhb:6c41e7f3055517601bffd7be8434801d2bb96234171828dc7f860432705b405d@ec2-107-20-224-137.compute-1.amazonaws.com:5432/d7fi5emvoirfqc')
class CrawlerPipeline(object):
	def process_item(self, item, spider):
		if item['category'] == 'movie':
			table = db['movie']
		if item['category'] == 'serial':
			table = db['serial']
		#self.links  = self.links  + item['link'] + " + "
		table.insert(dict(name=item['name'] , year=item['year'] , photo=item['photo'] , link480=f"{item['link480']}" , link720=f"{item['link720']}" , link1080=f"{item['link1080']}" ))
		return item

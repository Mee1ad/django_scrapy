import scrapy
import scrapy.spiders
import json
import re
from crawler.items import SoftwareItem
from scrapy.http import Request

class AllSoftwareFinderSpyder(scrapy.Spider):
	name = "software"
	allowed_domains = ["soft98.ir"]
	start_urls = ['https://soft98.ir/']
	page = 1

	def parse(self,response):
		article_link = response.css("h2 > a::attr('href')").extract()
		for link in article_link:
			yield Request(link , callback=self.parse_software)
		print(article_link)
		next_link = response.css("ul.card-body.pagination.justify-content-center a::attr('href')").extract()[-1]
		print(next_link)
		self.page = self.page + 1
		if self.page > 2:
			return
		yield Request(next_link)


	def parse_software(self,response):
		app = softwareItem()

		name = response.css("h1 > a::text").extract()[0]
		pattern = '[A-z]+.+[A-z]+'
		app['name'] = re.search(pattern,name)[0]
		app['image'] = response.css("div:nth-child(3) > img::attr('src')").extract()[0]
		app['link'] = response.css("dd:nth-child(2) > a::attr('href')").extract()[0]

import scrapy
import scrapy.spiders
import json
import re
from crawler.items import SerialItem , SerialLinkItem
from scrapy.http import Request

class SerialFinderSpyder(scrapy.Spider):
	name = "serial"
	allowed_domains = ["dibamoviez.xyz"]
	start_urls = ['http://dibamoviez.xyz/series/']
	page = 1

	def parse(self,response):
		article_link = response.css("a.col-xs-6.no-padding.arch_series_fix::attr('href')").extract()
		print(article_link)
		#article_image = response.css("img.serimg::attr('src')").extract()
		#article_name = response.css("p.titser::text").extract()
		for link in article_link:
			yield Request(link , callback=self.parse_movies)
		next_link = response.css("a.next.page-numbers::attr('href')").extract()[0]
		self.page = self.page + 1
		if self.page > 1:
			return
		yield Request(next_link)


	def parse_movies(self,response):
		serial = SerialItem()
		year = response.css('span.series_box_options:first-of-type::text').extract()[0]
		pattern = '[0-9]+'
		serial['year'] = re.search(pattern,year)[0]
		serial['category'] = response.css('div.genre_box_film > a::text').extract()
		serial['image'] = response.css('img.wp-post-image::attr("src")').extract()[0]
		name = response.css('div.title_box_film > h1::text').extract()[0]
		pattern = '[A-z]+.+[A-z]+'
		serial['name'] = re.search(pattern,name)[0]
		yield serial

		serialLink = SerialLinkItem()
		pattern = '[A-z]+.+[A-z]+'
		serialLink['name'] = re.search(pattern , response.css("div.title_box_film > h1::text").extract()[0])[0]
		part = len(response.css("div.-body > div.-dl"))
		for section in range(part):
			serialLink['season'] = response.css('#sesid::text').extract()[section]
			serialLink['quality'] = response.css('#qutid::text').extract()[section]
			serialLink['link'] = response.css(f'div.-body > div:nth-child({section+1}) p > a::attr("href")').extract()
			yield serialLink


#download > div:nth-child(2)
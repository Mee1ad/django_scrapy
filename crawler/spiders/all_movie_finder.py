import scrapy
import scrapy.spiders
import json
import re
from crawler.items import MovieItem
from scrapy.http import Request

class AllMovieFinderSpyder(scrapy.Spider):
	name = "all_movies"
	allowed_domains = ["dibamoviez.pw"]
	start_urls = ['http://dibamoviez.pw/']
	page = 1

	def parse(self,response):
		article_link = response.css("div[class='movies'] > article > div > h2 > a::attr('href')").extract()
		for link in article_link:
			yield Request(link , callback=self.parse_movies)
		print(article_link)
		next_link = response.css("div:nth-child(3) > article > div > a.nextpostslink::attr('href')").extract()[0]
		self.page = self.page + 1
		if self.page > 2:
			return
		yield Request(next_link)


	def parse_movies(self,response):
		item = MovieItem()
		item['category'] = "movie"
		fullname = response.css("div[id='Body'] > main > article > div[class='section_one'] > div[class='title_box_film'] > h1::text").extract()[0]
		pattern = '([آ-ی0-9]+)'
		name = re.sub(pattern ,"" ,fullname)
		item['name'] = name.replace("  " , "")
		pattern = '[0-9]+'
		item['year'] = re.search(pattern ,fullname)[0]
		item['photo'] = response.css('div[id="Body"] > main > article > section.box-movie-details-body.clearfix > a > img::attr("src")').extract()[0]
		links = response.css("div[id='Body'] > main > section[class='box-movie-download'] > div> div > div > div > div > div > div > div> div> span:nth-child(odd) > a::attr(href)").extract()
		pattern = ["(.*)(480)(.*)" , "(.*)(720)(.*)" , "(.*)(1080)(.*)"]
		item['link480'] = []
		item['link720'] = []
		item['link1080'] = []
		items = [item['link480'] , item['link720'], item['link1080']]
		
		for i in range(3):
			for link in links:
				res = re.match(pattern[i] ,link)
				if res:
					items[i].append(res.group())

		yield item
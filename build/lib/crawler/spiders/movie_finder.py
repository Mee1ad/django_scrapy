import scrapy
import scrapy.spiders
import json
import re
from crawler.items import MovieItem , MovieLinkItem
from scrapy.http import Request

class AllMovieFinderSpyder(scrapy.Spider):
	name = "movie"
	allowed_domains = ["dibamoviez.xyz"]
	start_urls = ['http://dibamoviez.xyz/']
	page = 1

	def parse(self,response):
		article_link = response.css("article > a::attr('href')").extract()
		for link in article_link:
			yield Request(link , callback=self.parse_movies)
		print(article_link)
		next_link = response.css("a.nextpostslink::attr('href')").extract()[0]
		print(next_link)
		self.page = self.page + 1
		if self.page > 1:
			return
		yield Request(next_link)


	def parse_movies(self,response):
		movie = MovieItem()
		movie['category'] = "movie"
		name = response.css("div.title_box_film > h1::text").extract()[0]
		pattern = '[0-9]+'
		movie['year'] = re.search(pattern ,name)[0]
		pattern = '[A-z]+.+[A-z]+'
		movie['name'] = re.search(pattern,name)[0]
		movie['image'] = response.css('section.box-movie-details-body.clearfix img::attr("src")').extract()[0]
		yield movie
		links =  response.css("div.-body:nth-child(2) span:nth-child(2) > a::attr('href')").extract()
		movie_link = MovieLinkItem()
		movie_link['name'] = re.search(pattern,name)[0]
		for link in range(len(links)):
			movie_link['link'] = links[link]
			movie_link['quality'] =  response.css(f"div.-body:nth-child(2)  div.Block_dl:nth-child({link+1}) li:nth-child(1) > span::text").extract()[0]
			movie_link['size'] =  response.css(f"div.-body:nth-child(2)  div.Block_dl:nth-child({link+1}) li:nth-child(2) > span::text").extract()[0]
			yield movie_link
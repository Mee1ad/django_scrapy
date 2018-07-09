import scrapy
import scrapy.spiders
from Movie.items import SearchItem

class SearchSpyder(scrapy.Spider):
	name = "search"
	allowed_domains = ["dibamoviez.pw"]

	def __init__(self, category, movieName, *args, **kwargs):
		super(SearchSpyder, self).__init__(*args, **kwargs)
		self.item = SearchItem()
		self.item['movieName'] = movieName
		self.item['category'] = category
		self.start_urls = [f"http://dibamoviez.pw/?s={movieName.replace(' ','+')}"]
		
	def parse(self, response):
		def cat(x):
		    return {
		        'movie': 'فیلم',
		        'serial': 'سریال'
		    }[x] 

		for href , title in zip(response.css("body > div[id='Body'] > main > div > a::attr('href')").extract() , response.css("body > div[id='Body'] > main > div > a > h4::text").extract()):
				if cat(self.item['category']) in title:
					self.item['link'] = href
					print(href)
					yield self.item
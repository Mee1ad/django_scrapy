import scrapy.spiders
from crawler.items import MusicItem
from scrapy.http import Request

class SerialFinderSpyder(scrapy.Spider):
	name = "music"
	allowed_domains = ["www.tak3da.com"]
	start_urls = ['https://www.tak3da.com']
	page = 1

	def parse(self,response):
		article_link = response.css('div.posthead a::attr("href")').extract()
		for link in article_link:
			yield Request(link , callback=self.parse_music)
		next_link = response.css('#pagination a::attr("href")').extract()[-2]
		self.page = self.page + 1
		if self.page > 1:
			return
		yield Request(next_link)


	def parse_music(self,response):
		music = MusicItem()
		music['image'] = response.css('div.postbg img::attr("src")').extract()[0]
		name = response.css('strong:nth-child(2)::text').extract()[0]
		music['name_fa'] = name.replace("به نام" , "-")
		music['name_en'] = response.css('strong:nth-child(5)::text').extract()[-1]
		music['link128'] = response.css('p > a::attr("href")').extract()[1]
		music['link320'] = response.css('p > a::attr("href")').extract()[0]
		yield music
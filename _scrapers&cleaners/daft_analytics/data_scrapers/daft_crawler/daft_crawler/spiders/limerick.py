# -*- coding: utf-8 -*-
import selenium
from scrapy import Spider
from selenium import webdriver
from scrapy.selector import Selector
from scrapy.http import Request
from scrapy.loader import ItemLoader
from daft_crawler.items import DaftCrawlerItem
from selenium.common.exceptions import NoSuchElementException
from time import sleep


class LimerickSpider(Spider):
	name = 'limerick'
	allowed_domains = ['www.daft.ie']
	start_urls = ['http://www.daft.ie/']

	def parse(self, response):
		self.driver = webdriver.Chrome('D:/PYTHON/WebScraping/chromedriver')  ## path to chromedriver on disk
		self.driver.get('https://www.daft.ie/limerick-city/property-for-sale/')   ## limerick city property for sale

		sel = Selector(text = self.driver.page_source)
		property_urls = sel.xpath('.//*[@class="search_result_title_box"]/h2/a/@href').extract()   ## get property offer url
		property_urls = ['https://www.daft.ie' + property_url for property_url in property_urls]   ## full url


		## Next page click loop

		while True:

			try:
				next_page = self.driver.find_element_by_xpath('//li[@class="next_page"]/a')	
				sleep(2)                                                           
				self.logger.info('Wait 2 seconds')
				next_page.send_keys(selenium.webdriver.common.keys.Keys.ENTER)

				sel = Selector(text=self.driver.page_source)
				property_urls = sel.xpath('.//*[@class="search_result_title_box"]/h2/a/@href').extract()
				property_urls = ['https://www.daft.ie' + property_url for property_url in property_urls] 
				for url in property_urls:
					 yield Request(url, callback= self.parse_details)

			except NoSuchElementException:   					   
				self.logger.info('Last Page')
				self.driver.quit()
				break	

	## Property details	
			
	def parse_details(self, response):
		l = ItemLoader(item=DaftCrawlerItem(), response=response)				## initiate item loader 
		url = response.url
		property_name = response.xpath('normalize-space(.//div[@class="smi-object-header"]/h1/text())').extract_first() 

		price_string = response.xpath('//*[@id="smi-price-string"]/text()').extract_first()
		price = price_string.split(' Per ')[0]
		price = price.replace('€', '')
		price = price.replace(',', '')

		ber_rating = response.xpath('//*[@class="smi-object-header"]/span/span/img/@alt').extract_first()

		address = response.xpath('//*[@class="map_info_box"]/text()').extract()[0]

		property_type = response.xpath('//*[@class="header_text"]/text()').extract_first()
		property_type = property_type[1:]

		beds = response.xpath('//*[@class="header_text"]/text()').extract()[1]
		baths = response.xpath('//*[@class="header_text"]/text()').extract()[2]


		l.add_value('url',url)
		l.add_value('property_name',property_name)
		l.add_value('price', price)
		l.add_value('ber_rating', ber_rating)
		l.add_value('address', address)
		l.add_value('property_type',property_type)
		l.add_value('beds', beds)
		l.add_value('baths', baths)
		return l.load_item()
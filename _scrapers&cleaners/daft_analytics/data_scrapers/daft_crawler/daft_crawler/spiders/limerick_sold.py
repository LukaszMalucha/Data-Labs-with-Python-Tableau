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



class LimerickSoldSpider(Spider):
	name = 'limerick_sold'
	allowed_domains = ['www.daft.ie']
	start_urls = ['http://www.daft.ie/']

	def parse(self, response):	

			self.driver = webdriver.Chrome('D:/PYTHON/WebScraping/chromedriver')  ## path to chromedriver on disk
			for i in range(1,57):												  ## 365 days of sales	
				self.driver.get('https://www.daft.ie/price-register/limerick-city/?min_price=25000&max_price=5000000&pagenum={0}'.format(i))
				sel = Selector(text = self.driver.page_source)

				## separate property record
				property_row = sel.xpath('//*[@class="priceregister-searchresult"]')

				## extract elements
				for row in property_row: 					
					address = row.xpath('.//span[@class="priceregister-address"]/a[2]/text()').extract_first()
					price = row.xpath('.//span[@class="priceregister-dwelling-details"]/b/text()').extract_first()	
					property_details = row.xpath('normalize-space(.//span[@class="priceregister-dwelling-details"]/text()[2])').extract_first()
					property_details = property_details.split('| ')
					date = property_details[1]
					property_type = property_details[2]
					try:
						beds = property_details[3]
						baths = property_details[4]
					except:
						beds = ''
						baths = ''	

					## data extraction	

					yield {'address': address,
							'price': price,
							'property_type': property_type,
							'beds': beds,
							'baths': baths}		
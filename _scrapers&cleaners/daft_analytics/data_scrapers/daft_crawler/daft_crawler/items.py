# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DaftCrawlerItem(scrapy.Item):
	url = scrapy.Field()
	property_name = scrapy.Field()
	price = scrapy.Field()
	ber_rating = scrapy.Field()
	address = scrapy.Field()
	property_type = scrapy.Field()
	beds = scrapy.Field()
	baths = scrapy.Field()
	

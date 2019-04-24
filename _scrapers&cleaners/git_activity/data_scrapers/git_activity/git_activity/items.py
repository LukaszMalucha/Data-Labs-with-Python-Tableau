# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GitActivityItem(scrapy.Item):
	day_data = scrapy.Field()
	contributions = scrapy.Field()

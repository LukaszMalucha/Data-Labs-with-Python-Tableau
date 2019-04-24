# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FaangItem(scrapy.Item):
	top_skills = scrapy.Field()
	skill_sets = scrapy.Field()


class LinkItem(scrapy.Item):
	link = scrapy.Field()

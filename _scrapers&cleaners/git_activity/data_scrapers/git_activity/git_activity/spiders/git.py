# -*- coding: utf-8 -*-
import selenium
from scrapy import Spider
from selenium import webdriver
from scrapy.selector import Selector
from scrapy.http import Request
from scrapy.loader import ItemLoader
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

from git_activity.items import GitActivityItem


## AVOID HANDSHAKE ERRORS
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')  
options.add_argument('--ignore-ssl-errors')

class GitSpider(Spider):
	name = 'git'
	allowed_domains = ['https://github.com/LukaszMalucha']
	start_urls = ['https://github.com/LukaszMalucha/']

	def parse(self, response):

		self.driver = webdriver.Chrome('D:/PYTHON/WebScraping/chromedriver',chrome_options=options)  ## path to chromedriver on disk
		self.driver.get('https://github.com/LukaszMalucha/')

		self.driver.execute_script("window.scrollTo(100, 1600);") 

		

		sel = Selector(text = self.driver.page_source)

		day_square = sel.xpath('//*[@class="day"]')
		for day in day_square:
			l = ItemLoader(item = GitActivityItem(), selector= day)
			day_data = day.xpath('./@data-date').extract_first()
			contributions = day.xpath('./@data-count').extract_first()
			l.add_value('day_data', day_data)
			l.add_value('contributions', contributions)

			yield l.load_item()



		self.driver.quit()
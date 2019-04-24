# -*- coding: utf-8 -*-
import selenium
from scrapy import Spider
from parsel import Selector
from selenium import webdriver
from scrapy.selector import Selector
from scrapy.http import Request
from scrapy.loader import ItemLoader
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from faang.items import LinkItem
from faang.env import *

## AVOID HANDSHAKE ERRORS
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')  
options.add_argument('--ignore-ssl-errors')



class LinksSpider(Spider):
	name = 'links'
	allowed_domains = ['www.linkedin.com']
	start_urls = ['http://linkedin.com/']

	def parse(self, response):
			
			self.driver = webdriver.Chrome('<CHROMEDRIVER DISK LOCATION>',chrome_options=options)  ## path to chromedriver on disk
			self.driver.get('https://linkedin.com/')   

			## Login Handling
				
			username = self.driver.find_element_by_class_name('login-email')
			username.send_keys('XXXXX')  ## username
			sleep(0.5)	

			password = self.driver.find_element_by_id('login-password')
			password.send_keys('XXXX')  ## password
			sleep(0.5)
			
			sign_in_button = self.driver.find_element_by_xpath('//*[@type="submit"]')
			sign_in_button.click()
			sleep(2)


			for p in range(1,34):

				self.driver.get(XXXX.format(p))   ## Search Link from env.py
				self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

				sleep(2)

				## Link Extractor
				
				sel = Selector(text = self.driver.page_source)
				search = sel.xpath('.//*[@class="search-results-page core-rail"]')
				links = search.xpath('.//a[contains(@href, "/in/")]/@href').extract()
				for link in links:
					l = ItemLoader(item = LinkItem(), selector=link)
					link = "https://www.linkedin.com" + link
					l.add_value('link', link)
					yield l.load_item()	
			

			self.driver.quit()	

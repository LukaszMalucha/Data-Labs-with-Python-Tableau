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
from faang.items import FaangItem
import pandas as pd

## AVOID HANDSHAKE ERRORS
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')  
options.add_argument('--ignore-ssl-errors')



### LOAD EXTRACTED PROFILE LINKS (links.py spider)
dataset = pd.read_csv('XXXXXX') ## choose company links 
dataset = dataset.dropna()
dataset = dataset.drop_duplicates()
link_urls = dataset['link'].values.tolist() 



class SkillsSpider(Spider):
	name = 'skills'
	allowed_domains = ['www.linkedin.com']
	start_urls = ['http://linkedin.com/']

	def parse(self, response):
		
		self.driver = webdriver.Chrome('D:/PYTHON/WebScraping/chromedriver',chrome_options=options)  ## path to chromedriver on disk
		self.driver.get('https://linkedin.com/')   

		## Login handling
		
		username = self.driver.find_element_by_class_name('login-email')
		username.send_keys('XXXX')
		sleep(0.5)	

		password = self.driver.find_element_by_id('login-password')
		password.send_keys('XXXXX')
		sleep(0.5)
		
		sign_in_button = self.driver.find_element_by_xpath('//*[@type="submit"]')
		sign_in_button.click()
		sleep(2)

		for element in link_urls:
			l = ItemLoader(item = FaangItem(), selector= element)
			self.driver.get(element)

			## Window scroller to discover button
			
			self.driver.execute_script("window.scrollTo(0, 1600);")
			try:
				show_more_button = self.driver.find_element_by_xpath('//*[@class="pv-profile-section__card-action-bar pv-skills-section__additional-skills artdeco-container-card-action-bar"]')	
			except:
				sleep(1)
				try:	
					self.driver.execute_script("window.scrollTo(0, 2100);")
					show_more_button = self.driver.find_element_by_xpath('//*[@class="pv-profile-section__card-action-bar pv-skills-section__additional-skills artdeco-container-card-action-bar"]')
				except:
					sleep(1)
					try:
						self.driver.execute_script("window.scrollTo(0, 2600);")
						show_more_button = self.driver.find_element_by_xpath('//*[@class="pv-profile-section__card-action-bar pv-skills-section__additional-skills artdeco-container-card-action-bar"]')
					except:
						sleep(1)
						try:
							self.driver.execute_script("window.scrollTo(0, 3600);")
							show_more_button = self.driver.find_element_by_xpath('//*[@class="pv-profile-section__card-action-bar pv-skills-section__additional-skills artdeco-container-card-action-bar"]')
						except:
							pass	


			sleep(2)
			
			## Skill & Country Extractor:
			
			try:
				actions = ActionChains(self.driver)                               
				actions.move_to_element(show_more_button).perform()
				show_more_button.click()
				sleep(3)
				sel = Selector(text = self.driver.page_source)
				country = sel.xpath("normalize-space(.//h3/text())").extract_first()
				top_skills = sel.xpath('.//*[@class="Sans-17px-black-100%-semibold"]/text()').extract()[0:3]

						
				div = sel.xpath('.//div[@class="pv-skill-category-list pv-profile-section__section-info mb6 ember-view"]')
				skill_sets = []
				for group in div:		
					skill_group = group.xpath('./h3/text()').extract_first()
					skills = group.xpath('.//*[@class="pv-skill-category-entity__name "]/a/span/text()').extract()
					skill_set = {skill_group : skills }
					skill_sets.append(skill_set)

				l.add_value('country', country)	
				l.add_value('top_skills', top_skills)	
				l.add_value('skill_sets', skill_sets)
				
			except:
				pass	

			yield l.load_item()

		self.driver.quit()
			

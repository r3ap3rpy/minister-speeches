from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from bs4 import BeautifulSoup
from pprint import pprint
from time import sleep
from random import randint
import json

root_url = "https://www.kormany.hu/"
start_url = "https://www.kormany.hu/hu/a-miniszterelnok/beszedek-publikaciok-interjuk"


driver = webdriver.Firefox()
driver.get(start_url)

LastPage = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath("//a[@class='last']"))

try:
	LastPage = int(LastPage.get_attribute('href').split('page=')[1])
except:
	print("Cannot identify the last page, cannot continue!")
	raise SystemExit
print(f"There are a total of {LastPage} pages that I can pull!")
ToAnalyse = {}
print(LastPage)
for i in range(41,50):
	current_url = start_url + f"?page={i}"
	print(f"Pulling sub_urls from page: {i}")
	driver.get(url = current_url)
	current_page = WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_xpath("//div[@id='Footer']"))
	print(current_url)
	current_page_parsed = BeautifulSoup(driver.page_source,'html.parser')
	ToAnalyse[i] = {'url':current_url,'content':[]}
	j = 1
	subsite_urls = []
	for article in current_page_parsed.findAll('div',{'class':'article'}):
		for u in BeautifulSoup(str(article),'html.parser').findAll('a'):
			if u['href'] != "hu/a-miniszterelnok":
				subsite_urls.append(u['href'])


	for subsite in subsite_urls:
	#for subsite in [ _ for _ in current_page_parsed.findAll('a') if 'beszedek' in  _['href'] ]:
		print(subsite)
	#for subsite in [ _ for _ in current_page_parsed.findAll('a')]:
		sub_url = root_url + subsite
		sub_page_name = subsite.split('/')[-1]
		print(sub_url)
		sub_page_name = sub_page_name.replace('-',' ').capitalize()
		print(f"Pulling speech from sub_urls page: {j}, named: {sub_page_name}")
		j += 1
		foundIt = False
		for k in range(1,4):
			sleep(3)
			print(f"Trying {k}")
			try:
				driver.get(url = sub_url)
				subpage_content = WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_xpath("//div[@class='article-content']"))
				subpage_parsed = BeautifulSoup(driver.page_source,'html.parser')
				subpage_parsed = subpage_parsed.find('div',{'class':'article-content'})
				ToAnalyse[i]['content'].append({'url':sub_url,'title':sub_page_name,'talk':subpage_parsed.text})
				foundIt = True
			except:
				pass
			if foundIt:
				break
			#sleep(1)
driver.close()

with open("Speeches41_50.txt","w") as speeches:
	json.dump(ToAnalyse,speeches)
#pprint(ToAnalyse)
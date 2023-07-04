#Thank you to W3 School and Verneacademy for teaching me the  ropes of Web Scraping
#And thank you ChatGPT for teaching me the inner workings of Selenium

import requests
from bs4 import BeautifulSoup
from selenium import webdriver

option = webdriver.ChromeOptions()
option.add_argument('--headless')
driver = webdriver.Chrome(options=option)

driver.get("https://steamstat.us/")
status = driver.page_source

soup = BeautifulSoup(status, 'html.parser')
mad_status = soup.find("span", id="mad")

print("Madrid Status:", mad_status.text)

driver.close()
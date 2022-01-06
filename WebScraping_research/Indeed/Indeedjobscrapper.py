import pandas as pd
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time


# Driver path 
DRIVER_PATH = "C:/Users/elgha/Documents/GitHub/WEB-SCRAPING-AUTOMATION/WebScraping_research/Indeed/chromedriver"


driver = webdriver.Chrome(executable_path = DRIVER_PATH)
driver.implicitly_wait(3)

driver.get('https://ca.indeed.com/')

# Accept Cookies

try:
    cookie = driver.find_element_by_xpath("//button[contains(text(),'OK')]")
    cookie.click()
except:
    pass

#Search of job key words 
"""
    Done {# DATA / FRANCE = 500+ }
    Done {#Data Science /}
    Done {#Analytics Engineer}
    Done {#Data Analytics}
    ................................................................
"""
# 
jobtype = driver.find_element_by_xpath('//input[@id="text-input-what"]')
jobtype.send_keys(['gis'])

#search location
location = driver.find_element_by_xpath('//input[@id="text-input-where"]')
location.send_keys(['Canada'])


#click search
find = driver.find_element_by_xpath("//button[contains(text(),'To research')]")
find.click()



# AFTER Advanced search:


print("ayob")

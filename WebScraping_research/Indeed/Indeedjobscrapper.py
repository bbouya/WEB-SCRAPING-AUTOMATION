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
find = driver.find_element_by_xpath("//button[contains(text(),'Rechercher')]")
find.click()



# AFTER Advanced search:
advanced_search = driver.find_element_by_xpath("//a[contains(text(),'Recherche avancée')]")
advanced_search.click()

# Set diplsay limit of 30 results per page.
display_limit = driver.find_element_by_xpath("//select[@id = 'limit']//option[@value = '30']")
display_limit.click()


search_button = driver.find_element_by_xpath('//*[@id = "fj"]')
search_button.click()

close_popup = driver.find_element_by_id('popover-x')
close_popup.click()



# Let the driver wait 3 seconds to locate the element before exiting out 
driver.implicitly_wait(3)

titles = []
companies = []
locations = []
links = []
reviews = []
salaries = []

# loop
for i in range(0,2):
    
  
   
  #job_card = driver.find_elements_by_xpath('//div[contains(@class,"job_seen_beacon")]')
    job_card = driver.find_elements_by_xpath('//a[contains(@id,"job_")]')
    
    for job in job_card:
       
    #.  not all companies have review
        try:
            review = job.find_element_by_xpath('.//span[@class="ratingNumber"]').text
        except:
            review = "None"
        reviews.append(review)
        print(review)

        try:
            location = job.find_element_by_xpath('.//div[contains(@class,"companyLocation")]').text
        except:
            location = "None"
    #.  tells only to look at the element       
        locations.append(location)
        print(location)

                                    
        try:
            title = job.find_element_by_xpath('.//h2[contains(@class, "jobTitle")]').text
        except:
            title = job.find_element_by_xpath('.//h2[contains(@class, "jobTitle")]').get_attribute(name="title")
        titles.append(title)
        print(title)
        
        
        links.append(job.get_attribute(name="href"))
   
        companies.append(job.find_element_by_xpath('.//span[@class="companyName"]').text)
        
        
    time.sleep( 2 )
      
 
    try:
        next_page = driver.find_element_by_xpath('//a[@aria-label={}]//span[@class="pn"]'.format(i+2))
        next_page.click()
        
    except NoSuchElementException:
        break
        
    

    print("Page: {}".format(str(i+2)))           

df_da=pd.DataFrame()
df_da['Title']=titles
df_da['Company']=companies
df_da['Location']=locations
df_da['Link']=links
df_da['Review']=reviews
 
   
pd.options.display.max_columns= None      
print(df_da.head(2))
df_da.to_csv('testgis10312021.csv') 

print("ayob")

import requests
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from selenium import webdriver
import os
from random import randint
from time import sleep
from time import time

# Name = "Aswin Srinivasan"
# Company = "ingram micro"
# click = []
#
# driver = webdriver.Edge(executable_path=r'C:\Users\inragy00\Downloads\msedgedriver')
# sleep(randint(1, 2))
# url = "https://www.google.com/search?q=" + Name + "+" + Company + "+" + "Zoominfo" + ""
# driver.get(url)
# html = driver.page_source
# soup = BeautifulSoup(html, 'html.parser')
# #for title in soup.find('h3', {'class': "LC20lb DKV0Md"}):
# for title in soup.find('div', {'class':"yuRUbf"}):
#        project_href = [i['href'] for i in title.find_all('a', href=True)if i['href'] != "#"]
#        #print(project_href)
#        if project_href:
#            #print(project_href)
#            #click.append(project_href[0])
#            sleep(randint(1, 2))
#            driver.get(project_href[0])
#            html1 = driver.page_source
#            soup1 = BeautifulSoup(html1, 'html.parser')
#            driver.find_element_by_class_name('search-bar-input').click()
#            print("Search box is clicked")
#            driver.find_element_by_class_name('search-bar-input').send_keys('Yugesh Ragavan Ingram')
#            print("input given")
#             #for name in soup1.find('h1', {'class': "person-name"}):
#             #    for role in soup1.find('h2', {'class': "person-role"}):
#             #        for update in soup1.find('span', {'class': "icon-text-content content"}):
#             #          print(name, "---", role, "---", update)

driver = webdriver.Chrome(executable_path=r'C:\Users\inragy00\Downloads\chromedriver.exe')
driver = webdriver.Edge(executable_path=r'C:\Users\inragy00\Downloads\msedgedriver')
sleep(randint(1, 2))
url = "https://www.zoominfo.com/people-search/"
driver.get(url)
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
sleep(randint(7, 8))
l= driver.find_element_by_link_text("Daniel Pearlson")
l.click()
Search = driver.find_element_by_class_name('search-bar-input').send_keys('Yugesh Ragavan Ingram')
# #sleep(randint(7, 8))
#Search.send_Keys(Keys.ENTER);
#driver.find_element_by_class_id('search-bar-img').click()

#for person in soup.find('div', {'class': "tableRow_personName"}):
    #project_href = [i['href'] for i in person.find_all('a', href=True)if i['href'] != "#"]
    #print(project_href)
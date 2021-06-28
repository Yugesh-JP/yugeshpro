import requests
import os
from bs4 import BeautifulSoup
from selenium import webdriver
import csv
from random import randint
from time import sleep
import re

headers = ['Company', 'web_domains']

if not os.path.exists(r'VendorNames_Websites test.csv'):
    with open('VendorNames_Websites test.csv', 'a+', newline="") as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()


driver = webdriver.Edge(executable_path=r'C:\Users\inragy00\Downloads\msedgedriver')

with open(('req.csv'), "r", encoding="utf8") as f:
    reader = csv.reader(f)
    next(reader)
    for col in reader:
        try:
            company = col[0].strip()
            print(col[0])
            sleep(randint(1, 2))
            G_Search = "https://www.google.com/search?q=" + company + ""
            driver.get(G_Search)
            html = driver.page_source
            soup = BeautifulSoup(html, 'html.parser')

            #for cite in soup.find('cite', {'class': "iUh30 Zu0yb tjvcx"}):
                #print(company, cite)
            for cite in soup.find('cite', {'class': "iUh30 Zu0yb qLRx3b tjvcx"}):
                Seperate = cite.splitlines(0)
                print(company, cite)
                with open('VendorNames_Websites test.csv', 'a+', newline="", encoding='utf-8') as file:
                    writer = csv.DictWriter(file, fieldnames=headers)
                    writer.writerow({'Company': company,
                                 'web_domains': cite,
                                 })
        except Exception as e:
            #print('exception handled----->',e)
            #with open('VendorNames_Websites test.csv', 'a+', newline="", encoding='utf-8') as file:
                #writer = csv.DictWriter(file, fieldnames=headers)
                #writer.writerow({'Company': company,
                #                 'web_domains': e,
                #                 })
            continue





#Url="https://www.google.com/search?q=sundar+pichai+google+zoominfo&rlz=1C1GCEA_enIN943IN943&sxsrf=ALeKk02w4b6hOieVpaDdB_6En_Sz1dzZYQ%3A1621828384912&ei=ICOrYMOEN83Zz7sP-synyAs&oq=sundar+&gs_lcp=Cgdnd3Mtd2l6EAMYAjIECCMQJzIKCC4QxwEQrwEQJzIECCMQJzIFCC4QsQMyCAgAELEDEIMBMggILhCxAxCDATICCAAyAggAMgUIABCxAzIICAAQsQMQgwE6BwgjELADECc6BwgjEOoCECc6BQguEJECOgUIABCRAjoECC4QQzoLCC4QsQMQxwEQowI6CAguEMcBEK8BOgcIIxDJAxAnOgUIABCSAzoLCC4QsQMQxwEQrwFQjnFY_YsBYPiiAWgDcAB4A4AB5AGIAZATkgEGMC4xMy4ymAEAoAEBqgEHZ3dzLXdperABCsgBAsABAQ&sclient=gws-wiz"
#Url="https://www.google.com/search?q=aswin+srinivasan+ingram+micro&rlz=1C1GCEA_enIN943IN943&oq=&sourceid=chrome&ie=UTF-8"
#Url = "https://www.google.com/search?q=yugesh+ragavan+ingram&rlz=1C1GCEA_enIN943IN943&oq=yug&aqs=chrome.0.69i59j69i57j69i59j46i67i433l2j69i60l3.1925j0j7&sourceid=chrome&ie=UTF-8"
#name = "Aswin Srinivasan"
#company = "ingram micro"
#G_Search = "https://www.google.com/search?q=" + name + "+" + company + "+" + "Zoominfo" +""
#G_Search = "https://www.google.com/search?q=" + company + ""
#driver.get(G_Search)
#driver.get(Url)

#print (soup)
#for element in soup.find('div',{'class': "TbwUpd NJjxre"}):
#for cite in soup.find('cite',{'class': "iUh30 Zu0yb tjvcx"}):
    #for cite2 in soup.find('cite', {'class': "iUh30 Zu0yb qLRx3b tjvcx"}):
        #for cite3 in soup.find('cite', {'class': "ellip iUh30"}):
#   print(cite)
     #seperate=element.split("- ")
     #for link in soup.find('div',{'class': "kCrYT"}):
        #print(element,"\n", (link))
        #print ("ingram" in element,"\n",len(element),"\n",seperate)
        #print(element)

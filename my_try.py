import requests
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from selenium import webdriver
import os
from random import randint
from time import sleep
import csv
headers = ['Name', 'Company Name', 'First Name', 'Last Name', 'Role', 'Company', 'Last Update', 'Zoominfo Link']


if not os.path.exists(r'Roles_Test_output_zA.csv'):
    with open('Roles_Test_output_zA.csv', 'a+', newline="") as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()


#Name = "Krishna Kurapaty"
#Company = "Ingram Micro"
click = []

#driver = webdriver.Chrome(executable_path=r'C:\Users\inragy00\Downloads\chromedriver.exe')
driver = webdriver.Edge(executable_path=r'C:\Users\inragy00\Downloads\msedgedriver')

with open(('Roles_TestA.csv'), "r", encoding="utf8") as f:
    reader = csv.reader(f)
    next(reader)
    for col in reader:
        try:
            company = col[1].strip()
            Name = col[0].strip()
            print(col[0], col[1])
            firstname = Name.split(" ")[0].lower()
            lastname = Name.split(" ")[-1].lower()
            sleep(randint(1, 2))
            url = "https://www.google.com/search?q=" + Name + "+" + company + "+" + "Zoominfo" + ""
            driver.get(url)
            html = driver.page_source
            soup = BeautifulSoup(html, 'html.parser')
#for title in soup.find('h3', {'class': "LC20lb DKV0Md"}):
            for title in soup.find('div', {'class':"yuRUbf"}):
             project_href = [i['href'] for i in title.find_all('a', href=True)if i['href'] != "#"]
        #print(project_href)
            if project_href:
             print(project_href)
            #click.append(project_href[0])
            sleep(randint(1, 2))
            driver.get(project_href[0])
            html1 = driver.page_source
            soup1 = BeautifulSoup(html1, 'html.parser')
            for name in soup1.find('h1', {'class': "person-name"}):
                for role in soup1.find('h2', {'class': "person-role"}):
                    seperate=role.split(" at ")
                    for update in soup1.find('span', {'class': "icon-text-content content"}):
                      #print(name, "---", role, "---", update)
                      cfirstname = name.split(" ")[0].lower()
                      clastname = name.split(" ")[-1].lower()
                      #print("----------------------")
                      #print(cfirstname, firstname, clastname, lastname)
                      if cfirstname == firstname and clastname == lastname:
                        print(cfirstname, clastname)
                        with open('Roles_Test_output_zA.csv', 'a+', newline="", encoding='utf-8') as file:
                            writer = csv.DictWriter(file, fieldnames=headers)
                            writer.writerow({'Name': Name,
                             'Company Name': company,
                             'First Name': cfirstname.capitalize(),
                             'Last Name': clastname.capitalize(),
                             'Role': seperate[0],
                             'Company': seperate[1],
                             'Last Update': update,
                             'Zoominfo Link': project_href,
                             })
                      else:
                          print("Zoominfo not found")
                      with open('Roles_Test_output_zA.csv', 'a+', newline="", encoding='utf-8') as file:
                        writer = csv.DictWriter(file, fieldnames=headers)
                        writer.writerow({'Name': Name,
                         'Company Name': company,
                         'First Name': cfirstname.capitalize(),
                         'Last Name': clastname.capitalize(),
                         'Role': seperate[0],
                         'Company': seperate[1],
                         'Last Update': update,
                         'Zoominfo Link': project_href,
                         })
        except Exception as e:
            print('exception handled----->',e)
            with open('Roles_Test_output_zA.csv', 'a+', newline="", encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=headers)
                writer.writerow({'Name': Name,
                         'Company Name': company,
                         'First Name': None,
                         'Last Name': None,
                         'Role': None,
                         'Company': None,
                         'Last Update': None,
                         'Zoominfo Link': e,
                         })
            continue
#print(click)



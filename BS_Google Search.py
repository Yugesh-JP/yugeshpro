import csv
import os

import editdistance
import pandas as pd
from pip._internal.utils import encoding
from selenium import webdriver
from bs4 import BeautifulSoup
from random import randint
from time import sleep
headers = ['Name', 'CompanyName', 'FirstName', 'LastName', 'Company', 'Role', 'LinkedIn Url', 'check', 'G_Search']


if not os.path.exists(r'Test_C_Output.csv.csv'):
    with open('Test_C_Output.csv', 'a+', newline="") as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()

#driver = webdriver.Chrome(executable_path=r'C:\Users\inragy00\Downloads\chromedriver.exe')
driver = webdriver.Edge(executable_path=r'C:\Users\inragy00\Downloads\msedgedriver')

#with open('EMEA DAAS 859 P1.csv', 'r') as f:
with open(('Test_C.csv'), "r", encoding="utf8") as f:
    reader = csv.reader(f)
    next(reader)
    for col in reader:
        try:
            company = col[1].strip()
            name = col[0].strip()
            print(col[0], col[1])
            firstname = name.split(" ")[0].lower()
            lastname = name.split(" ")[-1].lower()
            sleep(randint(1, 2))
            G_Search = "https://www.google.com/search?q=" + name + "+" + company + ""
            driver.get(G_Search)
            html = driver.page_source
            soup = BeautifulSoup(html, 'html.parser')

            #companyrole = soup.find("div", {"class": "fG8Fp uo4vr"})
            companyrole = soup.find("div", {"class": "MUxGbd wuQ4Ob WZ8Tjf"})
            validator = companyrole.find_parent("div", {"class": "IsZvec"}).find_previous_sibling("div", {"class": "yuRUbf"})
            check_text = validator.find("h3", {"class": "LC20lb DKV0Md"}).get_text()
            missing_parent = companyrole.find_parent("div", {"class": "IsZvec"})
            if missing_parent.find("div", {"class": "TXwUJf"}):
                missingClass = missing_parent.find("div", {"class": "TXwUJf"})
                mis_text = missingClass.get_text()
            else:
                mis_text = None

            cfirstname = check_text.split(' - ')[0].split(" ")[0].lower()
            clastname = check_text.split(' - ')[0].split(" ")[-1].lower()

            if cfirstname == firstname and clastname == lastname:
            #if cfirstname == firstname:
            #if clastname == lastname:
                if missing_parent:
                    print(cfirstname, clastname)
                    data = companyrole.get_text()
                    refine_text = data.split(" · ")
                    role, companyname = refine_text[1], refine_text[2]
                    #role, companyname = refine_text[-2], refine_text[-1]
                    print('Role: {}\nCurrent Company: {}'.format(role, companyname))
                    link = validator.find("a", href=True)
                    print(link['href'])
                    linkedurl = link['href']
                    with open('Test_C_Output.csv', 'a+', newline="", encoding='utf-8') as file:
                        # headers = ['Name',
                        #            'CompanyName',
                        #            'FirstName',
                        #            'LastName',
                        #            'Company',
                        #            'Role',
                        #            'LinkedIn Url',
                        #            'check'
                        #            ]
                        writer = csv.DictWriter(file, fieldnames=headers)
                        writer.writerow({'Name': name,
                                         'CompanyName': company,
                                         'FirstName': cfirstname.capitalize(),
                                         'LastName': clastname.capitalize(),
                                         'Company': companyname,
                                         'Role': role,
                                         'LinkedIn Url': linkedurl,
                                         'check': mis_text,
                                         'G_Search': G_Search
                                         })

            else:
                print('No Linkedin found!')
                with open('Test_C_Output.csv', 'a+', newline="", encoding='utf-8') as file:
                    # headers = ['Name',
                    #            'CompanyName',
                    #            'FirstName',
                    #            'LastName',
                    #            'Company',
                    #            'Role',
                    #            'LinkedIn Url',
                    #            'check'
                    #            ]
                    writer = csv.DictWriter(file, fieldnames=headers)
                    writer.writerow({'Name': name,
                                     'CompanyName': company,
                                     'FirstName': None,
                                     'LastName': None,
                                     'Company': None,
                                     'Role': None,
                                     'LinkedIn Url': "Linked Not Found!",
                                     'check':None,
                                     'G_Search': G_Search
                                   })
        except Exception as e:
            print('exception handled----->',e)
            with open('Test_C_Output.csv', 'a+', newline="", encoding='utf-8') as file:
                # headers = ['Name',
                #            'CompanyName',
                #            'FirstName',
                #            'LastName',
                #            'Company',
                #            'Role',
                #            'LinkedIn Url',
                #            'check'
                #            ]
                writer = csv.DictWriter(file, fieldnames=headers)
                writer.writerow({'Name': name,
                                 'CompanyName': company,
                                 'FirstName': None,
                                 'LastName': None,
                                 'Company': None,
                                 'Role': None,
                                 'LinkedIn Url': e,
                                 'check': None,
                                 'G_Search': G_Search
                                 })
            continue
#Matching=pd.read_csv("C:\\Users\\inragy00\\PycharmProjects\\pythonProject\\Test_C_Output.csv",sheet_name="Test_C_Output",na_filter=False)
Matching=pd.read_csv("C:\\Users\\inragy00\\PycharmProjects\\pythonProject\\Test_C_Output.csv")
df=Matching.copy()
df.head(3)
import Levenshtein as lv
df['Company'][0]
#lv.ratio(df['CompanyName'][0],df['Company'][0])
lv.ratio(str(df['CompanyName'][0]),str(df['Company'][0]))
df.dtypes
df['First_Company_Name'] = df['CompanyName'].str[0]
df['First_Company_Linkedin'] = df['Company'].str[0]
df['Company'][0]
if not df['Company'][0]:
    print ("Empty")
else:
    print ("Comparison Made Successfully")
Percentage=[]
FirstLetterMatch=[]
for i in range(0,len(df)):
    Percentage.append(lv.ratio(str(df['CompanyName'][i]).lower(),str(df['Company'][i]).lower()))
    if not df['Company'][i]:
        FirstLetterMatch.append('NotApplicable')
    else:
        FCN = str(df['First_Company_Name'][i]).lower()
        FCL = str(df['First_Company_Linkedin'][i]).lower()
        FirstLetterMatch.append(list(
    map(lambda x: x.startswith(FCN), FCL)))
df['Percentage']=Percentage
df['FirstLetterMatch']=FirstLetterMatch
df.head(5)
df.to_excel("C:\\Users\\inragy00\\PycharmProjects\\pythonProject\\Test_C_Output.xlsx",sheet_name="Sheet1",index=False)
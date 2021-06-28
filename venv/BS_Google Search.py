import csv
import os
from selenium import webdriver
from bs4 import BeautifulSoup
from random import randint
from time import sleep


if not os.path.exists(r'Missing_Result.csv'):
    with open('Missing_Result.csv', 'a+', newline="") as file:
        headers = ['Name', 'CompanyName', 'FirstName', 'LastName', 'Company', 'Role', 'LinkedIn Url','check']
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()

driver = webdriver.Chrome(executable_path=r'C:\Users\inragy00\Downloads\chromedriver.exe')

with open('Missing.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)
    for col in reader:
        try:
            company = col[1].strip()
            name = col[0].strip()
            print(col[0], col[1])
            firstname = name.split(" ")[0].lower()
            lastname = name.split(" ")[-1].lower()
            sleep(randint(10, 60))
            driver.get("https://www.google.com/search?q=" + name + "+" + company + "")
            html = driver.page_source
            soup = BeautifulSoup(html, 'html.parser')

            companyrole = soup.find("div", {"class": "fG8Fp uo4vr"})
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
                if missing_parent:
                    print(cfirstname, clastname)
                    data = companyrole.get_text()
                    refine_text = data.split(" · ")
                    role, companyname = refine_text[1], refine_text[2]
                    print('Role: {}\nCurrent Company: {}'.format(role, companyname))
                    link = validator.find("a", href=True)
                    print(link['href'])
                    linkedurl = link['href']
                    with open('Missing_Result.csv', 'a+', newline="", encoding='utf-8') as file:
                        headers = ['Name',
                                   'CompanyName',
                                   'FirstName',
                                   'LastName',
                                   'Company',
                                   'Role',
                                   'LinkedIn Url',
                                   'check'
                                   ]
                        writer = csv.DictWriter(file, fieldnames=headers)
                        writer.writerow({'Name': name,
                                         'CompanyName': company,
                                         'FirstName': cfirstname.capitalize(),
                                         'LastName': clastname.capitalize(),
                                         'Company': companyname,
                                         'Role': role,
                                         'LinkedIn Url': linkedurl,
                                         'check':mis_text

                                         })

            else:
                print('No Linkedin found!')
                with open('Missing_Result.csv', 'a+', newline="", encoding='utf-8') as file:
                    headers = ['Name',
                               'CompanyName',
                               'FirstName',
                               'LastName',
                               'Company',
                               'Role',
                               'LinkedIn Url',
                               'check'
                               ]
                    writer = csv.DictWriter(file, fieldnames=headers)
                    writer.writerow({'Name': name,
                                     'CompanyName': company,
                                     'FirstName': None,
                                     'LastName': None,
                                     'Company': None,
                                     'Role': None,
                                     'LinkedIn Url': "Linked Not Found!",
                                     'check':None

                                   })
        except Exception as e:
            print('exception handled----->',e)
            with open('Missing_Result.csv', 'a+', newline="", encoding='utf-8') as file:
                headers = ['Name',
                           'CompanyName',
                           'FirstName',
                           'LastName',
                           'Company',
                           'Role',
                           'LinkedIn Url',
                           'check'
                           ]
                writer = csv.DictWriter(file, fieldnames=headers)
                writer.writerow({'Name': name,
                                 'CompanyName': company,
                                 'FirstName': None,
                                 'LastName': None,
                                 'Company': None,
                                 'Role': None,
                                 'LinkedIn Url': e,
                                 'check': None
                                 })
            continue
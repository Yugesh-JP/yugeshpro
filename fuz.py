#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


Matching=pd.read_excel("C:\\Users\\inragy00\\Desktop\\EMEA DAAS 859.xlsx",sheet_name="Sheet1",na_filter=False)


# In[3]:


df=Matching.copy()


# In[4]:


df.head(3)


# In[ ]:


import Levenshtein as lv


# In[12]:


df['CompanyName_Linkedin'][0]


# In[ ]:


lv.ratio(df['Final Company Name'][0],df['CompanyName_Linkedin'][0])


# In[ ]:


df.dtypes


# In[3]:


df['First_Company_Name'] = df['Final Company Name'].str[0]


# In[303]:


df['First_Company_Linkedin'] = df['CompanyName_Linkedin'].str[0]


# In[304]:


df['CompanyName_Linkedin'][0]


# In[305]:


if not df['CompanyName_Linkedin'][0]:
    print ("Empty")
else:
    print ("Not Empty")


# In[310]:


Percentage=[]
FirstLetterMatch=[]
for i in range(0,len(df)):
    Percentage.append(lv.ratio(str(df['Final Company Name'][i]).lower(),str(df['CompanyName_Linkedin'][i]).lower()))
    if not df['CompanyName_Linkedin'][i]:
        FirstLetterMatch.append('NotApplicable')
    else:
        FCN = str(df['First_Company_Name'][i]).lower()
        FCL = str(df['First_Company_Linkedin'][i]).lower()
        FirstLetterMatch.append(list(
    map(lambda x: x.startswith(FCN), FCL)))
df['Percentage']=Percentage
df['FirstLetterMatch']=FirstLetterMatch


# In[311]:


df.head(5)


# In[313]:


df.to_excel("C:\\Users\\inragy00\\Desktop\\EMEA DAAS 859.xlsx",sheet_name="Sheet2",index=False)





# from fuzzywuzzy import fuzz
# Str1 = "Ubistor"
# Str2 = "UbiStor, Inc."
# Ratio = fuzz.ratio(Str1.lower(),Str2.lower())
# Partial_Ratio = fuzz.partial_ratio(Str1.lower(),Str2.lower())
# Token_Sort_Ratio = fuzz.token_sort_ratio(Str1,Str2)
# Token_Set_Ratio = fuzz.token_set_ratio(Str1,Str2)
# print(Ratio)
# print(Partial_Ratio)
# print(Token_Sort_Ratio)
# print(Token_Set_Ratio)
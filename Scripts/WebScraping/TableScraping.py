#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import requests as rqst
from bs4 import BeautifulSoup as bs


# # Scraping on First Sample

# In[31]:


tabScript = """<table class="type 1 table">
    <tr>
      <th>Month</th>
      <th>Savings</th>
    </tr>
    <tr>
      <td>March</td>
      <td>$400</td>
    </tr>
    <tr>
      <td>April</td>
      <td>$300</td>
    </tr>
  </table>
  <table class="type 2 table">
    <thead>
        <tr>
            <th>Month</th>
            <th>Savings</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>January</td>
            <td>$100</td>
        </tr>
        <tr>
            <td>February</td>
            <td>$200</td>
        </tr>
    </tbody>
  </table>"""


# In[33]:


soup = bs(tabScript,"html.parser")


# In[34]:


myTable = soup.find('table',{'class':"type 1 table"})
myTable


# In[38]:


row_headers = []
for x in myTable.find_all('tr'):
    for y in x.find_all('th'):
        row_headers.append(y.text)
row_headers


# In[44]:


tableValues = []
for x in myTable.find_all('tr')[1:]:
    td_tags = x.find_all('td')
    td_val = [y.text for y in td_tags]
    tableValues.append(td_val)
tableValues


# In[45]:


pd.DataFrame(tableValues,columns=row_headers)


# # Scraping on second sample

# In[47]:


web = rqst.get("https://fastestlaps.com/tracks/adm-miachkovo")

soup = bs(web.content,"html.parser")


# In[48]:


tableHead = soup.thead
tableHead


# In[49]:


row_headers = []
for x in tableHead.find_all('tr'):
    for y in x.find_all('th'):
        row_headers.append(y.text)
row_headers


# In[50]:


tableBody = soup.tbody
tableBody


# In[51]:


tableValues = []
for x in tableBody.find_all('tr')[1:]:
    td_tags = x.find_all('td')
    td_val = [y.text for y in td_tags]
    tableValues.append(td_val)
tableValues


# In[53]:


df = pd.DataFrame(tableValues,columns=row_headers)
df.to_excel(r"D:\Learnerea\Tables\tabledata.xlsx",index=False)


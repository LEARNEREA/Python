#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import requests as rqst
from bs4 import BeautifulSoup as bs


# In[2]:


web = rqst.get("https://books.toscrape.com/")


# In[3]:


web.status_code


# In[4]:


soup = bs(web.content,"html.parser")
print(soup.prettify())


# In[7]:


soup.h3.a['title']


# In[9]:


book_lists = []

for x in soup.find_all('h3'):
    book_lists.append(x.a['title'])
book_lists


# In[13]:


soup.article.p['class']


# In[14]:


ratings = []
for x in soup.find_all("article"):
    ratings.append(x.p['class'][1])
ratings


# In[15]:


price=[]

for x in soup.find_all('p',{'class':"price_color"}):
    price.append(x.get_text())
price


# In[17]:


data = {'books_list':book_lists,'ratings':ratings,'prices':price}

book_data = pd.DataFrame(data)
book_data.to_excel(r"D:\Learnerea\Tables\book_lists_part2.xlsx",index=False)


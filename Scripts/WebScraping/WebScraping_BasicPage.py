#!/usr/bin/env python
# coding: utf-8

# In[2]:


# pip install beautifulsoup4
# pip install requests
# pip install webbrowser
# pip install selenium


# In[85]:


import requests as rqst
import webbrowser as wb
from bs4 import BeautifulSoup as bs
import selenium as sl

import pandas as pd


# In[24]:


testPage = """<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>"""


# In[103]:


soup = bs(testPage,'html.parser')
soup


# In[108]:


soup.html.head.title.text


# In[112]:


title = soup.title.text
title


# In[121]:


paragraphs = []

for para in soup.find_all('p'):
    paragraphs.append(para.text)
paragraphs


# In[127]:


url = []

for link in soup.find_all('a'):
    url.append(link.get("href"))
url


# In[129]:


data = {'paragraphs':paragraphs,'url':url}
data


# In[140]:


story  = pd.DataFrame(data)
story['title'] = title
story.sort_index(axis=1)


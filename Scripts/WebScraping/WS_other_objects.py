#!/usr/bin/env python
# coding: utf-8

# In[2]:


# pip install beautifulsoup4
# pip install requests
# pip install webbrowser
# pip install selenium


# In[3]:


import requests as rqst
import webbrowser as wb
from bs4 import BeautifulSoup as bs
import selenium as sl

import pandas as pd


# In[51]:


testPage = """<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p><!-- Check out the Learnerea --></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>"""


# In[62]:


soup = bs(testPage,'html.parser')
soup


# <html><head><title>The Dormouse's story</title></head>
# <body>
# <p class="title"><b>The Dormouse's story</b></p>
# <p><!-- Check out the Learnerea --></p>
# <p class="story">Once upon a time there were three little sisters; and their names were
# <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
# <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a> and
# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>;
# and they lived at the bottom of a well.</p>
# <p class="story">...</p></body></html>

# # NavigableString

# # BeautifulSoup

# # Comments

# In[ ]:





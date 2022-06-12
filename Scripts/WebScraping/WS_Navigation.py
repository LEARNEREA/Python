#!/usr/bin/env python
# coding: utf-8

# In[115]:


import requests as rqst
from bs4 import BeautifulSoup as bs


# <html>
#     <head>
#         <b>
#             Welcome to Learnerea
#         </b>
#      </head>
#     <p>
#         Here you gonna get all kind of technical support and also you can provide the support
#     </p>
#     <div>
#         this is the div tag
#     </div>
#     <p>
#         The support will always be free of cost and the supporters are volunteers
#         <a href="https://www.youtube.com/channel/UCArCI8B7Vlls-HNH-UqW68A/featured" id="link1">
#             click here to check out the channel
#         </a>,
#         <a href="https://youtu.be/zX-zPfwv6c8" id="link1">
#             some of the most popular videos
#         </a> 
#     </p>
# </html>

# In[116]:


myPage = """<html>
    <head>
        <b>
            Welcome to Learnerea
        </b>
     </head>
    <p>
        Here you gonna get all kind of technical support and also you can provide the support
    </p>
    <div>
        this is the div tag
    </div>
    <p>
        The support will always be free of cost and the supporters are volunteers
        <a href="https://www.youtube.com/channel/UCArCI8B7Vlls-HNH-UqW68A/featured" id="link1">
            click here to check out the channel
        </a>,
        <a href="https://youtu.be/zX-zPfwv6c8" id="link1">
            some of the most popular videos
        </a> 
    </p>
</html>"""


# In[119]:


soup = bs(myPage,'html.parser')
soup


# In[131]:


soup.html.p.next_sibling.next_sibling.next_sibling.next_sibling.a.next_sibling.next_sibling['href']


# In[142]:


list(soup.a.parent.strings)[0]


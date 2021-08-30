#!/usr/bin/env python
# coding: utf-8

# In[115]:


import pandas as pd


# In[117]:


os.getcwd()


# In[2]:


pd.set_option('display.max_columns',None)


# In[11]:


mart = pd.read_excel("D:/Learnerea/Tables/supermarket_sales_data.xlsx")
custMast = mart[['Invoice ID','City','Customer type','Gender','Rating']]
tran = mart[['Invoice ID','Date','Time','Product line', 'Unit price', 'Quantity','Total','cogs']]


# In[103]:


custSample1 = custMast.loc[0:4]
custSample2 = custMast.loc[5:9].reset_index(drop=True)
custSample3 = custMast.loc[10:14].reset_index(drop=True)
tranSample1 = tran.loc[3:7]


# In[105]:


custSample1


# In[107]:


custSample2


# In[109]:


custSample3


# In[112]:


custSample = pd.concat([custSample1,custSample2,custSample3],ignore_index=True)
custSample


# In[114]:


appending = custSample1.append([custSample2,custSample3],ignore_index=True)
appending


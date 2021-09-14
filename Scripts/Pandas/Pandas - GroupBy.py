#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[5]:


pd.set_option("display.max_columns",None)
# pd.set_option("display.max_rows",None)


# In[26]:


df = pd.read_excel("D:/Learnerea/Tables/supermarket_sales_data.xlsx")
df.head()


# In[40]:


df.groupby(["Gender","Payment"]).count()['Quantity']


# In[49]:


df.groupby(["Gender","Payment"]).agg(["count","sum","min","max","mean"])["Quantity"]


# In[51]:


df.groupby(["Gender","Payment"]).agg({"Quantity":["count","sum","min","max","mean"],"cogs":["sum"],"gross income":["sum"],"Rating":["mean"]})


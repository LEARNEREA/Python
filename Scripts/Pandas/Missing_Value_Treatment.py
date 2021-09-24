#!/usr/bin/env python
# coding: utf-8

# In[38]:


import pandas as pd


# In[121]:


df = pd.read_excel("D:/Learnerea/Tables/DropNaSample.xlsx",sheet_name="fillna")
greet = pd.read_excel("D:/Learnerea/Tables/DropNaSample.xlsx",sheet_name="axis_fillna")


# In[65]:


df.fillna({"Gender":df["Gender"].mode()[0],
          "Unit price":df["Unit price"].mean(),
          "Quantity":df["Quantity"].median(),
          "Total":df["Total"].min()})


# In[78]:


greet.fillna('xyz',limit=2)


# In[87]:


df.set_index("Date").interpolate("time")


# In[124]:


df["Gender"]=df["Gender"].fillna(df["Gender"].mode()[0])
df


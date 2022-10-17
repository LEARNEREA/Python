#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[29]:


df = pd.read_excel(r'D:\Learnerea\Tables\dup_columns.xlsx')
df


# In[19]:


df.iloc[:,1]


# In[23]:


dup_cols = set()

for x in range(df.shape[1]):
    base_col  = df.iloc[:,x]
    for y in range(x+1,df.shape[1]):
        comp_col = df.iloc[:,y]
        
        if base_col.equals(comp_col):
            dup_cols.add(df.columns.values[y])
        
#         print(df.columns.values[x],df.columns.values[y])


# In[28]:


df.drop(labels=dup_cols,axis=1)


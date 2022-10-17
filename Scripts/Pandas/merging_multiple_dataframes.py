#!/usr/bin/env python
# coding: utf-8

# In[22]:


import pandas as pd
import numpy as np
# from faker import Faker


# In[87]:


emp = pd.read_excel(r'D:\Learnerea\Tables\org_details.xlsx',sheet_name='emp')
sal = pd.read_excel(r'D:\Learnerea\Tables\org_details.xlsx',sheet_name='salary')
contacts = pd.read_excel(r'D:\Learnerea\Tables\org_details.xlsx',sheet_name='contacts')


# In[121]:


emp


# In[122]:


sal


# In[88]:


print('shape of emp datafrmae: ', emp.shape)
print('shpae of sal dataframe: ', sal.shape)
print('shpae of contacts dataframe: ', sal.shape)


# ### 1. How to Merge Multiple or More than two DataFrames
# ### 2. How to Merge with "Where" Condition

# In[89]:


emp.head(3)


# In[90]:


sal.head(3)


# In[95]:


contacts


# In[111]:


all_merged = pd.merge(emp, sal, left_on=['ID','Name'],right_on=['emp_id','Name'],how='inner').merge(contacts.query("Name in ('Donald Johnson','Crystal Flores')")
                                                                                       ,on=['emp_id','Name'],how='left')
all_merged


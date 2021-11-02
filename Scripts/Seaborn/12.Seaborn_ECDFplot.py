#!/usr/bin/env python
# coding: utf-8

# In[182]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statistics as sts

pd.set_option('display.max_rows',None)


# In[212]:


mart = pd.read_excel(r"D:\Learnerea\Tables\supermarket_sales.xlsx")
mart = mart[['Gender','Payment','Unit price','Quantity','Total','gross income']]
mart.head()


# In[219]:


sns.ecdfplot(data=mart,y='gross income',hue='Gender',stat='count')


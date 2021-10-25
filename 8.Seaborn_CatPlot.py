#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


mart = pd.read_excel("D:/Learnerea/Tables/supermarket_sales.xlsx")
mart.head()


# In[57]:


p=sns.catplot(data=mart,x='Payment',y='Total',col='Gender',kind='box',row='Customer type',palette='CMRmap_r')
# p.set_titles(col_template="{col_name}")


#!/usr/bin/env python
# coding: utf-8

# In[58]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


# In[12]:


mart = pd.read_excel(r'D:\Learnerea\Tables\mart_linePlot.xlsx')
mart.columns = mart.columns.str.lower()
mart.head(10)


# In[61]:


martPiv = mart.pivot_table(index='outlet_year',columns='outlet_size',values='sales')
martPiv


# In[66]:


sns.set_style('white')
plt.figure(figsize=(5,5))

sns.heatmap(martPiv
#            ,square=True
           ,annot=True
           ,fmt='.0f'
           ,annot_kws=dict(size=15,weight='bold')
           ,linewidths=0.5
           ,linecolor='black'
           ,cmap='OrRd_r')


# In[68]:


sns.heatmap(mart.corr()
           ,vmin=-1
           ,vmax=1
           ,center=0
           ,cmap='OrRd_r'
           ,annot=True
           ,fmt='.1f'
           ,annot_kws=dict(size=15,weight='bold')
           ,linecolor='black'
           ,linewidths=0.5)


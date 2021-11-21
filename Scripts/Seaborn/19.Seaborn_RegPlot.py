#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


tips = sns.load_dataset('tips')
tips.head()


# **1. Creat a basic reg plot**

# In[23]:


sns.regplot(data=tips,x='total_bill',y='tip')


# **2. Change the styling of reg plot, only line, only scatter, show/hide the ci, change the ci value, change n_boot**

# In[38]:


sns.regplot(data=tips,x='total_bill',y='tip'
#            ,color='red'
#            ,marker='+'
           ,line_kws=dict(color='red',linestyle='--')
           ,scatter_kws=dict(s=100,color='green',alpha=0.5)
           ,ci=60
           ,n_boot=500)


# **3. Discuss aobut the statistical models in seaborn**

# In[39]:


sns.regplot(data=tips,x='total_bill',y='tip')


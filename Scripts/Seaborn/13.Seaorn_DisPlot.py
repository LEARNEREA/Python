#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[57]:


mart = pd.read_excel(r"D:\Learnerea\Tables\supermarket_sales.xlsx")
mart = mart[['Gender','Payment','Unit price','Quantity','Total','gross income','Branch']]
mart.head()


# In[60]:


sns.displot(data=mart,y='Total',kde=True,rug=True,rug_kws={'height':0.05},hue='Payment',multiple='stack',col='Branch',row='Gender')


# In[62]:


sns.displot(data=mart,y='Total',kind='ecdf',hue='Payment',col='Branch',row='Gender')


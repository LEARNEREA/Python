#!/usr/bin/env python
# coding: utf-8

# In[60]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[61]:


mart = pd.read_excel(r'D:\Learnerea\Tables\mart_linePlot.xlsx').sample(n=50)
mart.columns=mart.columns.str.lower()
mart.head()


# In[76]:


mart.to_excel(r'D:\Learnerea\Tables\mart_relPlot.xlsx',index=False)


# In[75]:


sns.relplot(data=mart,x='outlet_year',y='sales',s=100,hue='outlet_size'
#            ,col='outlet_size'
#            ,row='tier'
#            ,hue='outlet_size'
           ,palette=['green','red','yellow'])


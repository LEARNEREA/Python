#!/usr/bin/env python
# coding: utf-8

# In[95]:


import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt


# In[135]:


mart = pd.read_excel(r'D:\Learnerea\Tables\mart_linePlot.xlsx')
mart.columns = mart.columns.str.lower()
mart.head()


# In[125]:


mart.outlet_size.unique()


# In[136]:


mart.outlet_location_type.unique()


# In[142]:


learnerea=sns.FacetGrid(mart,col='outlet_size')
learnerea.map_dataframe(sns.scatterplot,x='outlet_year',y='sales',hue='outlet_location_type'
                       ,marker='+'
                       ,alpha=0.5
                       ,color='red'
                       ,s=100)


# In[152]:


learnerea=sns.FacetGrid(mart,col='outlet_size',row='outlet_location_type',sharey=False,ylim=(0,1000))
learnerea.map_dataframe(sns.histplot,x='sales')
learnerea.set_axis_labels('sales','count')
learnerea.set_titles(col_template='{col_name} Size',row_template='{row_name} Type')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





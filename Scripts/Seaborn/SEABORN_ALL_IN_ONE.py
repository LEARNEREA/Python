#!/usr/bin/env python
# coding: utf-8

# **Import all the required libraries**

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# **Import the relevant DataFrames**

# In[280]:


tips = sns.load_dataset('tips')
flights = sns.load_dataset('flights')
mart = pd.read_excel(r'D:\Learnerea\Tables\mart_linePlot.xlsx')
mart.columns = mart.columns.str.lower()
tips.head(10)


# In[357]:


sns.set_style('white')


# In[281]:


flights.head(10)


# In[333]:


tips.columns


# **1. COUNT PLOT**

# In[282]:


sns.countplot(data=mart,x='outlet_size')


# **2. BAR PLOT**

# In[285]:


sns.barplot(data=mart,x='outlet_size',y='sales')


# **3. BOX PLOT**

# In[298]:


plt.figure(figsize=(6,5))
sns.boxplot(data=mart,x='outlet_size',y='sales',showmeans=True,meanprops=dict(markerfacecolor='white',markersize=15))


# **4. VIOLIN PLOT**

# In[299]:


sns.violinplot(data=mart,x='outlet_size',y='sales')


# **5. STRIP PLOT**

# In[307]:


sns.stripplot(data=mart.sample(500),x='outlet_size',y='sales',jitter=.08)


# **6. SWARM PLOT**

# In[358]:


sns.set_style('white')
sns.swarmplot(data=mart.sample(500),x='outlet_size',y='sales')


# **7. CATEGORICAL or CAT PLOT**

# In[356]:


sns.set_style('white')
sns.catplot(data=mart,x='outlet_size',y='sales',kind='violin')


# **8. HISTOGRAM PLOT or HIST PLOT**

# In[314]:


sns.histplot(data=mart,x='sales',bins=np.arange(0,11000,2000))


# **9. KDE PLOT or KERNAL DENSITY ESTIMATION PLOT**

# In[359]:


sns.set_style('white')
sns.kdeplot(data=mart,x='sales')


# **10. RUG PLOT**

# In[316]:


sns.rugplot(data=mart,x='sales')


# **11. ECDF or Empirical Cumulative Distribution Funcitons PLOT**

# In[317]:


sns.ecdfplot(data=mart,x='sales')


# **12. Distribution or DIST PLOT**

# In[323]:


sns.displot(data=mart,x='sales',rug=True,kde=True)


# **13. JOINT PLOT**

# In[325]:


sns.jointplot(data=mart.sample(500),x='sales',y='item_mrp')


# **14. PAIRT PLOT**

# In[328]:


sns.pairplot(data=mart.sample(500),kind='reg')


# **15. SCATTER PLOT**

# In[334]:


sns.scatterplot(data=tips,x='total_bill',y='tip')


# **16. LINE PLOT**

# In[341]:


sns.lineplot(data=mart,x='outlet_year',y='sales',ci=None,color='red')


# **17. REL or Relational PLOT**

# In[346]:


sns.relplot(data=flights,x='year',y='passengers')
# flights.columns


# **18. REG or Regression PLOT**

# In[347]:


sns.regplot(data=tips,x='total_bill',y='tip')


# **19. HEATMAP PLOT**

# In[191]:


mart_piv=mart.pivot_table(index='outlet_year',columns='outlet_size',values='sales')


# In[349]:


sns.heatmap(data=mart_piv,annot=True,fmt='.0f')


# **20. CLUSTERMAP PLOT**

# In[351]:


sns.clustermap(data=mart_piv,annot=True,fmt='.0f')


# **21. FacetGrid PLOT**

# In[354]:


learnerea=sns.FacetGrid(data=mart,col='outlet_size',row='tier')
learnerea.map_dataframe(sns.histplot,x='sales')


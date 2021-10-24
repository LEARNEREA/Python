#!/usr/bin/env python
# coding: utf-8

# **1. Import all the required libraries**

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# **2. Import the supermarket sales data excel file**

# In[37]:


mart = pd.read_excel(r'D:\Learnerea\Tables\supermarket_sales.xlsx')
mart.head()


# **3. Create a basic SWARM PLOT on Total column**

# In[38]:


sns.swarmplot(data=mart,y='Total')


# **4. Create SWARM PLOT group by CATEGORIES**

# In[40]:


sns.swarmplot(data=mart,y='Total',x='Payment',hue='Gender')


# **5. Showing Hues Separatly on the categorical axis**

# In[63]:


plt.figure(figsize=(15,5))
sns.swarmplot(data=mart,y='Total',x='Payment',hue='Gender',split=True)


# **6. Styling a SWARM - Change the marker, size, color, edge color.....**

# In[55]:


plt.figure(figsize=(15,5))
sns.swarmplot(data=mart,y='Total',x='Payment',size=10,color='green',edgecolor='black')


# **7. Overlay a SWARM PLOT on a BOX PLOT**

# In[57]:


sns.boxplot(data=mart,y='Total',x='Payment')
sns.swarmplot(data=mart,y='Total',x='Payment',color='black')


# **8. Overlay a SWARM PLOT on a VIOLIN PLOT**

# In[62]:


sns.violinplot(data=mart,y='Total',x='Payment',inner=None,width=1)
sns.swarmplot(data=mart,y='Total',x='Payment',color='white')


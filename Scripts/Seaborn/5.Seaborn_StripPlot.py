#!/usr/bin/env python
# coding: utf-8

# **1. Import all the required libraries**

# In[61]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# **2. Import the supermart data excel file**

# In[74]:


mart = pd.read_excel("D:/Learnerea/Tables/supermarket_sales.xlsx")
mart.head()


# **3. Create a basic STRIP PLOT**

# In[160]:


sns.stripplot(data=mart, y='Total')


# **4. Expand markers in STRIP PLOT using jitter**

# In[138]:


sns.stripplot(data=mart, y='Total',jitter=0.2)


# **5. Draw line around the points using LINEWIDTH**

# In[141]:


sns.stripplot(data=mart, y='Total',linewidth=0.2)


# **6. Include third categorical variable with HUE**

# In[145]:


sns.stripplot(data=mart, y='Total',x='Payment',hue='Gender',jitter=0.2,linewidth=0.5)


# **7. Separate each level of hue using DODGE**

# In[146]:


sns.stripplot(data=mart, y='Total',x='Payment',hue='Gender',jitter=0.2,linewidth=0.5,dodge=True)


# **8. Draw the strips on top of VIOLIN PLOT**

# In[157]:


sns.stripplot(data=mart, y='Total',x='Payment',jitter=0.1)
sns.violinplot(data=mart, y='Total',x='Payment',color='gray')


# **9. Draw the strips on top of BOX PLOT**

# In[158]:


sns.stripplot(data=mart, y='Total',x='Payment',color="black")
sns.boxplot(data=mart, y='Total',x='Payment',color='gray')


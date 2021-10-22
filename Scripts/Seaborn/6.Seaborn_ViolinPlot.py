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


# **3. Create a basic VIOLINPLOT**

# In[76]:


sns.violinplot(y="Total",data=mart)


# **4. Create a VIOLINPLOT on two categorical and one numeric variable and use split**

# In[79]:


sns.violinplot(x='Payment',y='Total',hue='Gender',data=mart,split=True)


# **5. Change the box in the VIOLINPLOT to horzontal lines**

# In[81]:


sns.violinplot(x='Payment',y='Total',hue='Gender',data=mart,split=True,inner='quartile')


# **6. Draw line for each observations in a VIOLINPLOT**

# In[82]:


sns.violinplot(x='Payment',y='Total',hue='Gender',data=mart,split=True,inner='stick')


# **7. Change the amount of smoothing using bw attribute**

# In[84]:


sns.violinplot(x='Payment',y='Total',hue='Gender',data=mart,split=True,inner='quartile',bw=.2)


# **8. Cut out the extreme values**

# In[85]:


sns.violinplot(x='Payment',y='Total',hue='Gender',data=mart,split=True,inner='quartile',bw=.2,cut=0)


#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statistics as sts

pd.set_option('display.max_rows',None)


# In[2]:


mart = pd.read_excel(r"D:\Learnerea\Tables\supermarket_sales.xlsx")
mart = mart[['Gender','Payment','Unit price','Quantity','Total','gross income']]
mart.head(10)


# **1. Create a basic HISTOGRAM on X or Y axis**

# In[26]:


sns.histplot(data=mart,y='Total')


# **2. Change the Bins Width using binwidth arguement**

# In[29]:


sns.histplot(data=mart,x='Total',binwidth=150)


# **3. Change Number of Bins and Interval**

# In[35]:


plt.figure(figsize=(15,5))
sns.histplot(data=mart,x='Total',bins=np.arange(0,1100,50))
plt.xticks(np.arange(0,1100,50))


# **4. Combine with KDE**

# In[38]:


sns.histplot(data=mart,x='Total',kde=True)


# **5. Use a categorical variable in HUE and STACK it using MULTIPLE agruement**

# In[40]:


sns.histplot(data=mart,x='Total',hue='Payment',multiple='stack')


# **6. Make it a step/poly plot using ELEMENT arguement and change the FILL**

# In[45]:


sns.histplot(data=mart,x='Total',hue='Payment',element='poly')


# **7. Use categorical variable and shrink it**

# In[50]:


sns.histplot(data=mart,x='Total',stat='probability')


# **8. Create a Bivariate Histogram**

# In[51]:


sns.histplot(data=mart,x='Total',y='gross income')


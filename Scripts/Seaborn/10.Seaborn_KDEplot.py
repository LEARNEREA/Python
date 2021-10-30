#!/usr/bin/env python
# coding: utf-8

# In[68]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statistics as sts

pd.set_option('display.max_rows',None)


# In[69]:


mart = pd.read_excel(r"D:\Learnerea\Tables\supermarket_sales.xlsx")
mart = mart[['Gender','Payment','Unit price','Quantity','Total','gross income']]
mart.head(10)


# **1. Create a basic KDE plot for Total column**

# In[70]:


sns.kdeplot(data=mart, x='Total')


# **2. Create KDE for all the numeric variables in dataframe**

# In[71]:


sns.kdeplot(data=mart)


# **3. Adjust the smooting using bw_adjust**

# In[74]:


sns.kdeplot(data=mart,x='Total',bw_adjust=0.5)


# **4. Group the KDE on a category variable**

# In[75]:


sns.kdeplot(data=mart,x='Total',hue='Payment')


# **5. Stack KDE on a category using MULTIPLE arguement**

# In[76]:


sns.kdeplot(data=mart,x='Total',hue='Payment',multiple='stack')


# **6. Use log scaling to map the variable in KDE**

# In[78]:


sns.kdeplot(data=mart,x='Total',log_scale=True)


# **7. Change styling of hued KDE using linewidth, palette, alpha etc....**

# In[84]:


sns.kdeplot(data=mart,x='Total',hue='Payment',multiple='stack',linewidth=5,palette='Dark2',alpha=0.5)


# **8. Creat a bivariate KDE**

# In[85]:


sns.kdeplot(data=mart, x='Unit price',y='gross income')


# **9. Group the bivariate KDE on a categorical variable and show the contours**

# In[90]:


sns.kdeplot(data=mart, x='Unit price',y='gross income',hue='Gender',fill=True,levels=5,thresh=0.2)


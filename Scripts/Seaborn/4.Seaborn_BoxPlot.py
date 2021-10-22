#!/usr/bin/env python
# coding: utf-8

# **1. Import all the required LIBRARIES**

# In[24]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# **2. Import MART dataframe**

# In[25]:


mart = pd.read_excel("D:/Learnerea/Tables/supermarket_sales.xlsx")
mart.head()


# **3. Create a basic BOX plot on one NUMERIC variable**

# In[29]:


sns.boxplot(y='Total',data=mart, width=0.2)


# **4. Create a basic BOX plot on one numeric variable by a CATEGORICAL variable**

# In[30]:


sns.boxplot(x='Payment',y='Total',data=mart)


# **5. Create a basic BOX plot on one numeric variable by TWO CATEGORICAL variable using HUE attribute**

# In[31]:


sns.boxplot(x='Payment',y='Total',hue='Gender',data=mart)


# **6. Add MEAN marker in the box plot using Showmeans attribute and change its style using meanprops**

# In[34]:


sns.boxplot(x='Payment',y='Total',hue='Gender',data=mart,showmeans=True,meanprops={"marker":"o"
                                                                                  ,"markerfacecolor":"white"
                                                                                  ,"markersize":"10"
                                                                                  ,"markeredgecolor":"black"})


# **7. Make HORIZONTAL box plot**

# In[35]:


sns.boxplot(x='Total',y='Payment',hue='Gender',data=mart,showmeans=True,meanprops={"marker":"o"
                                                                                  ,"markerfacecolor":"white"
                                                                                  ,"markersize":"5"
                                                                                  ,"markeredgecolor":"black"})


# **8. Change PALETTE, LINE WIDTH etc..**

# In[41]:


sns.boxplot(x='Total',y='Payment',hue='Gender',data=mart,showmeans=True,meanprops={"marker":"o"
                                                                                  ,"markerfacecolor":"white"
                                                                                  ,"markersize":"5"
                                                                                  ,"markeredgecolor":"black"}
           ,palette='CMRmap'
           ,linewidth=5)


# **9. Create box plot for EACH OF THE NUMERIC VARIABLE in the dataframe**

# In[43]:


plt.figure(figsize=(15,5))

sns.boxplot(data=mart)


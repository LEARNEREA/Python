#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[4]:


mart = pd.read_csv(r'D:\Learnerea\Tables\train.csv')
mart[['Tier']]=mart['Outlet_Location_Type'].str.split(expand=True)[1]
mart.head()


# **1. Creat a basic line plot and try different estimators**

# In[336]:


#---Estimator = None"
# height = [5, 5, 7, 5, 8]
# age    = [22,42,30,35,40]
# sns.lineplot(x=age,y=height,estimator=None)

#---Estimator = sum
height = [5, 6, 7, 6.5,4]
age    = [22,25,30,25,25]
sns.lineplot(x=age,y=height,estimator=sum)


# In[334]:


sns.lineplot(data=mart,x="Outlet_Year",y="Sales",ci=None,estimator=None)


# **2. Test with different Confidence Intervals and with different number of Bootstraping**

# In[342]:


sns.lineplot(data=mart,x="Outlet_Year",y="Sales",n_boot=2)


# **3. Grouping using HUE and use different Palettes**

# In[347]:


sns.lineplot(data=mart,x="Outlet_Year",y="Sales",ci=None
             ,hue='Outlet_Size'
            ,palette=['red','green','blue'])


# **4. Grouping using Style, use different Marker and Dashes**

# In[350]:


sns.lineplot(data=mart,x="Outlet_Year",y="Sales",ci=None
             ,style='Outlet_Size'
            ,markers=True
            ,dashes=False)


# **5. Grouping using Size**

# In[353]:


sns.lineplot(data=mart,x="Outlet_Year",y="Sales",ci=None
            ,size='Outlet_Size'
            ,sizes=(.5,5))


# **6. Use different semantic styling parameters on same or different variables**

# In[360]:


sns.lineplot(data=mart,x="Outlet_Year",y="Sales",ci=None
            ,hue='Outlet_Size'
#             ,style='Outlet_Size'
#             ,markers=True
             ,size='Tier'
            )


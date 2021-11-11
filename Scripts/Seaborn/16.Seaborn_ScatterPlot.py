#!/usr/bin/env python
# coding: utf-8

# In[195]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[239]:


mart = pd.read_csv(r'D:\Learnerea\Tables\train.csv').sample(50)
mart[['Tier']]=mart['Outlet_Location_Type'].str.split(expand=True)[1]
mart.to_excel(r'D:\Learnerea\Tables\mart_train_sample.xlsx',index=False)


# **1. Create a basic SCATTER PLOT**

# In[216]:


sns.scatterplot(data=mart,x='Item_MRP',y='Sales')


# **2. Grouping basis on a categorical variable using HUE**

# In[217]:


sns.scatterplot(data=mart,x='Item_MRP',y='Sales',hue='Outlet_Size')


# **3. Grouping basis on a categorical variable using STYLE and Styling Markers as well**

# In[219]:


sns.scatterplot(data=mart,x='Item_MRP',y='Sales',style='Outlet_Size'
                ,markers={"High":"^","Small":"v","Medium":"o"})


# **4. Grouping basis on a categorical variable using HUE & STYLE both together**

# In[237]:


sns.scatterplot(data=mart,x='Item_MRP',y='Sales',style='Outlet_Size'
                ,hue='Outlet_Size'
                ,s=200
                ,markers={"High":"^","Small":"v","Medium":"o"})


# **5. Grouping basis on numeric variable using HUE and use PALETTE**

# In[226]:


sns.scatterplot(data=mart,x='Item_MRP',y='Sales'
#                 ,style='Outlet_Size'
                ,hue='Outlet_Size'
                ,palette='Purples_r'
                ,markers={"High":"^","Small":"v","Medium":"o"})


# **6. Grouping basis on a numeric variable using HUE & SIZE**

# In[231]:


sns.scatterplot(data=mart,x='Item_MRP',y='Sales'
                ,hue='Outlet_Size'
                ,size='Tier'
                ,sizes=(20,200)
                ,legend='full'
                ,palette='Purples_r'
                ,markers={"High":"^","Small":"v","Medium":"o"})


# **7. Change the Marker size with S arguement**

# In[236]:


sns.scatterplot(data=mart,x='Item_MRP',y='Sales',s=500,color='red',edgecolor='black')


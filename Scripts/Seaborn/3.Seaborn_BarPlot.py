#!/usr/bin/env python
# coding: utf-8

# **1. Import all the required libraries**

# In[106]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# **2. Display the SEBORN dataset names and load one of them for example**

# In[109]:


# sns.get_dataset_names()
titanic=sns.load_dataset('titanic')
titanic.head()


# **3. Import mart dataframe**

# In[110]:


mart = pd.read_excel("D:/Learnerea/Tables/supermarket_sales.xlsx")
mart.head()


# **4. Create a basic BARPLOT**

# In[112]:


plt.figure(figsize=(15,5))

sns.barplot(x='Product line',y='Total',data=mart)


# **5. Add HUE to the barplot**

# In[113]:


plt.figure(figsize=(15,5))

sns.barplot(x='Product line',y='Total',hue='Gender',data=mart)


# **6. Make the barplot HORIZONTAL**

# In[114]:


plt.figure(figsize=(15,5))

sns.barplot(x='Total',y='Product line',data=mart)


# **7. Plot the bars in a given ORDER**

# In[120]:


plt.figure(figsize=(15,5))

sns.barplot(x='Product line',y='Total',hue='Gender',data=mart,order=['Electronic_accessories', 'Fashion_accessories','Food_and_beverages', 'Health_and_beauty', 'Home_and_lifestyle','Sports_and_travel']
           ,hue_order=['Male','Female'])


# In[117]:


x=mart['Product line'].sort_values()
x.unique()


# **8. Add CAP on the ERROR BAR**

# In[121]:


plt.figure(figsize=(15,5))

sns.barplot(x='Product line',y='Total',hue='Gender',data=mart,order=['Electronic_accessories', 'Fashion_accessories','Food_and_beverages', 'Health_and_beauty', 'Home_and_lifestyle','Sports_and_travel']
           ,hue_order=['Male','Female']
           ,capsize=0.2)


# **9. REMOVE the error bar using ci**

# In[122]:


plt.figure(figsize=(15,5))

sns.barplot(x='Product line',y='Total',hue='Gender',data=mart,order=['Electronic_accessories', 'Fashion_accessories','Food_and_beverages', 'Health_and_beauty', 'Home_and_lifestyle','Sports_and_travel']
           ,hue_order=['Male','Female']
           ,ci=None)


# **10. Change bar colors using COLOR attribute**

# In[125]:


plt.figure(figsize=(15,5))

sns.barplot(x='Product line',y='Total',data=mart,order=['Electronic_accessories', 'Fashion_accessories','Food_and_beverages', 'Health_and_beauty', 'Home_and_lifestyle','Sports_and_travel']
           ,hue_order=['Male','Female']
           ,color='red')


# **11. Change color using PALLETE attribute**

# In[128]:


plt.figure(figsize=(15,5))

sns.barplot(x='Product line',y='Total',hue='Gender',data=mart,order=['Electronic_accessories', 'Fashion_accessories','Food_and_beverages', 'Health_and_beauty', 'Home_and_lifestyle','Sports_and_travel']
           ,palette='cividis')


# **12. Using SATURATION parameter**

# In[131]:


plt.figure(figsize=(15,5))

sns.barplot(x='Product line',y='Total',hue='Gender',data=mart,order=['Electronic_accessories', 'Fashion_accessories','Food_and_beverages', 'Health_and_beauty', 'Home_and_lifestyle','Sports_and_travel']
           ,palette='cividis'
           ,saturation=0.1)


# **13. CHANGE DEFAULT AGGREGATION METHOD USING ESTIMATOR PARAMETER**

# In[133]:


plt.figure(figsize=(15,5))

sns.barplot(x='Product line',y='Total',hue='Gender',data=mart,order=['Electronic_accessories', 'Fashion_accessories','Food_and_beverages', 'Health_and_beauty', 'Home_and_lifestyle','Sports_and_travel']
           ,palette='cividis'
           ,estimator=np.median)


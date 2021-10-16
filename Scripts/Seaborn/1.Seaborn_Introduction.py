#!/usr/bin/env python
# coding: utf-8

# **1.Installing Seaborn**

# In[ ]:


conda install seaborn


# In[ ]:


pip install seaborn


# **2.Importing all the required libraries**

# In[77]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# **3.Import the data**

# In[76]:


mart = pd.read_excel("D:/Learnerea/Tables/supermarket_sales.xlsx")
mart.head()


# **4.Create a COUNTPLOT**

# In[78]:


sns.countplot(x='Gender',data=mart)


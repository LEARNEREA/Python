#!/usr/bin/env python
# coding: utf-8

# In[45]:


import pandas as pd
import matplotlib.pyplot as plt
# import numpy as np
import seaborn as sns
# from sunbird.categorical_encoding import frequency_encoding

pd.set_option('display.max_rows',None)


# In[87]:


mart = pd.read_excel(r'D:\Learnerea\Tables\mart_linePlot.xlsx')
mart.columns = mart.columns.str.lower()
mart.head(10)


# In[88]:


martPiv=mart.pivot_table(index='outlet_year',columns='outlet_size',values='sales')
martPiv.head()


# In[111]:


sns.clustermap(martPiv
#               ,col_cluster=False
               ,row_cluster=False
               ,annot=True
               ,fmt='.0f'
#                ,z_score=1
               ,standard_scale=1
               ,linewidth=.5
              )


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





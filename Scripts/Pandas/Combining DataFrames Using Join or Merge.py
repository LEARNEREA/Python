#!/usr/bin/env python
# coding: utf-8

# In[30]:


import pandas as pd
pd.set_option('display.max_columns',None)


# In[43]:


cust = pd.read_excel("D:\Learnerea\Tables\martData.xlsx",sheet_name="customer")
tran = pd.read_excel("D:\Learnerea\Tables\martData.xlsx",sheet_name="tran")


# In[45]:


cust


# In[47]:


tran


# In[50]:


dfJoins = cust.join(tran,lsuffix="_cust")
dfJoins


# In[59]:


tran1 = tran
tran1['new index'] = [11,12,13,14,15]
tran1 = tran1.set_index("new index")
tran1


# In[61]:


dfJoins2 = cust.join(tran1,rsuffix="_tran")
dfJoins2


# In[86]:


tran2 = tran.set_index("Invoice ID")
dfJoins3 = cust.join(tran2,lsuffix="_tran",on="Invoice ID")
dfJoins3


# In[76]:


dfMerge = pd.merge(cust[["Invoice ID","Gender"]],tran[["Invoice ID","Quantity","cogs"]],on="Invoice ID",suffixes=("_cust","_tran"),how="left")
dfMerge


# In[77]:


cust1 = cust.rename(columns={"Invoice ID": "Invoice ID Cust"})
tran1 = tran.rename(columns={"Invoice ID": "Invoice ID Tran"})
cust1


# In[79]:


tran1


# In[82]:


dfMerge = pd.merge(cust1[["Invoice ID Cust","Gender"]],tran1[["Invoice ID Tran","Quantity","cogs"]],suffixes=("_cust","_tran"),how="left",left_on="Invoice ID Cust",right_on="Invoice ID Tran")
dfMerge


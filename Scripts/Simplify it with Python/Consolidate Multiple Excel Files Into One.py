#!/usr/bin/env python
# coding: utf-8

# **1.Import all the required libraries**

# In[189]:


import pandas as pd
import os


# **2.Create variables for input and ouput location**

# In[190]:


input_loc  = "D:/Learnerea/temp/output/"
output_loc = "D:/Learnerea/temp/temp_out/"


# **3.Create variable for list of input files**

# In[191]:


fileList = os.listdir(input_loc)
fileList


# **4.Consolidate the files using for loop**

# In[203]:


finalDf = pd.DataFrame()

for files in fileList:
    if files.endswith(".xlsx"):
        df = pd.read_excel(input_loc+files)
        finalDf = finalDf.append(df)
        
finalDf.to_excel(output_loc+"finalDf.xlsx",index=False)


# **5.Exporting different dataframes on different sheets of same excel file**

# In[204]:


writer = pd.ExcelWriter(output_loc+"MultiSheet.xlsx",engine='xlsxwriter')

for files in fileList:
    if files.endswith(".xlsx"):
        df=pd.read_excel(input_loc+files)
        df.to_excel(writer, sheet_name=files, index=False)
writer.save()


# In[208]:


excelFile = pd.ExcelFile(output_loc+"MultiSheet.xlsx")
excelFile.sheet_names


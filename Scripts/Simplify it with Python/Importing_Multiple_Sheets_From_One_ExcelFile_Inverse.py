#!/usr/bin/env python
# coding: utf-8

# In[131]:


import pandas as pd
import numpy as np
import os

pd.set_option('display.max_rows',None)
pd.set_option('display.max_columns',None)

# Location - "D:/Learnerea/temp/output/btcoin_monthly_prices/"


# ## Reading specific set of sheets from excel file

# ## 1.Create list of all the sheets availlable in given excel file
#     Location - "D:/Learnerea/temp/output/btcoin_monthly_prices/"

# In[141]:


sheet = pd.ExcelFile("D:/Learnerea/temp/output/btcoin_monthly_prices/monthly_price.xlsx")
myWorkSheets = sheet.sheet_names
myWorkSheets[0:3]


# # 2.Separate year/string from each of the sheet names

# In[147]:


years = [year[3:] for year in myWorkSheets]
years = list(dict.fromkeys(years))
years


# # 3.Read all the sheets from the said file and create a separate excel for each year

# In[148]:


for year in years:
    excelWriter = pd.ExcelWriter("D:/Learnerea/temp/output/btcoin_monthly_prices/testing/price_list_"+year+".xlsx",engine="xlsxwriter")
    for sheet in myWorkSheets:
        if sheet.endswith(year):
            df = pd.read_excel("D:/Learnerea/temp/output/btcoin_monthly_prices/monthly_price.xlsx",sheet_name=sheet)
            df.to_excel(excelWriter,sheet_name=sheet,index=False)
    excelWriter.save()

#!/usr/bin/env python
# coding: utf-8

# In[34]:


import pandas as pd
import numpy as np
import os

# D:/Learnerea/temp/output/btcoin_monthly_prices/combined
# D:/Learnerea/temp/output/btcoin_monthly_prices/testing


# In[35]:


fileList = os.listdir("D:/Learnerea/temp/output/btcoin_monthly_prices/testing/")
excelWriter = pd.ExcelWriter("D:/Learnerea/temp/output/btcoin_monthly_prices/combined/multiple_sheets.xlsx",engine='xlsxwriter')
files = [file.split('.',1)[0] for file in fileList]

for file in files:
    df = pd.read_excel("D:/Learnerea/temp/output/btcoin_monthly_prices/testing/"+file+".xlsx")
    df.to_excel(excelWriter,sheet_name=file,index=False)
excelWriter.save()


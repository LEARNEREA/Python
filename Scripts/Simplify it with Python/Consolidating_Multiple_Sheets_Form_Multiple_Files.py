# ## Combining sheets with similar name from multiple excel files

# ## 1.List down all the excel files from the given folder

# In[149]:


files = os.listdir("D:/Learnerea/temp/output/btcoin_monthly_prices/testing")
files


# ## 2.Import specific sheets from all the excel files and consolidate them into one

# In[153]:


finalDf = pd.DataFrame()

for file in files:
    sheets = pd.ExcelFile("D:/Learnerea/temp/output/btcoin_monthly_prices/testing/"+file)
    myWorkSheets = sheets.sheet_names
    for sheet in myWorkSheets:
        if sheet.startswith("Jun") or sheet.startswith("Jul"):
            df = pd.read_excel("D:/Learnerea/temp/output/btcoin_monthly_prices/testing/"+file,sheet_name=sheet)
            finalDf = finalDf.append(df)
finalDf.to_excel("D:/Learnerea/temp/output/btcoin_monthly_prices/combined/price_list_jun_jul.xlsx",index=False)


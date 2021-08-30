# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 22:25:04 2021

@author: smrvr
"""
#Import pandas
import pandas as pd

#Import CSV file
df_csv = pd.read_csv("D:/Learnerea/Tables/python/employee_csv.csv"
                     ,engine='python')

#Check the imported file
df_csv.shape

#Subset the imported data
df_csv2 = df_csv.head(30)

#Export the Subset in CSV
df_csv2.to_csv("D:/Learnerea/Tables/python/employee_csv_exported.csv"
               ,index=False)

#Impoert Excel file
df_excel = pd.read_excel("D:/Learnerea/Tables/python/employee_excel.xlsx")

#Check the imported file
df_excel.shape

#Subset imported file
df_excel2 = df_excel.head(25)

#Export the subset in excel
df_excel2.to_excel("D:/Learnerea/Tables/python/employee_excel_exported.xlsx"
                   ,index=False)
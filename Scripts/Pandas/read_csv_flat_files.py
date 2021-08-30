# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 22:47:42 2021

@author: smrvr
"""

#filepath_or_buffer
#sep
#header
#prefix
#mangle_dupe_cols
#nrows
import pandas as pd

#Importing a CSV file with UnicodeDecodeError fix
emp = pd.read_csv("D:Learnerea/Tables/python/employee.csv"
                  ,engine='python'
                  ,encoding = "ISO-8859-1")
emp.head()

#Importing a text or flat file with different separater
emp_sep = pd.read_csv("D:Learnerea/Tables/python/emp_pipe_separated.txt"
                  ,engine='python'
                  ,sep='|')
emp_sep.head()

#Specifying column name or header row
emp_header = pd.read_csv("D:Learnerea/Tables/python/employee.csv"
                  ,engine='python'
                  ,header=1)
emp_header.head()

#Specifying a columns' prefix value
emp_prfx = pd.read_csv("D:Learnerea/Tables/python/employee.csv"
                  ,engine='python'
                  ,header=None
                  ,prefix='emp_')
emp_prfx.head()

#Manage duplicate columns
emp_dup = pd.read_csv("D:Learnerea/Tables/python/emp_duplicate_columns.csv"
                      ,engine='python'
                      ,mangle_dupe_cols=True)
emp_dup.head()

#Read only specific number of rows while importing a csv file
emp_nrows =pd.read_csv("D:Learnerea/Tables/python/employee.csv"
                      ,engine='python'
                      ,nrows=50)
emp_nrows.shape


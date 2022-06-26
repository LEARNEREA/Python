#!/usr/bin/env python
# coding: utf-8

# ### Import required modules

# In[2]:


import os
import pandas as pd
import shutil


# ### Listdown all the files which contains given string

# In[8]:


# list down all the files in the given root directory
ListFiles = []
SearchString = "LEARNEREA"

for dirpath, dirname, filenames in os.walk(r"D:\Learnerea\others"):
    for file in filenames:
        ListFiles.append(os.path.join(dirpath, file))

# Find out the files which contains the given string
Source = []
for file in ListFiles:
    f = open(file,'r',errors='ignore')
    if SearchString in f.read():
        Source.append(file)
    f.close()


# In[17]:


# Source


# ### Prepare output location string

# In[36]:


# Separate the file name from the list created above
FilesList = []

for x in Source:
    FilesList.append(x.split('\\')[-1])

# Concatenate file name with output location
dest = 'D:\Learnerea\youOutputs'

destination = []
for file in FilesList:
    destination.append(os.path.join(dest,file))
destination
# shutil.copyfile(source, dest)

for (x,y) in zip(Source,destination):
    shutil.copyfile(x,y)


# ### Copy from source to location

# In[1]:


# copy the files from source to location


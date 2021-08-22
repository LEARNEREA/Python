

# Import the libraries
import os
import pandas as pd
import numpy as np

# Assign the variables
sourceLoc="D:/Learnerea/others/"
outLoc="D:/Learnerea/temp/"
searchString="LEARNEREA"
fileType=".txt"

direc = os.listdir(sourceLoc)
direc

fileList = []
# For loop to search for the string
for file in direc:
    if file.endswith(fileType):
        f=open(sourceLoc+file,'r')
        if searchString in f.read():
            fileList.append(file)
        f.close()
        

# DataFrame creation and export to excel
stringFile = pd.DataFrame(fileList,columns=['FileName'],index=range(0,len(fileList)))
stringFile.to_excel(outLoc+"stringFile.xlsx",index=False)
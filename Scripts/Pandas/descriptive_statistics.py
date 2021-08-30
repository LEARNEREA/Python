
#Total number of non-missing values     -- using count()
#What's the total sales amount          -- using sum()
#What's the average satisfaction level and what's the spread of it
#                                       -- using mean() and std()
#Most frequently used payment method    -- using mode()
#Minimum and Maximum Quantity sold      -- using min() and max()
#Daily increasing sales                 -- using cumsum()

#DESCRIBE      --- object, all

import pandas as pd

mart = pd.read_excel("D:/Learnerea/Tables/supermarket_sales_data.xlsx")

mart.count()

mart[['Total','gross income']].sum()

mart['Rating'].mean()

mart['Rating'].std()

mart['Payment'].mode()

mart['Quantity'].min()

mart['Quantity'].max()

mart['Total'].cumsum().head()
mart['Total'].head()


mart.describe()

mart.describe(include='object')





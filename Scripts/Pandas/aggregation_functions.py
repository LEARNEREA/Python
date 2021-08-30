
#METHOD 1 - dataframe.aggregate(numpy.aggregate_function)

#METHOD 2 - Dataframe[[‘column or list of columns’]].aggregate([list of numpy.aggregate_function])

#METHOD 3 - Dataframe.aggregate({‘column’: numpy.aggregate_function
#                                ,'column’: numpy.aggregate_function
#                                ,‘column3’: numpy.aggregate_function})

import pandas as pd
import numpy as np

mart = pd.read_excel("D:/Learnerea/Tables/supermarket_sales_data.xlsx")
mart['Date']=pd.to_datetime(mart.Date)

mart[['Date','Unit price','Quantity']].aggregate([np.min,np.max,np.sum])

mart.agg({'Date':[np.min,np.max],
                'Unit price':np.max,
                'Quantity':np.mean})
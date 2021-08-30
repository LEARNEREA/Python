#METHOD 1 - dataframe.aggregate(numpy.aggregate_function)

#METHOD 2 - Dataframe[[‘column or list of columns’]].aggregate([list of numpy.aggregate_function])

#METHOD 3 - Dataframe.aggregate({‘column’: numpy.aggregate_function
#                                ,'column’: numpy.aggregate_function
#                                ,‘column3’: numpy.aggregate_function})

import pandas as pd
import numpy as np

mart = pd.read_excel("D:/Learnerea/Tables/supermarket_sales_data.xlsx")
mart['Date']=pd.to_datetime(mart.Date)

mart_subset = mart[['Product line','Date','Quantity','Payment']].head()
mart_subset.sort_index(axis=1)

equals = mart_subset
equals['Quantity'] = [1,2,3,4,5]

equals
mart_subset

equals['Test'] = [11,12,33,44,55]

equals
mart_subset

mart_subset = mart[['Product line','Date','Quantity','Payment']].head()
mart_subset.sort_index(axis=1)

shallow_copy = mart_subset.copy(deep=False)
shallow_copy['Quantity'] = [1,2,3,4,5]

shallow_copy
mart_subset

shallow_copy['Test'] = [11,12,33,44,55]
shallow_copy
mart_subset

mart_subset = mart[['Product line','Date','Quantity','Payment']].head()
mart_subset.sort_index(axis=1)

deep_copy = mart_subset.copy()

deep_copy['Quantity'] = [1,2,3,4,5]
deep_copy

mart_subset

deep_copy['Test'] = [11,12,33,44,55]

deep_copy

mart_subset
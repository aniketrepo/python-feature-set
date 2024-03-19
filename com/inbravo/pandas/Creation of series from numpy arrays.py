import pandas as pd
import numpy as np

array1= np.array([1,2,3,4,5,6]) # Unspecified index
series1= pd.Series(array1)
print(series1)

series2= pd.Series(array1, index= [6,5,4,3,2,1])    # User-specified index
print(series2)
import pandas as pd
import numpy as np

seriesCapCntry= pd.Series(['New Delhi', 'Tokyo', 'London', 'Paris'], index= ['India', 'Japan', 'UK', 'France'])
print(seriesCapCntry[1:3])              # Shows the values from positional indices 1-2 and excludes the one at positional index 3
print(seriesCapCntry['India':'France']) # Using labelled indices to print values, this time the last one is also printed
print(seriesCapCntry[::-1])             # Printing the series in reverse order
print('\n')

seriesAlph= pd.Series(np.arange(10,16,1), index= ['a', 'b', 'c', 'd', 'e', 'f'])
print(seriesAlph[1:3])  # To print the values at indices 1 and 2, as the last one is excluded
print('\n')

seriesAlph[1:3]= 50  # To change the values of indices 1 to 2 to 50
print(seriesAlph)
print('\n')

seriesAlph['a':'c']= 500   # Slicing using index labels
print(seriesAlph)
print('\n')
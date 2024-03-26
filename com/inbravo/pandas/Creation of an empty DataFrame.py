import pandas as pd
import numpy as np

# Creation of DataFrame-
dframeEmt= pd.DataFrame()    # Creation of an empty DataFrame
print(dframeEmt)
print('\n')




dictLst= {
    'Name':['Jack','John','Zack'],
    'Age':[14,14,15],
    'Class':[12,12,12]
}
dFrameDictLst= pd.DataFrame(dictLst)      # Creation of DataFrame from dictionary of lists
print(dFrameDictLst)
print('\n')
dFrameDictLst1= pd.DataFrame(dFrameDictLst, columns= ['Age', 'Class', 'Name'])        # To change the sequence of column names
print(dFrameDictLst1)
print('\n')

series1= pd.Series([1,2,3,4,5], index= ['a','b','c','d','e'])
series2= pd.Series([100,2000,-60,-8000, 700], index= ['a','b','c','d','e'])
series3= pd.Series([10,20,50,90,70], index= ['x','y','a','c','e'])

dFrame1= pd.DataFrame(series1)
print(dFrame1)
print('\n')
dFrame2= pd.DataFrame([series1 + series2])
print(dFrame2)
print('\n')
dFrame3= pd.DataFrame(series3)
print(dFrame3)
dFrame3= pd.DataFrame([series3 * series2])

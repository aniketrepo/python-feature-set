import pandas as pd

series1= pd.Series([1,2,3,4,5], index= ['a','b','c','d','e'])
series2= pd.Series([100,2000,-60,-8000, 700], index= ['a','b','c','d','e'])
series3= pd.Series([10,20,50,90,70], index= ['x','y','a','c','e'])

dFrame1= pd.DataFrame(series1)          # Creation of DataFrame from series
print(dFrame1)
print('\n')
dFrame2= pd.DataFrame([series1 + series2])
print(dFrame2)
print('\n')
dFrame3= pd.DataFrame(series3)
print(dFrame3)
dFrame3= pd.DataFrame([series3 * series2])
import pandas as pd

series1= pd.Series([10,20,30,40])   # Unspecified index
print(series1)

series2= pd.Series(['Jake','Josh','Justin'], index= [3,2,1])
print(series2)
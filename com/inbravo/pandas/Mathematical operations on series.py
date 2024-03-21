import pandas as pd

seriesA= pd.Series([1,2,3,4,5], index= ['a','b','c','d','e'])
seriesB= pd.Series([10,20,-10,-50,100], index= ['z','y','a','c','e'])

# Addition of two series-
print(seriesA + seriesB)                        # Method 1, will give NaN values
print('\n')
print(seriesA.add(seriesB, fill_value=0))       # Method 2, will not give NaN values
print('\n')

# Subtraction of two series-
print(seriesA - seriesB)                        # Method 1, will give NaN values
print('\n')
print(seriesA.sub(seriesB, fill_value=1000))    # Method 2, will not give NaN values
print('\n')

# Multiplication of two series-
print(seriesA * seriesB)                        # Method 1, will give NaN values
print('\n')
print(seriesA.mul(seriesB, fill_value=0))       # Method 2, will not give NaN values
print('\n')

# Division of two series-
print(seriesA / seriesB)                        # Method 1, will give NaN values
print('\n')
print(seriesA.div(seriesB, fill_value=0))       # Method 2, will not give NaN values
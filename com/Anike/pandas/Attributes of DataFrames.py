import pandas as pd

ForestArea = {
    'Assam': pd.Series([78438, 2797, 10192, 15116],
                       index= ['GeoArea', 'Very Dense', 'Moderately Dense', 'Open Forest']),
    'Kerala': pd.Series([38852, 1663, 9407, 9251],
                        index= ['GeoArea', 'Very Dense', 'Moderately Dense', 'Open Forest']),
    'Delhi': pd.Series([1483, 67.2, 56.24, 129.45],
                       index= ['GeoArea', 'Very Dense', 'Moderately Dense', 'Open Forest'])
}
ForestAreaDF= pd.DataFrame(ForestArea)
print(ForestAreaDF)
print('\n')

# To display row labels
print(ForestAreaDF.index)
print('\n')

# To display column labels
print(ForestAreaDF.columns)
print('\n')

# To display data types of each column in the dataframe
print(ForestAreaDF.dtypes)
print('\n')

# To display a NumPy ndarray having all the values in the dataframe without the axes labels
print(ForestAreaDF.values)
print('\n')

# To display a tuple representing the dimensionality of the dataframe
print(ForestAreaDF.shape)
print('\n')
print(ForestAreaDF.size)
print('\n')

# To print the transpose of the dataframe
print(ForestAreaDF.T)
print('\n')

# To display the first n rows of the dataframe
print(ForestAreaDF.head(2))
print('\n')

# To display the last n rows of the dataframe
print(ForestAreaDF.tail(2))
print('\n')

#  To check whether the dataframe is empty or not
print(ForestAreaDF.empty)
print('\n')
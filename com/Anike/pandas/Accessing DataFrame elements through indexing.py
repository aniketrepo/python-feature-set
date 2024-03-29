import pandas as pd

ResultSheet= {
    'Arnab': pd.Series([90, 91, 97],
                       index= ['Math', 'Science', 'Hindi']),
    'Ramit': pd.Series([92, 98, 85],
                       index= ['Math', 'Science', 'Hindi']),
    'Samridhi': pd.Series([90, 95, 80],
                          index= ['Math', 'Science', 'Hindi']),
    'Riya': pd.Series([81, 71, 67],
                      index= ['Math', 'Science', 'Hindi'])
}
ResultDF= pd.DataFrame(ResultSheet)
print(ResultDF)
print('\n')

# Label-based indexing
print(ResultDF.loc['Science'])
print('\n')

print(ResultDF.loc[:, 'Arnab'])
print('\n')

# Boolean indexing
print(ResultDF.loc['Math']>0)
print('\n')

print(ResultDF.loc[:, 'Arnab']>95)
print('\n')
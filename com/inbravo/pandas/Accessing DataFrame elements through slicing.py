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

# Slicing using row labels
print(ResultDF.loc['Math':'Science'])
print('\n')

print(ResultDF.loc['Math':'Science', 'Arnab'])
print('\n')

print(ResultDF.loc['Math':'Science', ['Arnab', 'Samridhi']])
print('\n')

# Filtering rows in DataFrame
print(ResultDF.loc[[True, False, True]])
print('\n')

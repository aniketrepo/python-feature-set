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

# Adding a new column to a DataFrame
ResultDF['Preeti']= [99, 98, 97]
print(ResultDF)
print('\n')

# Adding a new row to a DataFrame
ResultDF.loc['English']= [98, 95, 95, 84, 65]
print(ResultDF)
print('\n')

# To change all values of a particular row to a particular value
ResultDF.loc['Math']= 0
print(ResultDF)
print('\n')

# To set ALL values in a DataFrame to some particular value
ResultDF[: ]= 0
print(ResultDF)
print('\n')

# Deleting rows or columns from a DataFrame
ResultDF= ResultDF.drop('Science', axis=0)  # Drop row
print(ResultDF)
print('\n')

ResultDF= ResultDF.drop(['Arnab', 'Riya'], axis=1)  # Drop column
print(ResultDF)
print('\n')

# Renaming the row labels of a DataFrame
ResultDF= ResultDF.rename({
    'Math':'Sub1',
    'Science':'Sub2',
    'English':'Sub3',
    'Hindi':'Sub4'
}, axis= 'index')
print(ResultDF)
print('\n')

# Renaming the column labels of a DataFrame
ResultDF= ResultDF.rename({
    'Ramit':'Student1',
    'Samridhi':'Student2',
    'Preeti':'Student3'
},axis= 'columns')
print(ResultDF)
print('\n')
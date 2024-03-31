import pandas as pd

result = {
    'Arnab': pd.Series([90, 91, 97],
                       index= ['Maths', 'Science', 'Hindi']),
    'Ramit': pd.Series([92, 81, 96],
                       index= ['Maths', 'Science', 'Hindi']),
    'Samridhi': pd.Series([89, 91, 88],
                          index= ['Maths', 'Science', 'Hindi']),
    'Riya': pd.Series([81, 71, 67],
                      index= ['Maths', 'Science', 'Hindi']),
    'Mallika': pd.Series([94, 95, 99],
                         index= ['Maths', 'Science', 'Hindi'])
}

resultDF = pd.DataFrame(result)
print(resultDF)
print('\n')

resultDF.to_csv('/home/gawdaintdeadyet/Documents/GitHub/python-feature-set/com/Anike/pandas/CSVs/ResultDF(Linux).csv', sep='.')

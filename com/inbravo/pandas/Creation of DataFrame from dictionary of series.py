import pandas as pd

ResultSheet = {
    'Arnab': pd.Series([90, 91, 97], index = ['Math', 'Science', 'Hindi']),
    'Ramit': pd.Series([92, 98, 85], index = ['Math', 'Science', 'Hindi']),
    'Samridhi': pd.Series([90, 95, 80], index = ['Math', 'Science', 'Hindi']),
    'Riya': pd.Series([81, 71, 67], index = ['Math', 'Science', 'Hindi'])
}
resultDF = pd.DataFrame(ResultSheet)
print(resultDF)
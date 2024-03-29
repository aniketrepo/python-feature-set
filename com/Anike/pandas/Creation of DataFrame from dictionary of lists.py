import pandas as pd

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

import pandas as pd

seriesNum= pd.Series([10,20,30])
print(seriesNum[2])    # To access the element at positional index 2

seriesMnths= pd.Series([1,2,3,4], index= ['Jan','Feb','Mar','Apr'])
print(seriesMnths['Mar'])   # Using the user-defined index to access an element

dictCptls= {
    'India':'New Delhi',
    'UK':'London',
    'Japan':'Tokyo'
}
seriesCptls= pd.Series(dictCptls)
print(seriesCptls['Japan']) # To access an element from a dictionary defined series
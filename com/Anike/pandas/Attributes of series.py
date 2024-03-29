import pandas as pd

dictCapCntry= {
    'India':'Delhi',
    'UK':'London',
    'Japan':'Tokyo',
    'US':'Washington DC'
}
seriesCapCntry= pd.Series(dictCapCntry)
print(seriesCapCntry)

seriesCapCntry.name= 'Capitals'             # [xyz.name= 'something'] assigns a name to the series
seriesCapCntry.index.name= 'Countries'      # [xyz.index.name= 'something'] assigns a name to the index of the series
print(seriesCapCntry.values)                # [xyz.values] prints the values in a series
print(seriesCapCntry.size)                  # [xyz.size] prints the number of values in a series
print(seriesCapCntry.empty)                 # [xyz.empty] checks whether the series is empty or not
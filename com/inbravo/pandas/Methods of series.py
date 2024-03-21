import pandas as pd
import numpy as np

seriesTenTwenty= pd.Series(np.arange(10,21,1))

print(seriesTenTwenty.head(2))     # seriesname.head(n) returns the first 'n' members of the series, if the value of 'n' is not passed then by default it returns the first 5 members of the series
print('\n')
print(seriesTenTwenty.tail(2))     # seriesname.tail(n) returns the last 'n' members of the series, if the value of 'n' is not passed then by default it returns the last 5 members of the series
print('\n')
print(seriesTenTwenty.count())     # seriesname.count() returns the number of non-NaN values in the series
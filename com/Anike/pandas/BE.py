import pandas as pd
import numpy as np

# Q1
SeriesAlph= pd.Series(['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'])
print(SeriesAlph)
print('\n')

Vowels= pd.Series(0, index= ['a','e','i','o','u'])
print(Vowels)
print('\n')

Friends= pd.Series({
    'Aniket':1,
    'Arihant':2,
    'Zade':3
})
print(Friends)
print('\n')

MTSeries= pd.Series()
print(MTSeries.empty)
print('\n')

MonthDays= pd.Series((np.array([31,28,30,31,30,31,30,31,30,31,30,31])), index=[1,2,3,4,5,6,7,8,9,10,11,12])
print(MonthDays)
print('\n')

# Q2
Vowels[:]= 10
print(Vowels)
print('\n')

print(Vowels/2)
print('\n')

Vowels1= pd.Series([2,5,6,3,8], index= ['a','e','i','o','u'])
print(Vowels1)
print('\n')

Vowels3= Vowels + Vowels1
print(Vowels3)
print('\n')

print(Vowels - Vowels1)
print('\n')
print(Vowels * Vowels1)
print('\n')
print(Vowels / Vowels1)
print('\n')

Vowels1.index= ['A','E','I','O','U']
print(Vowels1)
print('\n')

print(Vowels.size)
print('\n')
print(Vowels.values)
print('\n')

MTSeries.name= 'SeriesEmpty'
print(MTSeries)
print('\n')

MonthDays.index.name= 'monthno'
print(MonthDays)
print('\n')
Friends.index.name= 'Fname'
print(Friends)
print('\n')

print('Third and Second values of the Series Friends in that order are', Friends[2], 'and', Friends[1])
print('\n')

print(SeriesAlph[4:16])
print('\n')

print(SeriesAlph.head(11))
print('\n')

print(SeriesAlph.tail(11))
print('\n')

print(MTSeries)
print('\n')

# Q3
print(MonthDays[::-1])
print('\n')

print(MonthDays[1:7])
print('\n')

# Q4
sales= pd.DataFrame({
    2014:[100.5,150.8,200.9,30000,40000],
    2015:[12000,18000,22000,30000,45000],
    2016:[20000,50000,70000,100000,125000],
    2017:[50000,60000,70000,80000,90000]
}, index= ['Madhu', 'Kusum', 'Kinshuk', 'Ankit', 'Shruti'])
print(sales)
print('\n')

# Q5
print(sales.index)
print('\n')

print(sales.columns)
print('\n')

print(sales.dtypes)
print('\n')

print(sales.shape)
print('\n')
print(sales.size)
print('\n')
print(sales.values)
print('\n')

print(sales.tail(2))
print('\n')

print(sales.iloc[:,:2])
print('\n')

sales2= pd.DataFrame({
    2018:[160000,110000,500000,340000,900000]
}, index= ['Madhu', 'Kusum', 'Kinshuk', 'Ankit', 'Shruti'])
print(sales2)
print('\n')
print(sales.empty)

# Q11
print(sales.append(sales2))
print('\n')

print(sales.T)
print('\n')

print(sales[2017])
print('\n')

print(sales.loc[['Madhu','Ankit'], 2017:])
print('\n')

print(sales.loc['Shruti', 2016])
print('\n')

Sumeet= pd.DataFrame({
    2014:[196.2],
    2015:[37800],
    2016:[52000],
    2017:[78438],
    2018:[38852]
}, index= ['Sumeet'])

sales= sales.append(Sumeet)
print(sales)
print('\n')

print(sales.drop(2014, axis= 1))
print('\n')

print(sales.drop('Kinshuk', axis=0))
print('\n')

print(sales.rename(index={'Ankit':'Vivaan','Madhu':'Shailesh'}))
print('\n')


import pandas as pd

marksUT= pd.DataFrame({
    'Name':['Raman', 'Raman', 'Raman', 'Zuhaire', 'Zuhaire', 'Zuhaire', 'Ashravy', 'Ashravy','Ashravy', 'Mishti', 'Mishti', 'Mishti'],
    'UT':[1,2,3,1,2,3,1,2,3,1,2,3],
    'Maths':[22,21,14,20,23,22,23,24,12,15,18,17],
    'Science':[21,20,19,17,15,18,19,22,25,22,21,18],
    'S.St':[18,17,15,22,21,19,20,24,19,25,25,20],
    'Hindi':[20,22,24,24,25,23,15,17,21,22,24,25],
    'Eng':[21,24,23,19,15,13,22,21,23,22,23,20]
})
print(marksUT)
print('\n')

print(marksUT.max())    # Will return the maximum values in each column
print('\n')

print(marksUT.max(numeric_only= True))  # Will only return the maximum numeric values from each columns, ignores the columns which store non-numeric values
print('\n')

marksUT2= marksUT[marksUT.UT == 2]
print('The marks scored by each student in the UT-2 are:')
print(marksUT2)
print('\n')

print('Maximum marks scored by each student in UT-2 are:')
print(marksUT2.max(numeric_only= True))
print('\n')

print(marksUT.max(axis=1))      # To print the maximum marks of a row, one should specify axis=0
print('\n')
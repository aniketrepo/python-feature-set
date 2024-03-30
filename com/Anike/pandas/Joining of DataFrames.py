import pandas as pd

dFrame1= pd.DataFrame(
    [[1, 2, 3], [4, 5], [6]],
    columns= ['C1', 'C2', 'C3'],
    index= ['R1', 'R2', 'R3']
)
print(dFrame1)
print('\n')

dFrame2= pd.DataFrame(
    [[10, 20], [30], [40, 50]],
    columns= ['C2', 'C5'],
    index= ['R4', 'R2', 'R5']
)
print(dFrame2)
print('\n')

dFrame1= dFrame1.append(dFrame2)
print(dFrame1)
print('\n')
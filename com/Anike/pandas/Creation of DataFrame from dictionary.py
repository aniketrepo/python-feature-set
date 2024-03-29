import pandas as pd

dict= [
    {'a':10, 'b':20},
    {'a':5, 'b':10, 'c':20}
]
dFrameDict= pd.DataFrame(dict)      # Creation of DataFrame from dictionary
print(dFrameDict)
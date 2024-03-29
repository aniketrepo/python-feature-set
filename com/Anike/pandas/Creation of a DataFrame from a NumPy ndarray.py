import pandas as pd
import numpy as np

array1= np.array([10,20,30])
array2= np.array([100,200,300])
array3= np.array([-10,-20,-30,-40])
dframeNpy= pd.DataFrame([array1, array2, array3], columns= ['a','b','c','d'])   # Creation of a DataFrame from a NumPy ndarrays
print(dframeNpy)
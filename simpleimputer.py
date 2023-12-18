import numpy as np
import pandas as pd 

def simple_imputer(data, strategy='mean'):
    if strategy not in ['mean', 'median', 'mode']:

        error="Invalid Imputation method"
        return error  
    if strategy == 'mean':
        return data.fillna(data.mean())
    elif strategy == 'median':
        return data.fillna(data.median())
    elif strategy == 'mode':
        return data.fillna(data.mode().iloc[0])  #if multiple values are repeated same time it returns shortest of them 


data = {'Hemang': [13, 54, 7, np.nan , 10 , 34, np.nan, 12, ] ,
        'Jain':[1 , 23 , 1 , np.nan , 34 , 89 ,np.nan , np.nan] }

df = pd.DataFrame(data)


example_mean = simple_imputer(df, strategy='mean')
print("DataFrame after imputation:\n\n", example_mean)

example_median = simple_imputer(df, strategy='median')
print("\nDataFrame after imputation:\n\n", example_median)

example_mode = simple_imputer(df, strategy='mode')
print("\nDataFrame after imputation:\n\n", example_mode)

example_error = simple_imputer(df, strategy='bhupendra jogi')
print("DataFrame after imputation:\n\n", example_error)
    
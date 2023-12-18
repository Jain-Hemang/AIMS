import numpy as np
import pandas as pd

def ordinal_encoder_M1(data):
    # unique_categories , index=np.unique(example_dataset , return_inverse=True)
    unique = np.unique(data)
    print("Uniques Values : " , unique)
    numbers=np.arange(unique.shape[0])
    
    symbols={}
    encoded=[]
    for i in range(unique.shape[0]) :
        symbols[unique[i]]=numbers[i]
    for i in range(data.shape[0]):    
        for key in symbols :
            if (data[i]== key) :
                encoded.append(symbols[key])
            else : 
                continue
    return encoded             
def ordinal_encoder_M2(data):
    unique_values , index=np.unique(example_dataset , return_inverse=True)
    return index 
# Example usage:
example_dataset = np.array(['Hemang' , 'Harshit' , 'Aditya' , 'Harshit' , 'Kartik' , 'Hemang' , 'Aditya'])


encoded_values_M1 = ordinal_encoder_M1(example_dataset)

encoded_values_M2 = ordinal_encoder_M2(example_dataset)
print("Encoded values from method 1 :", encoded_values_M1)

print("Encoded values from method 2:", encoded_values_M2)

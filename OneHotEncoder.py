import numpy as np
import pandas as pd

def one_hot_encode(example_dataset):

    unique_values=np.unique(example_dataset)
    print(unique_values)
    matrix=np.zeros((example_dataset.shape[0] , unique_values.shape[0]) , dtype=int)
    for i in range(example_dataset.shape[0]) :
        for j in range(unique_values.shape[0]) :
            if (example_dataset[i]==unique_values[j]) :
                matrix[i][j]=1 
            else :
                continue 
    return matrix        
    
example_dataset = np.array(['Hemang' , 'Harshit' , 'Aditya' , 'Harshit' , 'Kartik' , 'Hemang' , 'Aditya'])
encoded_matrix = one_hot_encode(example_dataset)
print("Encoded matrix:\n", encoded_matrix)

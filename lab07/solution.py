import numpy as np

def reshape_rows(values, width):
    arr = np.array(values)
    if len(arr) % width == 0:
        arr =  np.array_split(arr, width)
        return arr
    else: return []

def block(matrix, rows, columns):
    if  not matrix or  not rows  or not columns:
        return []
    arr  = np.array(matrix)
    sub_arr = arr[np.ip_(rows, columns)]
    return np.round(sub_arr, 6).tolist()

def column_means(matrix):
     arr  = np.array(matrix)
     return np.round(arr.mean(axis=0), 6).tolist()


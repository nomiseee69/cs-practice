import numpy as np

def reshape_rows(values, width):
    # Добавляем проверку на пустой список values
    if not values or len(values) % width != 0:
        return []
    arr = np.array(values, dtype=float).reshape(-1, width)
    return np.round(arr, 6).tolist()

def block(matrix, rows, columns):
    if not matrix or not rows or not columns:
        return []
    arr = np.array(matrix, dtype=float)
    sub_arr = arr[np.ix_(rows, columns)]
    return np.round(sub_arr, 6).tolist()

def column_means(matrix):
    if not matrix:
        return []
    arr = np.array(matrix, dtype=float)
    return np.round(arr.mean(axis=0), 6).tolist()

def column_range(matrix, column):
    if not matrix:
        return 0.0
    arr = np.array(matrix, dtype=float)
    col_data = arr[:, column]
    difference = np.max(col_data) - np.min(col_data)
    return float(np.round(difference, 6))

import numpy as np

def reverse(matrix):
    n = len(matrix)
    reversed = np.zeros((n, n))
    for i in range(n):
        reversed[i][i] = matrix[i][i]
    for k in range(n):
        for j in range(k + 1):
            for i in range(k + 1, n):
                reversed[i][j] = reversed[i][j] - matrix[i][k] * reversed[k][j]
    # print(reversed)
    return reversed

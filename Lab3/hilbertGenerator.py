import numpy as np
from matrixZipper import zipEm


def generate(height, width):
    matrix = np.zeros((height, width))
    for i in range(height):
        for j in range(width):
            matrix[i][j] = 1 / (i + j + 1)
    return zipEm(matrix)

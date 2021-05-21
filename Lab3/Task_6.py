import time
from diagonalDominantMatrix import diagonalDominantMatrix
from matrixZipper import zipEm
from Task_1 import find_x as uniter_method
from GaussSeidelMethod import seidel as iter_method
import numpy as np

def task6(eps):
    sizes = [10, 50, 100, 1000]
    result = "Accuracy: {eps}\n\n"

    for size in sizes:
        # x vector to find b
        x = []
        for i in range(1, size + 1):
            x.append([i])

        #find b
        b = matrix.dot(np.array(x))
        
        #check methods
        result += f"Size: {size}\n"
        matrix = diagonalDominantMatrix(size)

        #check uniteration method
        data_a, index_a, ind_ptr_a = zipEm(matrix)
        data_b, index_b, ind_ptr_b = zipEm(b)

        uniter_start_time = time.time()
        uniter_method(data_a, index_a, ind_ptr_a, data_b, index_b, ind_ptr_b)

        duration = time.time() - uniter_start_time

        result += f"Uniteration method time: {duration}\n"

        #check iteration method
        iter_start_time = time.time()

        iter_method(matrix, b, eps)

        duration = time.time() - iter_start_time

        result += f"Iteration method time: {duration}\n\n"
    
    return result

print(task6())



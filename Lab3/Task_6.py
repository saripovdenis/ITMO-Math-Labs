import time
from diagonalDominantMatrix import diagonalDominantMatrix
from matrixZipper import zipEm
from Task_1.py import find_x as uniter_method
from GaussSeidelMethod import seidel as iter_method

def task6():
    sizes = [10, 50, 100, 1000]
    result = ""

    for size in sizes:
        result += f"Size: {size}"
        matrix = diagonalDominantMatrix(size)

        #check uniteration method
        [data, index, ind_ptr] = zipEm(matrix)

        uniter_start_time = time.time()
        uniter_method(data, index, ind_ptr)

        duration = time.time() - uniter_start_time

        result += f"Uniteration method time: {duration}"

        #check iteration method
        iter_start_time = time.time()

        iter_method(matrix)

        duration = time.time() - iter_start_time

        result += f"Iteration method time: {duration}"
    
    return result





import numpy as np
from matrixZipper import zipEm
from scipy import sparse as sp

def seidel(A, b, eps):
    iterations = 0
    n = len(A)
    x = np.zeros(n)  # zero vector

    converge = False
    while not converge:
        iterations += 1
        x_new = np.copy(x)
        for i in range(n):
            s1 = sum(A[i][j] * x_new[j] for j in range(i))
            s2 = sum(A[i][j] * x[j] for j in range(i + 1, n))
            x_new[i] = (b[i] - s1 - s2) / A[i][i]

        converge = np.sqrt(sum((x_new[i] - x[i]) ** 2 for i in range(n))) <= eps
        x = x_new

    return x, iterations

def arch_seidel(data_a, index_a, ind_ptr_a, data_b, index_b, ind_ptr_b, eps):
    A = sp.csr_matrix((data_a, index_a, ind_ptr_a)).toarray()
    b = sp.csr_matrix((data_b, index_b, ind_ptr_b)).toarray()
    return seidel(A, b, eps)

import numpy as np
from obrat_l import reverse
from scipy import sparse as sp
from matrixZipper import zipEm

def get_lu(matrix):
    n = len(matrix)
    u = np.zeros((n, n))
    l = np.zeros((n, n))

    for i in range(n):
        for j in range(n):
            u[i][j] = matrix[i][j]

    for i in range(n):
        for j in range(i, n):
            l[j][i] = u[j][i] / u[i][i]

    for k in range(1, n):
        for i in range(k - 1, n):
            for j in range(i, n):
                l[j][i] = u[j][i] / u[i][i]
        for i in range(k, n):
            for j in range(k - 1, n):
                u[i][j] = u[i][j] - l[i][k - 1] * u[k - 1][j]
    return l, u


def find(l, u, b):
    # y = u * x
    # l * y = b
    y = reverse(l).dot(b)
    x = np.linalg.inv(u).dot(y)
    return x


def find_x(data_a, index_a, ind_ptr_a, data_b, index_b, ind_ptr_b):
    lu = get_lu(sp.csr_matrix((data_a, index_a, ind_ptr_a)).toarray())  # lu
    return zipEm(find(np.array(lu[0]), np.array(lu[1]), sp.csr_matrix((data_b, index_b, ind_ptr_b)).toarray()))  # x


def find_a_obrat(data_a, index_a, ind_ptr_a, data_e, index_e, ind_ptr_e):
    lu = get_lu(sp.csr_matrix((data_a, index_a, ind_ptr_a)).toarray())  # lu
    return zipEm(find(np.array(lu[0]), np.array(lu[1]), sp.csr_matrix((data_e, index_e, ind_ptr_e)).toarray()))  # a^-1

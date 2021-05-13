import numpy as np

def get_el(matrix):
    n = len(matrix)
    u = np.array(matrix)
    l = np.zeros((n, n))


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
    print(u)
    print(l)
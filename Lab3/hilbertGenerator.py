import numpy as np
from matrixZipper import zipEm


def generate(height, width):
    matrix = np.zeros((height, width))
    for i in range(height):
        for j in range(width):
            matrix[i][j] = 1 / (i + j + 1)
    return matrix

def hilbertGeneration(a):
    A = generate(a, a)
    B = generate(a, a)
    C = generate(a, a)

    A_cond = np.linalg.cond(A)
    B_cond = np.linalg.cond(B)
    C_cond = np.linalg.cond(C)

    # search A
    min_cond = min(A_cond, B_cond, C_cond)

    if min_cond == B_cond:
        A, B = B, A
        A_cond, B_cond = B_cond, A_cond
    elif min_cond == C_cond:
        A, C = C, A
        A_cond, C_cond = C_cond, A_cond

    # search B
    med_cond = min(B_cond, C_cond)

    if med_cond == C_cond:
        B, C = C, B
        B_cond, C_cond = C_cond, B_cond

    return A, B, C

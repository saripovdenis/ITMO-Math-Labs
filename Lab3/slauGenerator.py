import numpy as np
from diagonalDominantMatrix import diagonalDominantMatrix

def slauGeneration(a):
    A = diagonalDominantMatrix(a)
    B = diagonalDominantMatrix(a)
    C = diagonalDominantMatrix(a)

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

    # print(A)
    # print(B)
    # print(C)
    # print(A_cond, B_cond, C_cond)

    # matrix = sp.csr_matrix(data, ind, indptr).toarray()
    # sp.save_npz('./slauMatrices/test.npz',matrix)

    return A, B, C
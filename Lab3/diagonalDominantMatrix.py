import numpy as np
import random

def fillNonDiagonal(matrix, a):
    for i in range(a):
        for j in range(a):
            if i != j:
                matrix[i][j] = random.randint(0, 100) # random integer from [0;100) 

def fillDiagonal(matrix, a):
    isFirst = True
    for i in range(a):
        sum = 0;

        for j in range(a):
            if i == j:
                sum += 0
            else:
                sum += abs(matrix[i][j])
        
        if isFirst: # one of diagonal values have a '> sum', others '== sum'
            matrix[i][i] = sum + 1
            isFirst = False
        else:
            matrix[i][i] = sum

def fillRandom(matrix, a):
    fillNonDiagonal(matrix, a)
    fillDiagonal(matrix, a)


def diagonalDominantMatrix(a):
    matrix = np.array([[0] * a] * a) # create a a*a size matrix

    fillRandom(matrix, a)
    
    return matrix

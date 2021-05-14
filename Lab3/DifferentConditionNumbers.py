from slauGenerator import slauGeneration
from Task_1 import find_x
from matrixZipper import zipEm
from GaussSeidelMethod import arch_seidel
import numpy as np

def differentConditionNumbers(eps):
    result = ""
    for k in range(2, 3):
        result += f"Matrix dimension: {k}\n\n"
        
        matrices = slauGeneration(k)
        low, med, high = matrices[0], matrices[1], matrices[2]
        result += "Our matrix:\n"
        result += f"Low condition number:\n{low}\n"
        result += f"Medium condition number:\n{med}\n"
        result += f"High condition number:\n{high}\n"

        # x vector to find b in the future
        x = []
        for i in range(1, k + 1):
            x.append([i])

        #exact solution
        result += "Exact solution:\n"

        #low
        b = low.dot(np.array(x))
        low_archived = zipEm(low)
        b_archived = zipEm(b)

        low_exact_solution = find_x(
            low_archived[0], low_archived[1], low_archived[2],
            b_archived[0], b_archived[1], b_archived[2]
        )
        result += f"low:\n{low_exact_solution}\n"

        #medium
        b = med.dot(x)
        med_archived = zipEm(med)
        b_archived = zipEm(b)

        med_exact_solution = find_x(
            med_archived[0], med_archived[1], med_archived[2],
            b_archived[0], b_archived[1], b_archived[2]
        )
        result += f"medium:\n{med_exact_solution}\n"

        #high
        b = high.dot(x)
        high_archived = zipEm(high)
        b_archived = zipEm(b)

        high_exact_solution = find_x(
            high_archived[0], high_archived[1], high_archived[2],
            b_archived[0], b_archived[1], b_archived[2]
        )
        result += f"high:\n{high_exact_solution}\n"

        #inexact solution
        result += "Inexact solution:\n"

        #low
        b = low.dot(x)
        low_archived = zipEm(low)
        b_archived = zipEm(b)

        low_inexact_solution = arch_seidel(
            low_archived[0], low_archived[1], low_archived[2],
            b_archived[0], b_archived[1], b_archived[2],
            eps
        )
        result += f"low:\n{low_inexact_solution}\n"

        #medium
        b = med.dot(x)
        med_archived = zipEm(med)
        b_archived = zipEm(b)

        med_inexact_solution = arch_seidel(
            med_archived[0], med_archived[1], med_archived[2],
            b_archived[0], b_archived[1], b_archived[2],
            eps
        )
        result += f"medium:\n{med_inexact_solution}\n"

        #high
        b = high.dot(x)
        high_archived = zipEm(high)
        b_archived = zipEm(b)

        high_inexact_solution = arch_seidel(
            high_archived[0], high_archived[1], high_archived[2],
            b_archived[0], b_archived[1], b_archived[2],
            eps
        )
        result += f"high:\n{high_inexact_solution}\n"

    return result

print(differentConditionNumbers(0.00001))

from scipy import sparse as sp

data = [1, 1, 2, 5, 1, 3]
ind = [0, 1, 2, 1, 0, 2]
indptr = [0, 3, 4, 6]

print(sp.csr_matrix((data, ind, indptr)).toarray())
print("task_1")

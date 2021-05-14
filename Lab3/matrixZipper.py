def zipEm(matrix):
    n = len(matrix)
    data = []
    index = []
    ind_ptr = [0]
    counter = 0
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != 0:
                data.append(matrix[i][j])
                index.append(j)
                counter += 1
        ind_ptr.append(counter)
    return data, index, ind_ptr
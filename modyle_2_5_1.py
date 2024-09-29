def get_matrix(n,m,volue):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(volue)
    return matrix

print(get_matrix(2,2,10))
print(get_matrix(3,5,42))
print(get_matrix(4,2,13))
def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
    return matrix


result_1 = get_matrix(2, 3, 10)
result_2 = get_matrix(3, 4 ,5)
result_3 = get_matrix(4, 9 ,8)
print(result_1)
print(result_2)
print(result_3)
# Задача "Матрица воплоти":
def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
    return matrix


matrix = get_matrix(4, 2, 13)
print(matrix)

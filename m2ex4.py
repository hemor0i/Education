# Задача "Матрица воплоти":
def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])                               # Добавляем "строку" в список
        for j in range(m):
            matrix[i].append(value)                     # Заполняем список значениями
    return matrix


n = int(input('Введите количество строк матрицы: '))    # Определяем как целочисленное, тк input всегда типа str
m = int(input('Введите количество столбцов матрицы: ')) # То же самое
value = input('Введите значение заполнения матрицы: ')  # Чтобы можно было любыми символами заполнять
matrix = get_matrix(n, m, value)
print(matrix)

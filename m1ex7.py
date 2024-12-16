grades = [[5,3,3,5,4],[2,2,2,3],[4,5,5,2],[4,4,3],[5,5,5,4,5]]
students = {'Johnny','Bilbo','Steve','Khendrik','Aaron'}
print(students)
# Переопределим в кортеж и отсортируем, хоть мы и не изучали такую функцию
students = sorted((tuple(students)))
print(students)
# Создадим пустое множество для будущего словаря
dictionary = {}
# Хоть мы еще и не изучали циклы, но я думаю тут без него не обойтись
for i in range(len(grades)):
    # Найдем среднее арифметическое
    arith_mean = sum(grades[i]) / len(grades[i])
    print(arith_mean)
    # Создадим словарь, добавляя в него итерационно элементы
    dictionary[students[i]] =  arith_mean
print (dictionary)
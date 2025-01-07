# Задание "Раз, два, три, четыре, пять .... Это не всё?":
def calculate_structure_sum(data):
    sum_ = 0
    for i in data:
        if isinstance(i, dict): # Проверка на тип словарь
            for j in i.items(): # Метод items() возвращает ключ и значение словаря в виде кортежа, можно итерировать
                sum_ += calculate_structure_sum(j)  # Для каждого значения кортежа вызвать рекурсивно функцию
        elif isinstance(i, str):    # Проверка на тип str
            sum_ += len(i)  # Прибавить длину строки к sum_
        elif isinstance(i, int):    # Проверка на тип int
            sum_ += i   # прибавить число
        else:
            sum_ += calculate_structure_sum(i)  # Если тип = список, кортеж либо множество вызов рекурсивно функции
    return sum_


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]
result = calculate_structure_sum(data_structure)
print(result)

# Задача "Счётчик вызовов":
def count_calls():
    global calls  # Используем глобальную переменную calls
    calls += 1


def string_info(string):
    count_calls()  # Вызываем функцию, чтобы прибавить 1 в calls
    length = len(string)  # Создаем переменную length и записываем в нее длину вводимой строки
    return length, string.upper(), string.lower()  # выводим кортеж из длины строки, строки в нижнем и в верхнем рег.


def is_contains(string, list_to_search):
    count_calls()   # Вызываем функцию, чтобы прибавить 1 в calls
    string = string.lower()  # Приводим строку в нижний регистр
    for i in range(len(list_to_search)):
        list_to_search[i] = list_to_search[i].lower()  # Цикл для приведения строк в списке в нижний регистр
        if string == list_to_search[i]:  # Поиск строки в списке и вывод
            return True

    return False

calls = 0       # Объявляем глобальные переменные

# Дальше вызываем как в примере задачи для проверки
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)

# Далее реализуем цикл с вызовом, чтобы постоянно не изменять код
calls = 0   # Обнуляем calls
while True:     # Создаем цикл
    stop = input('Функция string_info. Введите stop, если не хотите продолжать вызывать функцию: ')
    if stop == 'stop': break    # При вводе 'stop' Цикл завершится
    print(string_info(input('Введите любую строку: ')))     # Вызываем функцию string_info

while True:
    stop = input('Функция is_contains. Введите stop, если не хотите продолжать вызывать функцию: ')
    if stop == 'stop': break    # При вводе 'stop' Цикл завершится
    string = input('Введите строку для поиска: ')
    list_to_search = []     # Определяем список в котором будем искать
    for i in range(int(input('Введите количество элементов в списке: '))):  # Определяем количество итераций
        item = input(f'Введите {i + 1} элемент списка: ')   # Вводим i-тый элемент списка
        list_to_search.append(item)                 # Добавляем в список элемент
    print(list_to_search)                           # Выводим весь список для личного удобства
    print(is_contains(string, list_to_search))      # Вызов функции is_contains
print(f'Было совершено вызовов функций: {calls}')                           # Отображение количества вызовов функций string_info и is_contains

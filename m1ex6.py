# 1. Работа со словарями
# Создайте переменную my_dict и присвойте ей словарь из нескольких пар ключ-значение
my_dict = {'Veniamin': 1997, 'Vladislav': 2000, 'Roman': 2003}
# Выведите на экран словарь my_dict.
print(my_dict)
# Выведите на экран одно значение по существующему ключу, одно по отсутствующему из словаря my_dict без ошибки.
print(my_dict['Roman'],my_dict.get('Robert', ''))
# Добавьте ещё две произвольные пары того же формата в словарь my_dict.
my_dict.update({'Aleksandr':1998, 'Timur':1999})
# Удалите одну из пар в словаре по существующему ключу из словаря my_dict и выведите значение из этой пары на экран
print (my_dict.pop('Aleksandr'))
# Выведите на экран словарь my_dict.
print(my_dict)

# 2. Работа с множествами
# Создайте переменную my_set и присвойте ей множество, состоящее из разных типов данных с повторяющимися значениями.
my_set = {1,2,3,1,2,3,4,5,True,'Kirill','Ekaterina','Kirill'} # True=1 поэтому не отображается
# Выведите на экран множество my_set (должны отобразиться только уникальные значения).
print(my_set)
# Добавьте 2 произвольных элемента в множество my_set, которых ещё нет.
add_ = {}
my_set.update({'Masha', "Rima",}) # Понял, что вместо .add можно и .update использовать
# Удалите один любой элемент из множества my_set.
my_set.remove('Masha')
# Выведите на экран измененное множество my_set.
print(my_set)
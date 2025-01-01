# Задача "Распаковка":
# 1. Функция с параметрами по умолчанию
def print_params(a=1, b='строка', c=True):
    print(a, b, c)

print_params()
print_params(3,'Cobra', False)
print_params(b=25)          # Работают вызовы
print_params(c = [1,2,3])

# 2. Распаковка параметров:
values_list = [27, True, 'Gena']
values_dict = {'a':7,'b':'String','c':True}
print_params(*values_list)
print_params(**values_dict)

# 3.Распаковка + отдельные параметры:
values_list_2 = [28.72, 'Строка']
print_params(*values_list_2,42)     # Работает

# С Новым Годом! 1-ый код в 2025 году

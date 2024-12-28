# Задача "Распаковка":
# 1. Функция с параметрами по умолчанию
def print_params(a=1, b='строка', c=True):
    print(a, b, c)

print_params()
print_params(3,'Cobra', False)
print_params(b=25)
print_params(c = [1,2,3])

# 2. Распаковка параметров:
values_list = [27, True, 'Gena']
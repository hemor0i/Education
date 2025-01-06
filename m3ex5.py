def get_multiplied_digits(number):
    str_number = str(number)    # Создадим объект со строкой числа
    first = int(str_number[0])  # Первый символ переопределим в int
    if first == 0:  # Исключаем вызов функции при 0
        return 1
    elif len(str_number) > 1:   # Основная рекурсия
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first    # Возврат числа, когда рекурсия доходит до последней цифры


result = get_multiplied_digits(40203)
print(result)
result2 = get_multiplied_digits(402030)
print(result2)

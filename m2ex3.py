# "Всё не так уж просто"
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in numbers:
    count = 0                   # Для подсчёта количества делителей
    is_prime = True
    for j in range(2, i+1):     # Пересчет делителя в диапазоне от 2 до деления самого на себя
        if i % j == 0:
            count += 1          # Инкремент в случае деления без остатка
        if count == 2:
            is_prime = False    # Если количество делителей == 2 (Исключили деление на 1)
            break               # Выход из цикла если делителей = 2
    if is_prime and count>0:    # 'count > 0' чтобы исключить 1 в списках
        primes.append(i)
    elif count>0:               # 'count > 0' чтобы исключить 1 в списках
        not_primes.append(i)
print(primes, not_primes)

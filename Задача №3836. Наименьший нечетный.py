# Ввод списка чисел
numbers = list(map(int, input().split()))

# Фильтруем нечетные числа из списка
odd_numbers = [num for num in numbers if num % 2 != 0]

# Проверяем, есть ли нечетные числа
if odd_numbers:
    # Находим и выводим наименьшее нечетное число
    print(min(odd_numbers))
else:
    # Если нечетных чисел нет, выводим 0
    print(0)
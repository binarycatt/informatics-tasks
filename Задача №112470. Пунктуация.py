# Считываем входную строку
input_string = input()

# Задаем набор знаков пунктуации
punctuation_marks = ".,;:!? "

# Инициализируем счетчик
punctuation_count = 0

# Перебираем каждый символ в строке
for char in input_string:
    if char in punctuation_marks:
        punctuation_count += 1

# Выводим общее количество знаков пунктуации
print(punctuation_count)
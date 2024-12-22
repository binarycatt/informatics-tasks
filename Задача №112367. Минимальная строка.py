# Считываем размеры матрицы
N, M = map(int, input().split())

# Инициализируем матрицу
matrix = []
for _ in range(N):
    row = list(map(int, input().split()))
    matrix.append(row)

# Переменные для хранения минимальной суммы и индекса строки с минимальной суммой
min_sum = float('inf')
min_row_index = -1

# Находим строку с минимальной суммой
for i in range(N):
    row_sum = sum(matrix[i])  # Сумма элементов строки
    if row_sum < min_sum:  # Если текущая сумма меньше минимальной
        min_sum = row_sum
        min_row_index = i  # Запоминаем индекс строки

# Выводим элементы найденной строки с минимальной суммой
print(" ".join(map(str, matrix[min_row_index])))
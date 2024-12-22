# Считываем количество пар синонимов
N = int(input())

# Инициализируем словарь для хранения синонимов
synonyms = {}

# Считываем пары синонимов
for _ in range(N):
    word1, word2 = input().split()
    synonyms[word1] = word2
    synonyms[word2] = word1  # Добавляем обратное соответствие

# Считываем слово, для которого нужно найти синоним
given_word = input().strip()

# Выводим синоним
print(synonyms[given_word])
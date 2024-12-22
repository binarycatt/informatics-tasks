import math

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    # Проверяем делимость от 5 до √n с шагом 6
    for i in range(5, int(math.sqrt(n)) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
            
    return True

# Считываем входное число
n = int(input())

# Проверяем, является ли число простым
if is_prime(n):
    print("prime")
else:
    print("composite")

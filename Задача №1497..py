# Входные данные
a, b = map(int, input().split())

if a == 0:
    if b == 0:
        print("many solutions")
    else:
        print("no solution")
else:
    if b % a == 0:
        x = b // a
        print(x)
    else:
        print("no solution")
num = int(input())
same = False
a = 0

while num != 0:
    last_digit = num % 10
    if last_digit == a:
        same = True
    else:
        a += last_digit
    num = num // 10

if same == True:
    print('YES')
else:
    print('NO')
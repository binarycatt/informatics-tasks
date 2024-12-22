a = int(input())
b = int(input())

if (a == 0 and b == 0):
    print('many solutions')
elif (a == 0 or (b % a) != 0):
    print('no solution')
else: 
    print(int(b / a))

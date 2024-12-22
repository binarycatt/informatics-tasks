n, m = map(int, input().split())

a = []
max_1 = 0
s = 0
per_2 = 0

for i in range(n):
    b = list(map(int, input().split()))
    a.append(b)

for i in range(n):
    for j in range(m):
        s = s + a[i][j]
    if s > max_1:
        max_1 = s
        per_2 = i
    s = 0

print(max_1)
print(per_2)
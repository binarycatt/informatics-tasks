n, m = (int(i) for i in input().split())
A = []
for i in range(n):
    A.append([int(i) for i in input().split()])
c = []
found = False
for i in range(m):
    for j in range(n):
        c.append(A[j][i])
    idx_max = c.index(max(c))
    if min(A[idx_max]) == max(c):
        print("{} {}".format(idx_max + 1, i + 1))
        found = True
    c = []
if not found:
    print(0)
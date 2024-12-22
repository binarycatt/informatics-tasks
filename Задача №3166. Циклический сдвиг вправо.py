a = list(map(int, input().split()))
last_elem = a[-1]
for i in range(len(a)-1, 0, -1):
    a[i] = a[i-1]
a [0] = last_elem
print(" ".join(map(str, a)))
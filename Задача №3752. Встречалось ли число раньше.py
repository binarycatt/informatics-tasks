data = input().split()
cur_set = set()
for item in data:
    if item in cur_set:
        print('YES')
    else:
        print('NO')
    cur_set.add(item)
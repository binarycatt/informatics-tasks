lst = [int(_) for _ in input().split()]
dictionary = dict()
for num in lst:
   if num in dictionary:
       dictionary[num] += 1
   else:
       dictionary[num] = 1

print(max(dictionary.items(), key=lambda x: x[1])[0])
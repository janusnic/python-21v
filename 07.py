# -*- coding:utf-8 -*- 

arr = [1,2,3,4,5,6,7]

for i in range(len(arr)):
    arr[i] *= 2
print(arr)

arr = [ i * 2 for i in arr]
print(arr)

for i, elern in enumerate(arr):
    arr[i] *= 2

print(arr)

i, c = 0, len(arr)
while i < c:
    arr[i] *= 2
    i += 1

print(arr)

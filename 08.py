# -*- coding:utf-8 -*- 

arr = [1,2,3,4,5,6,7]

for i in range(len(arr)):
    arr[i] *= 2
print(arr)

arr = [ i * 2 for i in arr]
print(arr)

arr = [ i * 10 for i in arr if i % 2 == 0]


arr = [ [1, 2], [3, 4], [5, 6] ]
arr = [ j * 10 for i in arr for j in i if j % 2 == 0 ]

print(arr)

arr = [1, 4, 12, 45, 10]
print(sum( ( i for i in arr if i % 2 ==0) ))

combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combs.append((x, y))

print(combs)

print([(x, y) for x in [1,2,3] for y in [3,1,4] if x != y])
# [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

vec = [[1,2,3], [4,5,6], [7,8,9]]
print([num for elem in vec for num in elem])
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

M = [ # Матрица 5 x 5 в виде вложенных списков
    [1,2,3,4,5], # Выражение в квадратных скобках может
    [1,4,3,4,5],
    [1,5,3,4,5],
    [1,7,3,4,5],
    [1,8,3,4,5], # занимать несколько строк
    ] 

print(M) # [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]]

col2 = [row[1] for row in M] # Выбирает элементы второго столбца

print(col2)

print(M) # Матрица не изменилась


print([row[1] + 1 for row in M]) # Добавить 1 к каждому элементу в столбце 2

print([row[1] for row in M if row[1] % 2 == 0]) # отфильтровать нечетные значения


diag = [ M[i][i] for i in [0, 1, 2, 3, 4]] # Выборка элементов диагонали матрицы
print(diag)

doubles = [c * 2 for c in 'spam'] # Дублирование символов в строке
print(doubles)

G = (sum(row) for row in M) # Генератор, возвращающий суммы элементов строк
print(next(G))
print(next(G)) # Вызов в соответствии с протоколом итераций




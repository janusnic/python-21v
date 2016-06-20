# -*- coding:utf-8 -*- 

import copy # Подкточаем модуль сору

x = [1,[2,3,4,5]] # Создали вложенный список

# делаем полную копию списка
y = copy.deepcopy(x) 

# Изменяем второй элемент
y[1][1] = 100

# Изменился только список в переменной у
print(x, y) # [1, [2, 3, 4, 5]] [1, [2, 100, 4, 5]]



x = [1,2]

y = [x,x] 

print(x, y) # два элемента ссылаются на один объект

z = copy.deepcopy(y) # Сделали копию списка

print(z)

print(z[0] is x, z[1] is x, z[0] is z[1])

z[0][0] = 300 # Изменили один элемент

print(z) # Значение изменилось сразу в двух элементах!

print(x) # Начальный список не изменился


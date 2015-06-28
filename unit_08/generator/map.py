# -*- coding:utf-8 -*-

# функция map, реализованная с помощью итераторов

def map(func, iterable):
    result = []
    for item in iterable:
        result.append(func(item))
    return result


it = iter(range(10))

print map(lambda x: x*x,it)

# функция map, реализованная с помощью генераторов   

def gmap(func, iterable):
    for item in iterable:
        yield func(item)
 
def map(func, iterable):
    return list(gmap(func, iterable))

it = iter(range(20))
print map(lambda x: x*x,it)

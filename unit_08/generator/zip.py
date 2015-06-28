# -*- coding:utf-8 -*-

def random(min_val=0, max_val=100):
    import random as rand
    rand.seed()
    while True:
        yield rand.randint(min_val, max_val)
 
print [r for (r, i) in zip(random(), xrange(20))] # [42, 17, 35, 96, 31, 11, 18, 9, 81, 78, 35, 71, 14, 12, 28, 24, 62, 67, 61, 49]

# Для list comprehensions так же существует аналог, возвращающий объект-генератор. Для этого выражение нужно заключить не в квадратные, а в круглые скобки:

print [r for (r, i) in zip(random(), xrange(20))] # [21, 35, 95, 20, 42, 88, 70, 72, 69, 50, 74, 52, 86, 26, 16, 39, 0, 63, 27, 21]

print (r for (r, i) in zip(random(), xrange(20))) # <generator object <genexpr> at 0x7fa00b298050>

print [r for r in zip(random(), xrange(20))] # [94, 23, 55, 17, 23, 50, 56, 44, 79, 30, 58, 1, 85, 46, 88, 99, 95, 2, 81, 44]
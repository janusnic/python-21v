# -*- coding:utf-8 -*-
class Reverse:
    def __init__(self, data):
        self.data = data
        self.index = len(data)
    def __iter__(self):
        return self
    def next(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]
 
print [char for char in Reverse("string")] # ['g', 'n', 'i', 'r', 't', 's']

# По умолчанию, итераторы однонаправленные и не возобновляемые:

it = iter(range(10))

print [i for i in it] # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print [i for i in it] # []

it = iter(range(10))
print zip(it, it) # [(0, 1), (2, 3), (4, 5), (6, 7), (8, 9)]
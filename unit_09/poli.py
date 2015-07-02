# -*- coding:utf-8 -*-
class A:
    def __init__(self, name):
        self.name = name
    def go(self):
        print('Go, A!')

class B(A):
    def go(self, name):
        print('Go, {}!'.format(name))


a = A('Vasya')

print a.name # Vasya
a.go()

b = B('Merry')
print b.name # Vasya
b.go('Bob')
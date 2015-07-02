# -*- coding:utf-8 -*-
class Newclass:
     def __init__(self, base):
          self.base = base
     def __add__(self, a):
          self.base = self.base + a
     def __str__(self):
          return "%s !!! " % self.base
 
a = Newclass(10)
a + 20
print a
 
b = Newclass("yes")
b + "terday"
print b
 
c = Newclass([2,6,3])
c + [7, 1]
print c

# Задание. 
# Дополните класс методами __mul__ 
# (вызывается при использовании объекта в операциях умножения) 
# и__sub__ (вычитание). 
# Вызовите данные методы с помощью соответствующих операций 
# с объектами. Для каких объектов невозможно использовать метод __sub__?
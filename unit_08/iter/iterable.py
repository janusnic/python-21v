# -*- coding:utf-8 -*-
class Iterable():
    def __init__(self, data):
        self.it = iter(data)
    def next(self):
        return self.it.next()
 
class Iterator():
    def __init__(self, data):
        self.data = data
    def __iter__(self):
        return Iterable(self.data)
 
it = Iterator("string")
# it.next() # такого метода нет - он определен в Iterable


print [char for char in Iterator("string")] #['s', 't', 'r', 'i', 'n', 'g']

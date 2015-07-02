# -*- coding:utf-8 -*-

class First():
    def setdata(self,string):
        self.name = string
    def display(self):
        print self.name

class Second(First):
    def display(self):
        print "Current value: %s" % self.name

class Third(Second):
    def __init__(self,value):
        self.name = value
    def __add__(self,other):
        self.name = self.name + other # не создается новый объект
    def __mul__(self,n):
        self.name = self.name * n

class Fourth(Third):
    def __add__(self,other):
        return Fourth(self.name + other) # создается новый объект
    def __mul__(self,n):
        return Fourth(self.name * n)

a = First()
b = Second()

a.setdata('Dima')
b.setdata(12.5)

a.display()
b.display()

c = Third("abc")
c + 'def '
c * 2
c.display()

d = Fourth(67)
d = d + 9
d = d * 10
d.display()

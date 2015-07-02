# -*- coding:utf-8 -*-

# Реализация доступа по индексу
class Indexer:
    def __init__(self, start):
        self.data = start
    def __getitem__(self, index):
        return self.data[index]

x = Indexer([5,3,9])
print(x[0])
for i in x:
    print i
for i in range(3):
    print x[i]

y = Indexer('bams')
print y[3]
print 'm' in y  # True
a,b,c,d = y

print a,c
print list(y)

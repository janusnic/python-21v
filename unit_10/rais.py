# -*- coding:utf-8 -*-


# raise RuntimeError('Неустранимая ошибка')



class Bad(Exception): pass

def doomed(): raise Bad()

try:
    doomed()
except Bad:
    print 'got Bad'

# got Bad


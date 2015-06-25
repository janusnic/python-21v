# -*- coding:utf-8 -*-
import io
import os

fh = open('file.txt','w')
fh.write('hello')
print __file__ 
# os.path.dirname(__file__) == путь к директории, содержащей исполняемый файл, 
# _относительно_текущей_рабочей_директории_. 
# Если эти две директории - это одна директория, то путь равен пустой строке.
print os.path.dirname(__file__)
print(__name__)
# print __loader__
print __package__
# текущая директроия Current Workin Directory
print os.getcwd()
# директория в которой лежит скрипт
print os.path.abspath(os.path.dirname('__file__'))

import os.path

for path in [ '/one/two/three', 
              '/one/two/three/',
              '/',
              '.',
              '']:
    print '"%s" : "%s"' % (path, os.path.split(path))

# -*- coding:utf-8 -*-

import sys
 
try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except IOError as err:
    print "I/O error: {0}".format(err)
except ValueError:
    print "Не могу преобразовать данные в целое."
except:
    print "Неожиданная ошибка:", sys.exc_info()[0]
    raise
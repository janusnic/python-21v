# -*- coding:utf-8 -*-
"""Описание модуля.

Подробное описание использования.
"""
import sys
import getopt
from main5 import runapp


def main():
    # Разбираем аргументы командной строки
    try:
        opts, args = getopt.getopt(sys.argv[1:], "h", ["help"])
    except getopt.error, msg:
        print msg
        print "для справки используйте --help"
        sys.exit(2)
    # process options
    for o, a in opts:
        if o in ("-h", "--help"):
            print __doc__
            sys.exit(0)

    runapp()

    # Анализируем
    # for arg in args:
    #    process(arg) # process() определен в другом месте

if __name__ == "__main__":
    main()

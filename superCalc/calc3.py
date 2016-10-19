# -*- coding:utf-8 -*-
# ---------- CALCULATOR ----------
'''
 Program make a simple calculator that can add,
 subtract, multiply and divide using functions
'''
from lib.functions import *
from utils.menu import menu, printMenu, myhelp, extacts
ops = ('+', '-', '*', '/', '//', '%', '**')

while True:

    choice = menu()

    if choice == 'q':
        print('{!s:#^40}'.format('Thankyou for using calculator.py!'))
        break
    if choice == 'h':
        myhelp()
        continue
    if choice == 'c':
        entry = raw_input("Enter x operator y: ")

        for o in ops:
            if entry.count(o) == 1:
                a, b, operator = extacts(entry, o)
            if entry.count(o) == 2:
                a, b, operator = extacts(entry, 2*o)

        if a.isdigit():
            x = float(a)
        else:
            myhelp()
            continue

        if b.isdigit():
            y = float(b)
        else:
            myhelp()
            continue

        if operator not in ops:
            myhelp()
            continue

        if operator == "+":
            print("{} + {} = {}".format(x, y, add(x, y)))

        elif operator == "-":
            print("{:+08.2f} - {:+08.2f} = {:+08.2f}"
                  .format(x, y, subtract(x,  y)))

        elif operator == "*":
            print("{0} * {k} = {1}".format(x, multiply(x, y), k=y))

        elif (operator == "/" or operator == "//" or operator == "%")  and y == 0:
            print 'integer division or modulo by zero'

        elif operator == "/" and y != 0:
            print("{0:+08.2f} / {1:+08.2f} = {2:+08.2f}"
                  .format(x, y, divide(x, y)))

        elif operator == "//" and y != 0:
            print("{} // {} = {}".format(x, y, intdivide(x, y)))

        elif operator == "%" and y != 0:
            print("{} % {} = {}".format(x, y, modulo(x, y)))

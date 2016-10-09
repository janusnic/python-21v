# -*- coding:utf-8 -*-
# ---------- CALCULATOR ----------
'''
 Program make a simple calculator that can add,
 subtract, multiply and divide using functions
'''

# define functions


def add(x, y):
    """This function adds two numbers"""
    return x + y


def subtract(x, y):
    """This function subtracts two numbers"""
    return x - y


def multiply(x, y):
    """This function multiplies two numbers"""
    return x * y


def divide(x, y):
    """This function divides two numbers"""
    return float(x / y)


def intdivide(x, y):
    """This function int divides two numbers"""
    return x // y


def modulo(x, y):
    """This function modulos two numbers"""
    return x % y


ops = ('+', '-', '*', '/', '//', '%', '**')
titles = ('Select operation:', "Usage operation:")
choices = ("Help", "Calculate", "Quit")
helpers = ('Display this usage message', 'Example: 55 % 7', 'Exit programm')


def printMenu(w, j, obj):
    gup = (': ', '| ')
    print("_"*(w+7))
    print(gup[1] + titles[j].ljust(w+3, ' ') + gup[1][::-1])

    for item in obj:
        print(gup[1] + item[0].lower() + gup[0] + item.ljust(w, ' ') +
              gup[1][:: -1])

    print("="*(w+7))


def menu():
    tupleLen = [len(i) for i in choices]
    width = max(max(tupleLen), len(titles[0]))

    print 'Super Calc'.upper().center(width+7, '=')
    printMenu(width, 0, choices)

    choice = raw_input("| Enter choice(h|c|q):".title())
    return str(choice) if choice != '' else 'h'


def myhelp():
    list1 = list()
    for i in range(len(helpers)):
        list1.append(choices[i]+' - ' + helpers[i])

    listLen = [len(i) for i in list1]
    printMenu(max(listLen), 1, list1)


def extacts(entry, o):
    index = entry.find(o)
    if index != -1:
        a, b = entry.split(o)
        a = a.strip()
        b = b.strip()
    return (a, b, o)


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

        elif (operator == "/" or operator == "//" or operator == "%")
        and y == 0:
            print 'integer division or modulo by zero'

        elif operator == "/" and y != 0:
            print("{0:+08.2f} / {1:+08.2f} = {2:+08.2f}"
                  .format(x, y, divide(x, y)))

        elif operator == "//" and y != 0:
            print("{} // {} = {}".format(x, y, intdivide(x, y)))

        elif operator == "%" and y != 0:
            print("{} % {} = {}".format(x, y, modulo(x, y)))

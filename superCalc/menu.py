# -*- coding:utf-8 -*-
# ---------- CALCULATOR ----------
'''
 Program make a simple calculator that can add,
 subtract, multiply and divide using functions
'''

# define functions


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

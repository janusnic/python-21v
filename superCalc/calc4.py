# -*- coding:utf-8 -*-
# ---------- CALCULATOR ----------
'''
To run under Python3 replace 'raw_input' call
with 'input'
Store the user input an operator
'''
print 'Super Calc'

while True:
    # Convert strings into integers
    x = float(raw_input("Enter x: "))
    y = float(raw_input("Enter y: "))

    # Store the user input an operator
    operator = raw_input('Enter Operator: ')

    if operator == 'q':
        print('Programm exit.')
        break

    if operator not in ('+','-','*','/','//','%','**'):
        print ("Help: Use either + - * / or % next time")
        continue

    if operator == "+":
        print ("{} + {} = {}".format(x, y, x * y))

    # If the 1st condition wasn't true check if this one is
    elif operator == "-":
        print ("{} - {} = {}".format(x, y, x - y))
    elif operator == "*":
        print ("{} * {} = {}".format(x, y, x * y))
    elif (operator == "/" or operator == "//" or operator == "%" ) and y==0:
        print 'integer division or modulo by zero'
    elif operator == "/" and y !=0:
        print ("{} / {} = {}".format(x, y, x / y))
    elif operator == "//" and y !=0:
        print ("{} // {} = {}".format(x, y, x // y))
    elif operator == "%" and y !=0:
        print ("{} % {} = {}".format(x, y, x % y))

    # If none of the above conditions were true then execute this by default
    else:
        print ("Use either + - * / or % next time")

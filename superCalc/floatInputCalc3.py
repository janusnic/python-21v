# -*- coding:utf-8 -*-
# ---------- CALCULATOR ----------
'''
To run under Python2 replace 'input' call
with 'raw_input'

'''
print('Super Calc')

# Convert strings into integers
x = float(input("Enter x: "))
y = float(input("Enter y: "))

# Store the user input an operator
operator = input('Enter Operator: ')

# If, else if (elif) and else execute different code depending on a condition
if operator == "+":
    print ("{} + {} = {}".format(x, y, x * y))

# If the 1st condition wasn't true check if this one is
elif operator == "-":
    print ("{} - {} = {}".format(x, y, x - y))
elif operator == "*":
    print ("{} * {} = {}".format(x, y, x * y))
elif operator == "/":
    if y==0:
        print('integer division or modulo by zero')
    else:
        print ("{} / {} = {}".format(x, y, x / y))
elif operator == "%":
    print ("{} % {} = {}".format(x, y, x % y))

# If none of the above conditions were true then execute this by default
else:
    print ("Use either + - * / or % next time")

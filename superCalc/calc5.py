# -*- coding:utf-8 -*-
# ---------- CALCULATOR ----------
'''
 Program make a simple calculator that can add, subtract, multiply and divide using functions
'''
print 'Super Calc'

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

   return x / y

def intdivide(x, y):
   """This function int divides two numbers"""

   return x // y

def modulo(x,y):
    """This function modulos two numbers"""

    return x % y

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
        print ("{} + {} = {}".format(x, y, add(x, y)))
    elif operator == "-":
        print ("{} - {} = {}".format(x, y, subtract(x, y)))
    elif operator == "*":
        print ("{} * {} = {}".format(x, y, multiply(x, y)))
    elif (operator == "/" or operator == "//" or operator == "%" ) and y==0:
        print 'integer division or modulo by zero'
    elif operator == "/" and y !=0:
        print ("{} / {} = {}".format(x, y, divide(x, y)))
    elif operator == "//" and y !=0:
        print ("{} // {} = {}".format(x, y, intdivide(x, y)))
    elif operator == "%" and y !=0:
        print ("{} % {} = {}".format(x, y, modulo(x, y)))

    # If none of the above conditions were true then execute this by default
    else:
        print ("Use either + - * / or % next time")

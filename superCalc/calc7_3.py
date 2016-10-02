# -*- coding:utf-8 -*-
# ---------- CALCULATOR ----------
'''
 Program make a simple calculator that can add, subtract, multiply and divide using functions
'''
print ('Super Calc')

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

def menu():
   print("Select operation.\n")
   print("+.Add")
   print("-.Subtract")
   print("*.Multiply")
   print("/.Divide\n")

   return str(input("Enter choice(+|-|*|/):"))

def myhelp():
   print ("""\
   Usage operation:
        'h'                        Display this usage message
        '+'                        Add
        '-'                        Subtract
        '*'                        Multiply
        '/'                        Divide
        'q'                        Quit
        """)

while True:
    # Convert strings into integers
    x = float(input("Enter x: "))
    y = float(input("Enter y: "))

    # Store the user input an operator

    operator = menu()

    if operator == 'q':
        print('{!r}'.format('Thankyou for using calculator.py!'))
        print('{!a}'.format('Thankyou for using calculator.py!'))
        print('{!s}'.format('Thankyou for using calculator.py!'))

        break

    if operator not in ('+','-','*','/','//','%','**'):
        # print ("Help: Use either + - * / or % next time")
        myhelp()
        continue

    if operator == "+":
        print ("{} + {} = {}".format(x, y, add(x, y)))
        print ("int: {0:d} hex: {0:x} + int: {1:d} hex: {1:x}  =  int: {2:d} hex: {2:x}".format(x, y, add(x, y)))
        print ("oct: {0:o} bin: {0:b} + oct: {1:o} bin: {1:b}  =  oct: {2:o} bin: {2:b}".format(x, y, add(x, y)))

    elif operator == "-":
        print ("{:+08.2f} - {:+08.2f} = {:+08.2f}".format(x, y, subtract(x, y)))
    elif operator == "*":
        print ("{0} * {k} = {1}".format(x, multiply(x, y), k=y))
    elif (operator == "/" or operator == "//" or operator == "%" ) and y==0:
        print ('integer division or modulo by zero')
    elif operator == "/" and y !=0:
        print ("{} / {} = {}".format(x, y, divide(x, y)))
    elif operator == "//" and y !=0:
        print ("{} // {} = {}".format(x, y, intdivide(x, y)))
    elif operator == "%" and y !=0:
        print ("{} % {} = {}".format(x, y, modulo(x, y)))

    # If none of the above conditions were true then execute this by default
    else:
        print ("Thankyou for using calculator.py!")

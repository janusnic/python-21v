# -*- coding:utf-8 -*-
# ---------- CALCULATOR ----------
'''
To run under Python3 replace 'raw_input' call
with 'input'
Store the user input an operator
'''
print 'Super Calc'

# Convert strings into integers
x = int(raw_input("Enter x: "))
y = int(raw_input("Enter y: "))

# Store the user input an operator
operator = raw_input('Enter Operator: ')

# Add the values entered and store in sum
sum = x + y

# Subtract the values and store in difference
difference = x - y

# Multiply the values and store in product
product = x * y

# Divide the values and store in quotient
# quotient = x / y

# Use modulus on the values to find the remainder
# remainder = x % y

# If, else if (elif) and else execute different code depending on a condition
if operator == "+":
    print ("{} + {} = {}".format(x, y, sum))

# If the 1st condition wasn't true check if this one is
elif operator == "-":
    print ("{} - {} = {}".format(x, y, difference))
elif operator == "*":
    print ("{} * {} = {}".format(x, y, product))
elif operator == "/":
    if y==0:
        print 'integer division or modulo by zero'
    else:
        print ("{} / {} = {}".format(x, y, x / y))
elif operator == "%":
    print ("{} % {} = {}".format(x, y, x % y))

# If none of the above conditions were true then execute this by default
else:
    print ("Use either + - * / or % next time")

# Other conditional operators
# > : Greater than
# < : Less than
# >= : Greater than or equal to
# <= : Less than or equal to
# != : Not equal to

# -*- coding:utf-8 -*-
# ---------- MATH ON 2 VALUES ----------
'''
To run under Python3 replace 'raw_input' call
with 'input'
'''
print 'Hello Super Calc'
x = int(raw_input("Enter x: "))
y = int(raw_input("Enter y: "))

# Add the values entered and store in sum
sum = x + y

# Subtract the values and store in difference
difference = x - y

# Multiply the values and store in product
product = x * y

# Divide the values and store in quotient
quotient = x / y

# Use modulus on the values to find the remainder
remainder = x % y

# Print your results
# format() loads the variable values in order into the {} placeholders
print ("{} + {} = {}".format(x, y, sum))
print ("{} - {} = {}".format(x, y, difference))
print ("{} * {} = {}".format(x, y, product))
print ("{} / {} = {}".format(x, y, quotient))
print ("{} % {} = {}".format(x, y, remainder))

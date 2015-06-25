from math import sqrt

#----------------------------------------------------------------------
def fibonacci(n):
    """
    http://stackoverflow.com/questions/494594/how-to-write-the-fibonacci-sequence-in-python
    """
    return ((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5))
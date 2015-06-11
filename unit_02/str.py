#  -*- coding: utf-8 -*- 

t = "Это не самый лучший способ объединения двух длинных строк, " + \
    "потому что он основан на использовании неуклюжего экранирования" 
s = ("Это отличный способ объединить две длинные строки, потому что он основан на конкатенации строковых литералов.")

print t
print s

print " " + \
"Usage: thingy [OPTIONS]" + \
"     -h                        Display this usage message" + \
"     -H hostname               Hostname to connect to" 

print ("Usage: thingy [OPTIONS] -h  Display this usage message -H hostname Hostname to connect to")


print """\ 
Usage: thingy [OPTIONS] 
     -h                        Display this usage message 
     -H hostname               Hostname to connect to 
""" 
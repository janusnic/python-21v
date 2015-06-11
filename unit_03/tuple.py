stock = ('GOOG', 100, 490.10)
address = ('www.python.org', 80) 
person = ('first_name', 'last_name', 'phone') 

a = () 
print type(a) 
b = ('item',) 
print type(b) 
c = 'item', 
print type(c)

print tuple('abc')

t = 1,[2,3]
t[1].append(4)
print t

v = ('a',2,True) 
(x,y,z) = v 
print x 
print y  
print z 

a_tuple = ("a","b","mpilgrim","z","example") 

a_list = list(a_tuple) 

print a_list

a_puble = (MONDAY,TUESDAY,WEDNESDAY,THURSDAY,FRIDAY,SATURDAY,SUNDAY) = range(7) 

print a_puble[MONDAY] 

print a_puble[SUNDAY] 
print SUNDAY
stock = ('GOOG', 100, 490.10)
address = ('www.python.org', 80) 
person = ('first_name', 'last_name', 'phone') 

print(stock)
print(address)
py_address = 'www.python.org', 443 #Python часто распознает кортежи, даже если они не заключены в круглые скобки
print(py_address)

# имеется возможность определять кортежи, содержащие 0 или 1 элемент
a = ()
print(type(a))
# Кортеж с нулевым количеством элементов (пустой кортеж) 
b = ('item',) # Кортеж с одним элементом (обратите внимание на запятую в конце) 
print(type(b))
c = 'item', # Кортеж с одним элементом (обратите внимание на запятую в конце)
print(type(c))
# прием распаковывания кортежей во множество переменных
name, shares, price = stock 
print(price)
host, port = address 
print(host)
first_name, last_name, phone = person 
print(phone)

a_tuple = ("a","b","mpilgrim","z","example")

print(a_tuple[0]) # Элементы кортежа заданы в определённом порядке, как и в списке
print(a_tuple[-1]) # Отрицательные значения индекса отсчитываются от конца кортежа
print(a_tuple[1:3]) # Создание среза кортежа

# Вы можете искать элементы в кортежи, поскольку это не изменяет кортеж.
print(a_tuple.index("example"))

# Вы не можете добавить элементы к кортежу. Кортежи не имеют методов append() или extend
a_tuple.append('new') 
# Вы не можете удалять элементы из кортежа. Кортежи не имеют методов remove() или pop
a_tuple.remove('z')


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

tup2 = (1, 2, 3, 4, 5, 6, 7 );
print "tup2[1:5]: ", tup2[1:5]


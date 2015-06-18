#!/usr/bin/env python

print('функция для создания строковых объектов class str:')
print(type(str())) # функция для создания строковых объектов class 'str'
print('возвращается строковое представление аргумента:')
print(str(1234)) # возвращается строковое представление аргумента
print('без аргументов возвращается пустая строка:')
print(str())
print('возвращается его копия:')
print(str("hello")) # возвращается его копия

print('экранировать символ перевода строки:')
print(str("Test 'test' can not, but \"test\" must"))

print(str('Test "test" can not, but \'test\' must have \\'))

print('Символы перевода строки:')
str1 = 'First line.\nSecond line.'  # \n means newline

print(str1)

print('C:\some\name')  # here \n means newline!

print (r'C:\some\name')  # note the r before the quote

print ("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")

print ("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")

print (" " + \
"Usage: thingy [OPTIONS]" + \
"     -h                        Display this usage message" + \
"     -H hostname               Hostname to connect to")

print ("Usage: thingy [OPTIONS] -h  Display this usage message -H hostname Hostname to connect to")
print('Экранированные последовательности в языке Python:')
str1 ="In the \rinteractive \\interpreter \
 "

str2 ="I\bn the interactive \vinterpreter, the output "

print (str1)
print (str2)

print('Сравнение строк ')
print('Получение срезов строк')
str1 ="отдельные элементы последовательности, а, следовательно, и отдельные символы в строках, могут извлекаться с помощью оператора доступа к элементам ([ ])"
str2 ="In the interactive interpreter, the output"

print (str1[1])
print (str2[9])
print (str2[1:9])
print (str2[-9])
print (str1[0:])
print (str1[:-1])
print (str1[:])
print (str2[0:])
print (str2[:-1])
print (str2[:])
print (str2[0:len(str2)])

print (str2[:12] + 'test' + str2[12:])
print (str2[:12] + str2[3:6] + str2[12:])

print(str2, str2[: :-1])

print(str2[0:12:1])
print(str2[::3])
print(str2[::-3])
print(str2[20::-3])
print(str2[50::-1])

# concotenation
print('concotenation')
str3 = ["In the interactive", "interpreter", "the output"]
print(str2+str3[0])
str2+=str3[2]
print(str2)

print(*str3[1])
print(3 * 'un' + 'ium')
print(80 * '#')
print ('Py' 'thon')
prefix = 'Py'
print(prefix + "thon")

text = ('Put several strings within parentheses '
            'to have them joined together.')
print(text)
print("".join(str3))
print("-".join(str3))
print(" ".join(str3))

print(str2.capitalize())
print(str2.center(80))
print(str2.center(80,'#'))
print(str2.count('the'))
print(str2.count('the',3,20))
print(str2.encode())
print(str2.encode('utf-8'))
print(str2.encode('ascii'))

print(str2.endswith('output'))
print(str2.endswith(('the', 'output')))
print(str2.startswith('inter'))

print('find')
print(str2.find('the'))
print(str2.find('the',5,20))
print(str2.find('the',5,8))
print(str2.rfind('the'))
print(str2.index('the'))

st1 = "123456"
st2 = "Abcd"
st4 = "ABC"
st3 = "   "
print(st1.isalnum())
print(st2.isalpha())
print(str2.isdigit())

print(str2.islower())
print(st1.isspace())
print(st3.isspace())
print(st2.isupper())
print(st4.isupper())


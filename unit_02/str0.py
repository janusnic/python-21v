#!/usr/bin/python

# 1.py str()

print(str(1234))
print(str())
print(str("hello")) 

print(str("Test 'test' can not, but \"test\" must"))

print(str('Test "test" can not, but \'test\' must'))

str1 = 'First line.\nSecond line.'  # \n means newline
print(str1)

print('C:\some\name')  # here \n means newline!

print r'C:\some\name'  # note the r before the quote

print """\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
"""


print " " + \
"Usage: thingy [OPTIONS]" + \
"     -h                        Display this usage message" + \
"     -H hostname               Hostname to connect to"

print ("Usage: thingy [OPTIONS] -h  Display this usage message -H hostname Hostname to connect to")

str1 ="In the \rinteractive \\interpreter \
 "

str2 ="I\bn the interactive \vinterpreter, the output "

print (str1)
print (str2)

2 ="In the interactive interpreter, the output"

print (str1[1])
print (str2[9])
print (str2[1:9])
print (str2[-9])
print (str2[0:])
print (str2[:-1])
print (str2[:])
print (str2[0:len(str2)])

str2 ="In the interactive interpreter, the output"

print (str2[:12] + 'test' + str2[12:])
print (str2[:12] + str2[3:6] + str2[12:])

str2 ="In the interactive interpreter, the output"

print(str2[0:12:1])
print(str2[::3])
print(str2[::-3])
print(str2[20::-3])
print(str2[50::-1])

str2 = ["In the interactive", "interpreter", "the output"]

print("".join(str2))
print("-".join(str2))
print(" ".join(str2))

str2 = "interpreter the output"

print(str2.capitalize())
print(str2.center(30))
print(str2.center(30,'#'))
print(str2.count('the'))
print(str2.count('the',3,20))
print(str2.encode())
print(str2.encode('utf-8'))
print(str2.encode('ascii'))

print(str2.endswith('output'))
print(str2.endswith(('the', 'output')))
print(str2.startswith('inter'))

str2 = "interpreter the output"

print(str2.find('the'))
print(str2.find('the',5,20))
print(str2.find('the',5,8))
print(str2.rfind('the'))
print(str2.index('the'))

str2 = "interpreter the output"
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

print(3 * 'un' + 'ium')

print ('Py' 'thon')
prefix = 'Py'
print(prefix + "thon")

text = ('Put several strings within parentheses '
            'to have them joined together.')
print(text)

def extract_from_tag(tag, line):
	opener = '<' + tag + '>'
	closer = '</' + tag + '>'
	try:
		i = line.index(opener)
		start = i + len(opener)
		j = line.index(closer, start)
		return line[start:j]
	except ValueError:
		return None



line = "<h2>interpreter the output</h2>"
tag = 'h2'

print(extract_from_tag(tag, line))

print(u'Hello\u0020World !')

filename = "image.jpg"

if filename.lower().endswith((".jpg", ".jpeg")): 
    print(filename, "is a JPEG image'") 

s = "\t no parking " 

print(s.lstrip())
print(s.rstrip())
print(s.strip())

s = "<[unbracketed]>"

print(s.strip("[](){><>"))


record = "Leo Tolstoy*1828-8-28*1910-11-20" 
fields = record.split("*") 
print(fields)
# ['Leo Tolstoy', '1828-8-28', '1910-11-20'] 
born = fields[1].split('-')  
# born 
# ['1828', '8', '28'] 
died = fields[2].split('-') 
print('lived about', int(died[0]) - int(born[0]), "years") 
# lived about 82 years 


record = "The novel {0} was published in {1}".format("Hard Times", 1854) 

print(record)
# "The novel Hard Times was published in 1854" 

record ="{0}{1}".format("The amount due is $", 200) 
print(record)

x = "three" 
s ="{0} {1} {2}" 
s = s.format("The", x, "tops")
print(s) 
# 

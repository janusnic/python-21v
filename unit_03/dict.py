a_dict = {'server': 'localhost','database':'mysql'}

print(a_dict)
print(a_dict['server'])
print(a_dict['database'])

a_dict = {'server': 'localhost','database':'mysql'}

print(a_dict)
print(a_dict['server'])
print(a_dict['database'])

a_dict['database'] = 'blog'
print(a_dict['database'])

a_dict['user'] = 'root'
print(a_dict['user'])

print(a_dict)

a_dict = {'server': 'localhost','database':'mysql',1000:['KB','MB','GB'],1024:['KiB','MiB','GiB']}

print(a_dict)
print(len(a_dict))

if 1000 in a_dict:
  print('1000 in dict')
else:
  print('not in dict')

print(a_dict[1000])

print(a_dict[1024])

print(a_dict[1024][2])


a_dict = {'server': 'localhost','database':'mysql',1000:['KB','MB','GB'],1024:['KiB','MiB','GiB']}

def is_it_true(anything):
  if anything:
    print('in dict')
  else:
    print('not in dict')

is_it_true({})
is_it_true({'a':1})
is_it_true(a_dict)






h1 = {1:"one", 2:"two", 3:"three"}
h2 = {0:"zero", 5:"five"}
h3 = {"z":1, "y":2, "x":3}

for key, value in h1.items():
    print key, " ", value

for key in h2.keys():
    print key, " ", h2[key]

for v in h3.values():
    print v

h1.update(h3)

print len(h1)

dic = {'key1': {'key3':5}, 'key2': {'key4':6}}

for key, value in dic.items():
    print key, " ", value
    for k, v in value.items():
    	print k, ' ', v

s={1:'one',2:'two'}

for k, v in s.iteritems():
    print k, v

my_list = [1,2,3,4,1,2,6,9,2,3,8,4,5,76,2,5,6,7]
unique_list = list(set(my_list))
print unique_list

a = [1,2,3,4,1,2,6,9,2,3,8,4,5,76,2,5,6,7]
b = [ e for i,e in enumerate(a) if e not in a[i+1:] ]
print b

a = [1,2,3,4,1,2,6,9,2,3,8,4,5,76,2,5,6,7]
b = [ e for i,e in enumerate(a) if e not in a[:i] ]
print b

print '_'*80
#-----------------------------
# dictionaries
age = {"Nat": 24,
       "Jules": 24,
       "Josh": 17}
#-----------------------------
age = {}
age["Nat"] = 24
age["Jules"] = 25
age["Josh"] = 17

for k, v in age.iteritems():
    print k, v
print '_'*80
#-----------------------------
food_color = {"Apple":  "red",
              "Banana": "yellow",
              "Lemon":  "yellow",
              "Carrot": "orange"
             }
#-----------------------------
# NOTE: keys must be quoted in Python
for k, v in food_color.iteritems():
    print k, v

print '_'*80

# Adding an Element to a Hash

#  mydict[key] = value
#-----------------------------
# food_color defined per the introduction
food_color["Raspberry"] = "pink"
print "Known foods:"
for food in food_color:
    print food

#=> Known foods:
#=> Raspberry
#=> Carrot
#=> Lemon
#=> Apple
#=> Banana
#-----------------------------
print '_'*80

# Testing for the Presence of a Key in a Hash

# does mydict have a value for key?
# if key in mydict:
#    pass # it exists
# else:
#    pass # it doesn't

#-----------------------------
# food_color per the introduction
for name in ("Banana", "Martini"):
    if name in food_color:
        print name, "is a food."
    else:
        print name, "is a drink."

print '_'*80
#=> Banana is a food.
#=> Martini is a drink.
#-----------------------------
age = {}
age["Toddler"] = 3
age["Unborn"] = 0
age["Phantasm"] = None

for thing in ("Toddler", "Unborn", "Phantasm", "Relic"):
    print ("%s:"%thing),
    if thing in age:
        print "Exists",
        if age[thing] is not None:
            print "Defined",
        if age[thing]:
            print "True",
    print
print '_'*80
#=> Toddler: Exists Defined True
#=> Unborn: Exists Defined
#=> Phantasm: Exists
#=> Relic:
#-----------------------------
res = []
for x in xrange(1, 25, 2):
    res.append(x)
print res 

print '_'*80

res = [x for x in xrange(1, 25, 2)]
print res 

print '_'*80

res = [x**2 for x in xrange(1, 25, 2)]
print res 

print '_'*80

res = [x**2 for x in xrange(1, 25, 2) if x % 3 != 0]
print res 

print '_'*80

dic = {'John':1200, 'Paul':1000, 'Jones':1850, 'Dorothy': 950}
print "\n".join(["%s = %d" % (name, salary) for name, salary in dic.items()])
print '_'*80


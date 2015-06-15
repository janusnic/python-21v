a_set = {'MONDAY',1,'TUESDAY',55,'WEDNESDAY','THURSDAY','FRIDAY','SATURDAY','SUNDAY'}

print(type(a_set))

print(a_set)

print('SUNDAY' in a_set)

a_list = ['MONDAY',1,'TUESDAY',55,'WEDNESDAY','THURSDAY','FRIDAY','SATURDAY','SUNDAY']

a_set = set(a_list)
print(type(a_set))

print(a_set)


a_set = set()
print(type(a_set))
print(len(a_set))


a_set = set()
print(type(a_set))
a_set.add(4)
print(len(a_set))
print(a_set)
a_set.add(1)
print(len(a_set))
print(a_set)

a_set.add(1)
print(len(a_set))
print(a_set)


a_set = {1,2,3}
print(type(a_set))
a_set.update({4})
print(len(a_set))
print(a_set)
a_set.update({1})
print(len(a_set))
print(a_set)

a_set.update({11,44,4,7,9})
print(len(a_set))
print(a_set)

a_set.update([111,41,4,7,9])
print(len(a_set))
print(a_set)

a_set = {1,2,3}
a_set.update({11,44,4,7,9})
a_set.update([111,41,4,7,9])
print(len(a_set))
print(a_set)

a_set.discard(111)
print(len(a_set))
print(a_set)

a_set.remove(11)
print(len(a_set))
print(a_set)

a_set = {1,2,3,11,44,4,7,9}

print(len(a_set))
print(a_set)

a_set.pop()
print(len(a_set))
print(a_set)


a_set = {1,2,3,11,44,4,7,9}

print(len(a_set))
print(a_set)
a_set.clear()
print(len(a_set))
print(a_set)

a_set.pop()
print(len(a_set))
print(a_set)


a_set = {1,2,3,11,44,4,7,9}

print(len(a_set))
print(a_set)

if 30 in a_set:
	print('Ok')
else:
	print('Nop')

if 44 in a_set:
	print('Yes')
print(a_set)



a_set = {1,2,3,11,44,4,7,9}
b_set = {21,22,23,111,744,48,79,99}

print(len(a_set))
print(a_set)

c_set = a_set.union(b_set)

print(len(a_set))
print(a_set)

print(len(c_set))
print(c_set)



a_set = {1,2,3,11,44,4,7,9}
b_set = {21,1,4,11,2,23,111,744,48,79,9}


print(a_set)
print(b_set)
c_set = a_set.intersection(b_set)

print(len(c_set))
print(c_set)



a_set = {1,2,3,11,44,4,7,9}
b_set = {21,1,4,11,2,23,111,744,48,79,9}


print(a_set)
print(b_set)
c_set = a_set.symmetric_difference(b_set)

print(len(c_set))
print(c_set)

d_set = b_set.symmetric_difference(a_set)

print(len(d_set))
print(d_set)

if c_set == d_set: 
	print('symmetric')

if b_set.union(a_set) == a_set.union(b_set):
	print('symmetric')

if b_set.difference(a_set) == a_set.difference(b_set):
	print('symmetric')
else:
	print('not symmetric')



a_set = {1,2,3,11,44,4,7,9}
b_set = {21,1,4,11,2,3,111,7,44,79,9}


print(a_set)
print(b_set)

if a_set.issubset(b_set): 
	print('Yes')
else:
	print('not')

if b_set.issuperset(a_set):
	print('Yes')
else:
	print('not')

a_set.add(5)
if a_set.issubset(b_set): 
	print('Yes')
else:
	print('not')

if b_set.issuperset(a_set):
	print('Yes')
else:
	print('not')




a_set = {1,2,3,11,44,4,7,9}

def is_it_true(anything):
	if anything:
		print('Yes')
	else:
		print('Nop')

is_it_true(set())

is_it_true({'a'})

is_it_true(a_set)


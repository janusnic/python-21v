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




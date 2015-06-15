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





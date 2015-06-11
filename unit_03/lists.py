# -*- coding utf-8 -*-
a_list = []
print a_list

a_list = ['a','b','mpilgrim','z','example']

print a_list

print a_list[1:3]
print a_list[1:-1]
print a_list[:-1]
print a_list[:3]

print a_list

a_list = a_list + [2.0,3]

print a_list

a_list.append(True)
print a_list

a_list.extend(['four','w'])
print a_list

print a_list[-1]

a_list.insert(0,'w')
print a_list
print len(a_list)
a_list.append(['g', 'h', 'i'])
print len(a_list)
print a_list[-1]

print a_list.count('w')

print a_list.index('w')

del a_list[0]
print a_list.index('w')

print 'w' in a_list
print 'w' not in a_list

a = ['Dave', 'Mark', ['Dave', 2, 99, [100,200]], 'Ann', [22, 33 ,77],'Phil'] 
print a[1] 
print a[2][2] 
print a[2][3][1] 

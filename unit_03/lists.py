# -*- coding utf-8 -*-
a_list = []
print a_list

names = ['Dave', 'Mark', 'Ann', 'Phil']


print(names[2])


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

a.sort()
print a

print a*2
print '--'*40
print a
print '--'*40
a.reverse()
print a

l = range(80)
print '--'*40
for x in sorted(l):
	print x,

print '--'*40

for x in reversed(l):
	print x,

print '--'*40

for x in set(l):
	print x,

print '--'*40

l2 = l[0:-1:3]
for x in set(l).difference(l2):
	print x,

print '--'*40

a1 = [ i*i for i in range(1,10)]
print a1

print '--'*40
a1 = [ i*i for i in range(1,10) if i % 2 == 0]

print a1

print '--'*40

words = ' to perform the task of sorting the words in a string by their length'.split()
wordlens = [(len(word), word) for word in words]
wordlens.sort()
print ' '.join(w for (_, w) in wordlens)

print '--'*40

stack = [1,2,3,4,5]  
print stack
stack.append(6)
print stack
stack.append(7)
print stack
stack.pop()
print stack
print '--'*40

queue = ['rock','in','roll']  
print queue
queue.append('alive')
print queue
queue.pop(0)
print queue

print '--'*40
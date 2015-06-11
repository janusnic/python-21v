import random
 
a = []
for i in range(20):
	n = round(random.random() * 100) 
	a.append(n)
print("A =",a)
 
b = []
i = 0
while i < len(a):
	if 35 < a[i] < 65:
		b.append(a[i])
		del a[i]
	else:
		i += 1
print("A =",a)
print("B =",b)
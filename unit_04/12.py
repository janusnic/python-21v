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


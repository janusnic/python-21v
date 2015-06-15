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

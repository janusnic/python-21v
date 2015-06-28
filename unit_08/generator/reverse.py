# -*- coding:utf-8 -*-
def reverse(data):
    new_data = list(data)
    new_data.reverse()
    for item in new_data:
        yield item
 
rev = reverse("string")
print rev # <generator object reverse at 0x7fa00b285aa0>

print [char for char in rev] # ['g', 'n', 'i', 'r', 't', 's']
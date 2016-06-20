# -*- coding:utf-8 -*- 
# Decart
colors = ['black', 'white']
sizes = ['S', 'M', 'L']
tabs = [(color, size) for color in colors for size in sizes]
print(tabs) # [('black', 'S'), ('black', 'M'), ('black', 'L'), ('white', 'S'), ('white', 'M'), ('white', 'L')]

for tab in ('%s %s' % (color, size) for color in colors for size in sizes):
    print(tab)

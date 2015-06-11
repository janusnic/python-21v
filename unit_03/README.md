# python-21v

# Списки

# Создание списка
<pre>
a_list = []
a_list = ['a','b','mpilgrim','z','example']
</pre>

# slicing: Разрезание списка
<pre>
a_list[1:3]
a_list[1:-1]
a_list[:-1]
a_list[:3]

</pre>

# Добавление элементов в список
<pre>
a_list = ['a'] 
a_list =a_list + [2.0, 3]
a_list
['a', 2.0, 3] 
a_list.append(True)
a_list.extend(['four','Ω'])
a_list.insert(0, 'Ω')

</pre>

# Поиск значений в списке
<pre>

a_list.count('new') 
'new' in a_list 
'new' not in a_list 
a_list.index('mpilgrim')
</pre>

# Удаление элементов из списка 
<pre>
a_list =['a', 'b', 'new', 'mpilgrim', 'new'] 
del a_list[1] 

a_list.remove('new')

a_list.pop() 

a_list.pop(0)

</pre>

# Список может содержать объекты любого типа, включая другие списки

<pre>
a = ['Dave', 'Mark', ['Dave', 2, 99, [100,200]], 'Ann', [22, 33 ,77],'Phil'] 
print a[1] 
print a[2][2] 
print a[2][3][1] 

</pre>



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
</pre>
# Элемент можно добавить в произвольную позицию списка с помощью метода insert:
a_list.insert(0, 'Ω')


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

# Можно менять как отдельные элементы списка, так и диапазон:
<pre>
lst[3] = 'piano'
lst[0:2] = [1,2]
lst
[1, 2, 100, 'piano']
</pre>
# Вставка:
<pre>
lst[1:1] = ['guitar','microphone']
lst
[1, 'guitar', 'microphone', 2, 100, 'piano']
</pre>
# Можно сделать выборку из списка с определенной частотой:
<pre>
numbers = [1,2,3,4,5,6,7,8,9,0]
numbers[::4]
[1, 5, 9]
</pre>
# Создание копии списка.
<pre>
L1 = L2[:] — создание второй копии списка. Здесь создается вторая копия обьекта.
L1 = list(L2) — тоже создание второй копии списка.
L1 = L2 — создание второй ссылки, а не копии. 3-й вариант показывает, что создаются две ссылки на один и тот же обьект, а не две копии.
</pre>

# Умножение, или повтор списков:
   L1 * 2

# sort() — сортировка списка:

lst.sort()

# reverse() — реверс списка:
lst.reverse()

# len() — длина списка:
len(lst)

# max() — максимальный элемент списка:
max(lst)

# min() — минимальный элемент списка:
min(lst)

# простая итерация списка:
  for x in L:

# сортированная итерация:
  for x in sorted(L):

# уникальная итерация:
  for x in set(L):

# итерация в обратном порядке:
  for x in reversed(L):
# исключающая итерация — например, вывести элементы 1-го списка, которых нет во 2-м списке:
  for item in set(L).difference(L2)

# Для генерации списков, кроме статической формы, можно использовать конструктор списков — list comprehension — цикл внутри квадратных скобок — на примере списка квадратов первых 10 натуральных чисел:

a = [ i*i for i in range(1,10)]

# Конструктор может быть условным — найдем квадраты четных натуральных чисел:

a = [ i*i for i in range(1,10) if i % 2 == 0]

# С помощью конструктора решим конкретную задачу — отсортируем слова в предложении в порядке их длительности:
<pre>

words = ' to perform the task of sorting the words in a string by their length'.split()

wordlens = [(len(word), word) for word in words]
wordlens.sort()
print ' '.join(w for (_, w) in wordlens)

</pre>

# Операция Sequence unpacking — присваивание списку переменных списка значений:

a, b = [1,2]

# Стек и очереди
## Список можно использовать как стек — когда последний добавленный элемент извлекается первым (LIFO, last-in, first-out). Для извлечения элемента с вершины стека есть метод pop():
<pre>
stack = [1,2,3,4,5]  
stack.append(6)
stack.append(7)
stack.pop()
stack
</pre>
## Список можно использовать как очередь — элементы извлекаются в том же порядке, в котором они добавлялись (FIFO, first-in, first-out). Для извлечения элемента используется метод pop() с индексом 0:
<pre>
queue = ['rock','in','roll']  
queue.append('alive')
queue.pop(0)
queue
['in', 'roll', 'alive']
</pre>

# Кортежи (Tuple)
Кортеж — это неизменяемый список. Кортеж не может быть изменён никаким способом после его создания. 
Для создания простейших структур данных можно использовать кортежи, которые позволяют упаковывать коллекции значений в единый объект. Кортеж создается заключением группы значений в круглые скобки, 
<pre>
a = () 
print(type(a)) 
# Кортеж с нулевым количеством элементов (пустой кортеж) 
b = ('item',) # Кортеж с одним элементом (обратите внимание на запятую в конце) 
print(type(b)) 
c = 'item', # Кортеж с одним элементом (обратите внимание на запятую в конце) 
print(type(c))
print tuple('abc')

t = 1,[2,3]
t[1].append(4)
print t
</pre>
# Кортежи могут быть преобразованы в списки и наоборот.
<pre>
a_tuple = ("a","b","mpilgrim","z","example") 

a_list = list(a_tuple) 

print(a_list[0]) 
print(a_list[-1]) 
print(a_list[1:3]) 
a_list.append('new') 
print(a_list[1:]) 
a_list.remove('z') 
print(a_list[1:]) 

a_tuple1 = tuple(a_list) 
print(a_tuple1[0]) 
print(a_tuple1[-1]) 
print(a_tuple1[1:]) 
</pre>

# Присваивание нескольких значений за раз
<pre>
v = ('a',2,True) 
(x,y,z) = v 
print(x) 
print(y) 
print(z)

a_puble = (MONDAY,TUESDAY,WEDNESDAY,THURSDAY,FRIDAY,SATURDAY,SUNDAY) = 
range(7) 

print(a_puble[MONDAY]) 

print(a_puble[SUNDAY]) 
print(SUNDAY)


</pre>
# Получение данных из кортежа
<pre>
tup2 = (1, 2, 3, 4, 5, 6, 7 );
print "tup2[1:5]: ", tup2[1:5]
</pre>

# Множества Сеты (Set)

# Сгенерировать сет можно с помощью функции:
s = set('abcde')


# Над сетами можно выполнять разные операции, например вычитание:
s3 = s - s2
# сложение:
s3 = s | s2
# пересечение:
s3 = s & s2

# Сеты имеют встроенные функции:
# add() — добавление элемента:
s.add(6)
# remove() — удаление элемента:
s.remove('a')
# Итерация:
for item in s:print (item)
#Сеты можно использовать для фильтрации дублей в коллекциях. Для этого коллекцию нужно сконвертировать в сет, а потом обратно:
<pre>
L = [1,2,3,4,1,2,6,7]
set(L)
set([1, 2, 3, 4, 6, 7])
L = list(set(L))
L
</pre>

# Сеты можно использовать для работы с большими наборами данных:

допустим, у нас имеются базы данных программистов и менеджеров:
<pre>
programmers = set(['ivanov','petrov','sidorov'])
managers = set(['ivanov','moxov','goroxov'])
</pre>
Найти тех, кто одновременно и программист, и менеджер:
<pre>
programmers & managers
set(['ivanov'])
</pre>
# Найти всех программистов и менеджеров:
<pre>
programmers | managers
set(['ivanov', 'petrov', 'sidorov', 'goroxov', 'moxov'])
</pre>
# Найти программистов, которые не менеджеры:
<pre>
programmers - managers
set(['petrov', 'sidorov'])
</pre>

# Словари
Словарь — это неупорядоченное множество пар ключ—значение. Когда вы добавляете ключ в словарь, вы также должны добавить и значение для этого ключа. (Значение всегда можно изменить позже.) Словари в Python оптимизированы для получения значения по известному ключу, но не для других целей. 

# in() — оператор проверки вхождения.
Пример: база данных может быть заполнена в виде словаря.
Проверить наличие в базе данных телефона по имени:
<pre>
people = {'Alice': {'phone': '2341', 'addr': 'Foo drive 23' },
          'Beth':  {'phone': '9102', 'addr': 'Bar street 42'}}
name = 'Alice'          
key = 'phone'
if name in people: 
  print "%s phone is %s" % (name, people[name][key])
 </pre>


# copy()
Пример создания копии словаря:
<pre>
x = {"user":'admin','attr':[1,2,3]}
y = x.copy()
y

</pre>
Метод copy() не делает полного копирования: если мы, например, сделаем операцию:
x['attr'].remove(1)
то с удивлением обнаружим, что удаление атрибута произойдет также и в копии.
Чтобы этого не произошло, нужно использовать метод deepcopy().
from copy import deepcopy
y = x.deepcopy()

# fromkeys() — создает словарь по заданным ключам с пустыми значениями:
{}.fromkeys(['name', 'age'])

# Можно все значения заполнить по умолчанию:
{}.fromkeys(['name', 'age'],123)

# get() — получает значение по ключу, в случае отсутствия дает None:

d = {}
print d.get('name')

# has_key() — проверяет, есть ли в словаре значение по данному ключу:
d = {}
d.has_key('name')

# items() — возвращает список значений:
<pre>
for key, value in d.items():
        print(key, value)
</pre>
# iteriyems() — возвращает итератор — выдает тот же результат:
<pre>
for k, v in d.iteritems():
...     print k, v
</pre>
# keys() — возвращает список ключей;
# iterkeys() — возвращает итератор ключей:
d.keys()

d.iterkeys()

# pop() — извлекает значение по ключу с последующим удалением:
d.pop('title')

# popitem() — извлекает произвольное значение с последующим удалением:
d = {'title': 'Python Web Site', 'url': 'http://www.python.org', 'www': 'python'}
d.popitem()


# update() — изменяет значение по ключу:
d2 = {'www':'python.org'}
d.update(d2)
# values() — возвращает список значений:
<pre>
d={}
d[1]=1
d[2]=2
d[3]=3
d

d.values()
</pre>
# del — оператор удаляет пару ключ: значение по ключу:
del d[2]


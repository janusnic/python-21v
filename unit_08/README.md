# Итераторы и генераторы

# Итераторы

Итераторы используются для прохождения по какому-нибудь контейнеру без учета особенностей его внутреннего строения. Обычно итераторы используются в циклах типа foreach Создадим простейший итератор вручную: 
<pre>
testIt = iter([1, 2, 3, 4, 5]) 
print [x for x in testIt] 


it = iter("string")
for i in it:
    print i
</pre>
функция iter() может принимать не только структуру данных, но и два совсем других аргумента: функцию без аргументов и стоповое значение, на котором итерация остановится. Пример: 
<pre>
def getSimple(state=[]): 
  if len(state) < 4: 
    state.append(" ") 
    return " " 

testIt2 = iter(getSimple, None) 
print [x for x in testIt2] 
</pre>
В классах, реализующих итераторы, должны быть определены методы __iter__() и next() (__next__()). __iter__() возвращает ссылку на итерируемый объект-контейнер, а next() при каждом вызове должен возвращать следующий элемент и бросать исключение StopIteration, если все элементы уже обработаны.
<pre>
class Iterable():
    def __init__(self, data):
        self.it = iter(data)
    def next(self):
        return self.it.next()
 
class Iterator():
    def __init__(self, data):
        self.data = data
    def __iter__(self):
        return Iterable(self.data)
 
it = Iterator("string")
it.next() # такого метода нет - он определен в Iterable
Traceback (most recent call last):
 AttributeError: Iterator instance has no attribute 'next'

[char for char in Iterator("string")]
['s', 't', 'r', 'i', 'n', 'g']

class Reverse:
    def __init__(self, data):
        self.data = data
        self.index = len(data)
    def __iter__(self):
        return self
    def next(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]
 
[char for char in Reverse("string")]
['g', 'n', 'i', 'r', 't', 's']

# По умолчанию, итераторы однонаправленные и не возобновляемые:

it = iter(range(10))

[i for i in it]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

[i for i in it]
[]

it = iter(range(10))
zip(it, it)
[(0, 1), (2, 3), (4, 5), (6, 7), (8, 9)]
</pre>
# Генераторы и итераторы

Генераторы списков, будучи по своей природе циклами for, очень тесно связаны с инструментами функционального программирования (такими как функции map и filter).
Функции map, zip и лямбда (называются "функции высшего порядка" или "first-class-functions") позволяют достаточно просто выполнять различные манипуляции с данными, для чего в "обычном" процедурном стиле приходится писать немного больше кода.

Простая задача есть список a = [1, 2] и список b = [3, 4] одинаковой длины и нужно слить их парами. Проще простого - используя функцию zip :
<pre>
a = [1,2]
b = [3,4]
print zip(a,b)
[(1, 3), (2, 4)]
или тройками :

a = [1,2]
b = [3,4]
c = [5,6]
print zip(a,b,c)
[(1, 3, 5), (2, 4, 6)]
или в более общем виде

list = [a, b, c]
print zip(*list)
[(1, 3, 5), (2, 4, 6)]
</pre>
Звездочка * перед list говорит что передается список аргументов, т.е. Действовать эквивалентно тому как если бы передали a, b, c т.е. Можно даже так print zip(*[a, b, c]) результат не изменится.
<pre>
# функция – map, когда нужно применить какую-либо функцию к каждому элементу списка.

def f(x):
    return x*x

nums = [1, 2, 3]
for num in nums:
    print f(num)

list comprehensions :

def f(x):
    return x*x
print [f(num) for num in nums]

проще :

def f(x):
    return x*x
print map(f, nums)

при условии конечно, что функцию можно записать лямбдой:

print map(lambda x: x*x, nums)
</pre>

map применяет какую-либо функцию к списку и возвращает результат в виде списка. Вы можете передать несколько списков, тогда функция (идущая первым параметром) должна принимать несколько аргументов (по количеству списков переданных в map).
<pre>
def f(x, y):    
    return x*y

a = [1,3,4]
b = [3,4,5]
print map(f, a, b)
[3, 12, 20]

</pre>
Однако если списки разной длины, т.е. Один короче другого, то он будет дополнен значениями None до нужной длины. Если убрать из списка b последнее значение – пример не будет работать, т.к. В функции f произойдет попытка умножения числа на None, и питоне не позволяет это делать. Поэтому если функция f достаточно объемна, неплохо бы проверять передаваемые значения. Например ;
<pre>
def f(x, y):
    if (y == None):
        y = 1    
    return x*y
Если же заместо функции стоит None – то map действует примерно так же как и zip, но если передаваемые списки разной длины в результат будет писаться None – что кстати очень уместно в некоторых моментах.

a = [1,3,4]
b = [3,4]
print map(None, a, b)
[(1, 3), (3, 4), (4, None)]
</pre>
# лямбда функции в python. 
Они используются когда вам необходимо определить функцию без исподьзования def func_name(): ...,. Поэтому функцию можно определить “на месте” f = lambda x: x*x  говорит нам – принимает x, возвращает x*x

Так используя стандартные инструменты питона можно записать довольно сложные действия в одну строчку. К примеру функцию :
<pre>
def f(x, y):
    if (y == None):
        y = 1    
    return x*y
можно представить как :

lambda x, y: x * (y if y is not None else 1)
</pre>
передавать списки отсортированные по длине – len(a) > (b) – воспользуемся функцией sorted :
<pre>
sorted([a, b], key=lambda x: len(x), reverse=True)
фунция sorted принимает список значений ([a,b] = [[1,2],[2,4,5]]) и сортирует по ключу key – который у нас задан функцией len(x) - возвращающей длину списка, сортируем в порядке убывания (reverse=True)

В конечном итоге вся операция записывается таким образом :

map(lambda x, y: x * (y if y is not None else 1), *sorted([a, b], key=lambda x: len(x), reverse=True))
списки a и b могут быть разной длины и передаваться в каком угодно порядке. Лямбда-выражения удобны для определения не очень сложных функций, которые передаются затем другим функциям.
</pre>
# Генераторы

Генераторы — это «ленивые» итераторы — функции, возвращающие следующий элемент тогда, когда он запрашивается. В генераторах запоминается точка выхода из функции и при следующем обращении работа функции продолжается с места выхода.

Для создания генераторов используют функции, содержащие в своем теле ключевое слово «yield» — такие функции возвращают объект-генератор.
<pre>
def reverse(data):
    new_data = list(data)
    new_data.reverse()
    for item in new_data:
        yield item
 
rev = reverse("string")
rev
generator object reverse at 0x7fa00b285aa0

[char for char in rev]
['g', 'n', 'i', 'r', 't', 's']

Для сравнения — пример реализации функции map с помощью итераторов и с помощью генераторов:

# функция map, реализованная с помощью итераторов

def map(func, iterable):
    result = []
    for item in iterable:
        result.append(func(item))
    return result
 
# функция map, реализованная с помощью генераторов   

def gmap(func, iterable):
    for item in iterable:
        yield func(item)
 
def map(func, iterable):
    return list(gmap(func, iterable))

it = iter(range(10))

print map(lambda x: x*x,it)

Генератор может возвращать результат бесконечное количество раз:

def random(min_val=0, max_val=100):
    import random as rand
    rand.seed()
    while True:
        yield rand.randint(min_val, max_val)
 
[r for (r, i) in zip(random(), xrange(20))]
[42, 17, 35, 96, 31, 11, 18, 9, 81, 78, 35, 71, 14, 12, 28, 24, 62, 67, 61, 49]

Для list comprehensions так же существует аналог, возвращающий объект-генератор. Для этого выражение нужно заключить не в квадратные, а в круглые скобки:

[r for (r, i) in zip(random(), xrange(20))]
[21, 35, 95, 20, 42, 88, 70, 72, 69, 50, 74, 52, 86, 26, 16, 39, 0, 63, 27, 21]

(r for (r, i) in zip(random(), xrange(20)))
generator object genexpr at 0x7fa00b298050

g = _
[r for r in g]
[94, 23, 55, 17, 23, 50, 56, 44, 79, 30, 58, 1, 85, 46, 88, 99, 95, 2, 81, 44]

Генераторы занимают в памяти меньше места, чем списки, так как каждый раз в ячейке памяти хранится только один результат, когда список требует память для храниения всех своих значений. Поэтому в циклах всегда для генерации последовательности чисел лучше использовать функцию «xrange», так как она возвращает генератор, в отличие от «range», которая возвращает список:

range(10)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

xrange(10)
xrange(10)

r = _
[i for i in r]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
</pre>
# itertools

import itertools
Например, для генерации бесконечных последовательностей в модуле есть следующие функции:
itertools.count(start=0, step=1) возвращает бесконечный генератор, который считает начиная от start с шагом step;
itertools.cycle(iterable) возвращает бесконечно повторяемую последовательность из iterable;
itertools.repeat(element, times=0) повторяет элемент, если times задано, то times раз;
<pre>
c = itertools.count()
[r for (r, i) in zip(c, xrange(20))]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

c = itertools.cycle("spam")
[r for (r, i) in zip(c, xrange(10))]
['p', 'a', 'm', 's', 'p', 'a', 'm', 's', 'p', 'a']

c = itertools.repeat(None)
[r for (r, i) in zip(c, xrange(10))]
[None, None, None, None, None, None, None, None, None, None]

Для контроля генераторов, выполняющихся бесконечно, можно использовать itertools.takewhile(), которая принимает лямбда-функцию и генерирует значения, пока лямбда-функция возвращает истину:

g = itertools.takewhile(lambda n: n&lt;10, itertools.count())
[i for i in g]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

Или с помощью itertools.islice():

c = itertools.count()
c = itertools.islice(c, 10)
[i for i in c]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

Функция, выполняющая противоложное для itertools.takewhile() — это itertools.dropwhile(). Она пропускает элементы, пока лямбда-функция возвращает истину:

a = [None] * 5 + range(5)
a
[None, None, None, None, None, 0, 1, 2, 3, 4]

g = itertools.dropwhile(lambda x: not x, a)
[i for i in g]
[1, 2, 3, 4]

В модуле так же присутсвуют ifilter(), imap(), izip() — такие же функции, как filter, map и zip, но только возвращающие генераторы;

def ncycles(iterable, n):
    "Returns the sequence elements n times"
    return chain.from_iterable(repeat(tuple(iterable), n))
 
def repeatfunc(func, times=None, *args):
    """Repeat calls to func with specified arguments.
    Example:  repeatfunc(random.random)
    """
    if times is None:
        return starmap(func, repeat(args))
    return starmap(func, repeat(args, times))
 
def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return izip(a, b)
</pre>
# Генераторные выражения 
<pre>
Синтаксис такой: 
 (expr1 expr2) 
</pre>
Выражение всегда заключено в круглые скобки. 
В случае, если выражение используется в качестве единственного аргумента при вызове функции, круглые скобки выражения могут совпадать с круглыми скобками вызова функции. 
<pre>
expr2 - итератор, генерирующий значения. 
expr1 - операция, которая производится с сгенрированным expr2 значением. 

Таким образом, генераторное выражение работает следующим образом: 
При очередном вызове expr2, и генерирует следующее исходное значение. 
Сгенерированное исходное значение подставляется в expr1. 
Сгенерированное expr1 значение возвращается генераторным выражением. 
Генераторное выражение ждет следующего вызова 

Простейший пример: 
for i in (x*x for x in [1,5,8]): 
    print i 
Выражение напечатает квадраты чисел 1,5,8 

Еще пример: 

print sum(x*(5+x) for x in xrange(10,20)) 
Выражение напечатает сумму результатов вычисления выражения x*(5+x), при x принимающем целочисленные значения от 10 до 20, 

</pre>
# -*- coding: utf-8 -*-
def foo(): pass

print 'foo.__class__=',foo.__class__ # &lt;type 'function'&gt;

print 'foo.__dict__=',foo.__dict__ # {}

# print (42).__dict__ # Traceback (most recent call last): File "&lt;stdin&gt;", line 1, in &lt;module&gt; AttributeError: 'int' object has no attribute '__dict__'

print '(42).__class__=',(42).__class__ # &lt;type 'int'&gt;

class A(object):
    qux = 'A'
    def __init__(self, name):
        self.name=name
    def foo(self):
        print 'foo'

a = A('a')

# У a тоже есть __dict__ и __class__:

print 'a.__dict__=',a.__dict__   # {'name': 'a'}
print 'a.__class__=',a.__class__  # &lt;class '__main__.A'&gt;
print 'A.__name__=',A.__name__ 
print 'A.__bases__=',A.__bases__ 
print 'type(a):',type(a) # &lt;class '__main__.A'&gt;

print a.__class__ is type(a) # True

# Класс и тип — это одно и то же.

print 'Класс и тип — это одно и то же.',a.__class__ is type(a) is A # True

# Пример. Переопределим класс объекта a:

class B(object):
    qux = 'B'
    def __init__(self):
        self.name = 'B object'
    def bar(self):
         print 'bar'

print a.__dict__ # {'name': 'a'}

a.foo() # foo

print a.__class__ # &lt;class '__main__.A'&gt;

a.__class__ = B

print a.__class__ # &lt;class '__main__.B'&gt;

# Смотрим, что поменялось.

# Значение a.name осталось прежним, т.е. __init__ не вызывался при смене класса.

print a.__dict__ # {'name': 'a'}
# Доступ к классовым переменным и методам «прошлого» класса A пропал:
# a.foo() # Traceback (most recent call last): File "&lt;stdin&gt;", line 1, in &lt;module&gt; AttributeError: 'B' object has no attribute 'foo'
# А вот классовые переменные и методы класса B доступы:
print a.bar() # bar
print a.qux # 'B'

# Работа с атрибутам объекта: установка, удаление и поиск, равносильна вызову встроенных функций settattr, delattr, getattr:

a.x = 1 
print a.x 
setattr(a, 'x', 1)
print a.x 

del a.x 
# print a.x 
# delattr(a, 'x')
# print a.x 

# print a.x 
# getattr(a, 'x')

# При этом стоит стоит понимать, что setattr и delattr влияют и изменяют только сам объект (точнее a.__dict__), и не изменяют класс объекта.

# qux — является классовой переменной, т.е. она «принадлежит» классу B, а не объекту a:

print a.qux #  'B'
print a.__dict__ # {'name': 'a'}

#  если мы попытаемся изменить (установить) атрибут, setattr поместит его в __dict__, специфичный для данного, конкретного объекта.

b = B()
print b.qux # 'B'
a.qux = 'myB'
print a.qux # 'myB'
print a.__dict__ # {'qux': 'myB', 'name': 'a'}
print b.qux # 'B'

# Ну и раз есть 'qux' в __dict__ объекта, его можно удалить с помощью delattr:

del a.qux

# После удаления, a.qux будет возвращать значение классовой переменной:

print a.qux # 'B'
print a.__dict__ # {'name': 'a'}

# Правда __dict__ у классов не совсем словарь

print A.__dict__ # &lt;dictproxy object at 0x1111e88&gt;

# __dict__ ответственен за доступ к внутреннему пространству имен, в котором хранятся методы, дескрипторы, переменные, свойства и прочее:

print dict(A.__dict__) # {'__module__': '__main__', 'qux': 'A', '__dict__': &lt;attribute '__dict__' of 'A' objects&gt;, 'foo': &lt;function foo at 0x7f7797a25c08&gt;, '__weakref__': &lt;attribute '__weakref__' of 'A' objects&gt;, '__doc__': None}
print A.__dict__.keys() # ['__module__', 'qux', '__dict__', 'foo', '__weakref__', '__doc__']&lt;

# Класс является объектом.
class A(object):
    pass


print isinstance(A, object) # True

# Число — это тоже объект.

print isinstance(42, object) # True

# Класс — это класс (т.е. тип).

print isinstance(A, type) # True

# А вот число классом (типом) не является. (Что такое type будет пояснено позже)

print isinstance(42, type) # False

# Ну и a — тоже обычный объект.

a = A()
print isinstance(a, A) # True
print isinstance(a, object) # True
print isinstance(a, type) # False

# И у A всего один прямой родительский класс — object.

print A.__bases__ # (&lt;type 'object'&gt;,)

# Часть специальных параметров можно даже менять:

print A.__name__ # 'A'
A.__name__ = 'B'
print A # &lt;class '__main__.B'&gt;

# С помощью getattr получаем доступ к атрибутам класса:

# print A.qux # 'A'
# print A.foo # &lt;unbound method A.foo&gt;

class A(object):
    qux = 'A'
    def __init__(self, name):
        self.name=name
    def foo(self):
        print 'foo'

a = A
b = A

print b.qux # 'A'
print A.qux # 'A'

# Меняем атрибут qux у класса A. И соответственно должны поменяться значения, которые возвращают экземпляры класса A — a и b:

A.qux='B'
print a.qux # 'B'
print b.qux # 'B'

# Точно так же в рантайме к классу можно добавить метод:

A.quux = lambda self: 'i have quux method'
print A.__dict__['quux'] # &lt;function &lt;lambda&gt; at 0x7f7797a25b90&gt;
print A.quux # &lt;unbound method A.&lt;lambda&gt;&gt;

# И доступ к нему появится у экземпляров:

#print a.quux() # 'i have quux method'

# объявим класс:

class A(object):
    pass

# Для класса A не определены ни __new__, ни __init__. В соответствии с алгоритмом поиска атрибутов для класса (типа), который не стоит путать с алгоритмом поиска атрибутов для обычных объектов, когда класс не найдет их в своем__dict__, он будет искать эти методы в __dict__ своих базовых (родительских) классах.

# Класс А имеет в качестве родителя встроенный класс object. Таким образом он будет их искать в object.__dict__

print object.__dict__['__init__'] # &lt;slot wrapper '__init__' of 'object' objects&gt;
print object.__dict__['__new__'] # &lt;built-in method __new__ of type object at 0x82e780&gt;


# Раз есть такие методы, значит, получается, что a = A() аналогичен последовательности вызовов:

a = object.__new__(A)
object.__init__(a)

# В общем виде, используя super, который как раз и реализует алгоритм поиска атрибутов по родительским классам [1]:

a = super(A, A).__new__(A)
super(A, A).__init__(a)

# Пример.

class A(object):
    def __new__(cls):
        obj = super(A, cls).__new__(cls)
        print 'created object', obj
        return obj
    def __init__(self):
        print 'initing object', self
A()
# created object &lt;__main__.A object at 0x1620ed0&gt;
# initing object &lt;__main__.A object at 0x1620ed0&gt;
# &lt;__main__.A object at 0x1620ed0&gt;

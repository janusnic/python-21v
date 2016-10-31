class Car(object):
    cars = 'A'

    def __init__(self, name):
        self.name = name

    def foo(self):
        print 'foo car'

a = Car('Audi')
# У a тоже есть __dict__ и __class__:
print a.__dict__   # {'name': 'Audi'}
print a.__class__  # <class '__main__.Car'>

print type(a)  # <class '__main__.Car'>
print a.__class__ is type(a)  # True


class Bus(object):
    cars = 'B'

    def __init__(self):
        self.name = 'B object'

    def bar(self):
        print 'bar Bus'

print a.__dict__  # {'name': 'Audi'}
print a.foo()  # foo
print a.__class__  # <class '__main__.Car'>
a.__class__ = B
print a.__class__  # <class '__main__.Bus'>
# Смотрим, что поменялось.
# Значение a.name осталось прежним,
# т.е. __init__ не вызывался при смене класса.
print a.__dict__  # {'name': 'Audi'}
# Доступ к классовым переменным и методам «прошлого» класса A пропал:
# a.foo() # Traceback (most recent call last): File "<stdin>", line 1, in
#  <module> AttributeError: 'B' object has no attribute 'foo'

# А вот классовые переменные и методы класса B доступы:
print a.bar()  # bar
print a.cars  # 'Bus'

# Работа с атрибутам объекта: установка, удаление и поиск, равносильна
# вызову встроенных функций settattr, delattr, getattr:
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

# При этом стоит стоит понимать, что setattr и delattr влияют и изменяют только
#  сам объект (точнее a.__dict__), и не изменяют класс объекта.
# cars — является классовой переменной, т.е. она «принадлежит» классу B,
# а не объекту a:

print a.cars   # 'B'
print a.__dict__  # {'name': 'Audi'}

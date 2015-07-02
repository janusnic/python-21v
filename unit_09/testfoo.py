# -*- coding:utf-8 -*-

class Foo(object):
	"""docstring for Foo 
       Одиночное подчеркивание в начале имени атрибута говорит о том, 
       что переменная или метод не предназначен для использования 
       вне методов класса, однако атрибут доступен по этому имени
	"""
    def _private(self):
       	print("Это приватный метод!")
	arg1 = None 
	_arg2 = None 
	__arg3 = None 
	def __init__(self): 
		super(Foo, self).__init__() 
	def bar(self): 
		pass


# Как получить список всех атрибутов объекта
print dir(Foo)

# Как получить список всех публичных атрибутов объекта

# Сделать это можно или с помощью списковых выражений (list comprehension):

print [arg for arg in dir(Foo) if not arg.startswith('_')]

# или воспользоваться функцией filter:

print filter(lambda x: not x.startswith('_'), dir(Foo))

# Как получить список методов объекта

print [arg for arg in dir(Foo) if callable(getattr(Foo, arg))]
# или
print filter(lambda arg: callable(getattr(Foo, arg)), dir(Foo))

# В какой «магической» переменной хранится содержимое help?

# В атрибуте __doc__. В данную переменную заносится комментарий сразу после объявления класса/метода/функции (см. тестовый класс).

print Foo.__doc__

# Так же можно воспользоваться функцией help в интерактивном режиме:

help(int)

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


a = Foo()
a._private() # Это приватный метод!
# -*- coding:utf-8 -*-
class C(object):
	instance = None
	def __new__(cls):
		if cls.instance is None:
			cls.instance = super(C, cls).__new__(cls)
		return cls.instance

print C() is C() # True
C().x = 1
c = C()
d = C()
print c.x # 1
print d.x # 1
c.x=2
print d.x # 2
print c.x # 2

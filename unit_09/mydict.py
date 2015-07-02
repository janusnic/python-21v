# -*- coding:utf-8 -*-

class Mydict(dict):
    def get(self, key, default = 0):
        return dict.get(self, key, default)

a = dict(a=1, b=2)

b = Mydict(a=1, b=2)

b['c'] = 4
print b # {'a': 1, 'c': 4, 'b': 2}
print a.get('v') # None
print b.get('v') # 0
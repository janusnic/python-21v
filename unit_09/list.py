# -*- coding:utf-8 -*-

# Класс-обертка для списков:
class MyList:
    def __init__(self,start):
        self.wrapped = []
        for i in start:
            self.wrapped.append(i)
    def __add__(self,other):
        lst = []
        for i in other:
            lst.append(i)
        return MyList(self.wrapped + lst)
    def __mul__(self,time):
        return MyList(self.wrapped * time)
    def __getitem__(self,offset):
        return self.wrapped[offset]
    def __len__(self):
        return len(self.wrapped)
    def __getslice__(self,low,high):
        return MyList(self.wrapped[low:high])
    def append(self,node):
        self.wrapped.append(node)
    def __getattr__(self,name):
        return getattr(self.wrapped,name)
    def __repr__(self):
        return repr(self.wrapped)

if __name__ == '__main__':
    x = MyList('abcdef')
    print x
    print x[2]
    print x[1:]
    x.append('B')
    print x + 'ghi'
    print x * 3
    x.sort()
    print x

# from mylist import MyList

class MyListSub(MyList):
    calls = 0 # счетчик класса
    def __init__(self,start):
        self.adds = 0 # счетчик экземпляра
        MyList.__init__(self,start)
    def __add__(self,other):
        MyListSub.calls += 1
        self.adds += 1
        return MyList.__add__(self,other)
    def stats(self):
        return self.calls, self.adds

if __name__ == '__main__':
    x = MyListSub('abcdef')
    y = MyListSub('zyxwvut')
    print x[2]
    print x[1:]
    print x + 'ghi'
    print x + 'lkj'
    print y + 'iop'
    print x.stats(), y.stats()

class Meta:
    def __getattr__(self,name):
        print 'get', name
    def __setattr__(self,name,value):
        print 'set',name, value

x = Meta()
x.app
x.color = 'blue'
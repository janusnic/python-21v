# -*- coding:utf-8 -*-

class Counter(object):
    def __init__(self, low, high):
        self.current = low
        self.high = high

    def __iter__(self):
        'Returns itself as an iterator object'
        return self

    # def __next__(self):
    def next(self):
        'Returns the next value till current is lower than high'
        if self.current > self.high:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1

# Now we can use this iterator in our code.

c = Counter(5,10)

for i in c:
  # print(i, end=' ')
  print i, 

# Remember that an iterator object can be used only once. 
# It means after it raises StopIteration once, it will keep raising the same exception.

c = Counter(5,6)
next(c) # 5
next(c) # 6
next(c) # Traceback (most recent call last): File "<stdin>", line 1, in <module> File "<stdin>", line 11, in next StopIteration

next(c) # Traceback (most recent call last): File "<stdin>", line 1, in <module> File "<stdin>", line 11, in next StopIteration

# Using the iterator in for loop example we saw, the following example tries to show the code behind the scenes.

iterator = iter(c)
while True:
    try:
        x = iterator.__next__()
        print(x, end=' ')
    except StopIteration as e:
        break

# 5 6 7 8 9 10
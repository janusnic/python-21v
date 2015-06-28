# -*- coding:utf-8 -*-
# itertools

import itertools

c = itertools.count()
print [r for (r, i) in zip(c, xrange(20))] # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

c = itertools.cycle("spam")
print [r for (r, i) in zip(c, xrange(10))] # ['p', 'a', 'm', 's', 'p', 'a', 'm', 's', 'p', 'a']

c = itertools.repeat(None)
print [r for (r, i) in zip(c, xrange(10))] # [None, None, None, None, None, None, None, None, None, None]


g = itertools.takewhile(lambda n: n<10, itertools.count())
print [i for i in g] # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


c = itertools.count()
c = itertools.islice(c, 10)
print [i for i in c] # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]



a = [None] * 5 + range(5)
print a # [None, None, None, None, None, 0, 1, 2, 3, 4]

g = itertools.dropwhile(lambda x: not x, a)
print [i for i in g] #[1, 2, 3, 4]


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

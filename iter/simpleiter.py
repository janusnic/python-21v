from __future__ import print_function
from six import Iterator


class SimpleIterator(Iterator):

    def __init__(self, fname):
        self.fd = open(fname, 'r')

    def __iter__(self):
        return self

    def __next__(self):
        line = self.fd.readline()
        if line != '':
            line = line.rstrip('\n')
            return line.title()
        raise StopIteration

simple_iter = SimpleIterator('loren.txt')
for i in simple_iter:
    print(i)

print([x for x in enumerate(simple_iter)])

simple_iter1 = SimpleIterator('loren.txt')
print([x for x in enumerate(simple_iter1)])

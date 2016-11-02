from __future__ import print_function
from six import Iterator


class MyIterator(Iterator):
    def __init__(self, step=5):
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        self.step -= 1
        if not self.step:
            raise StopIteration()
        return self.step

myiterator = MyIterator()
for item in myiterator:
    print(item)
    print()

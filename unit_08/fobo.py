# -*- coding:utf-8 -*-
class Fibonacci: 
    """Итератор последовательности Фибоначчи до N""" 
    
    def __init__(self, N): 
        self.n, self.a, self.b, self.max = 0, 0, 1, N 
    
    def __iter__(self): 
    # сами себе итератор: в классе есть метод next() 
       return self 
    
    def next(self): 
       if self.n < self.max: 
           a, self.n, self.a, self.b = self.a, self.n+1, self.b, self.a+self.b 
           return a 
       else: 
           raise StopIteration 

# Использование: 
for i in Fibonacci(100): 
    print i, 

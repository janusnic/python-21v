class SimpleIterator(object): 
     def __init__(self,fname): 
         self.fd = open(fname,'r') 
         
     def __iter__(self): 
         return self 
 
     def next(self): 
         l = self.fd.readline() 
         if l != '': 
             l = l.rstrip('\n') 
             num = int(l) 
             return num*2 
         raise StopIteration 

simple_iter = SimpleIterator('test_data.txt') 
for i in simple_iter: 
    print i 

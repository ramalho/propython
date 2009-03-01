# coding: utf-8

def fibonacci(a=1, b=1): 
    while 1: 
        yield a 
        a, b = b, a+b

t = fibonacci()
for i in range(100): 
    print t.next()
   

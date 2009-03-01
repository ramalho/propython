#!/usr/bin/env python
# -*- coding: utf-8 -*-

def fatorial(n):
    """Devolve n! (n fatorial)
    
    >>> fatorial(1)
    1
    >>> fatorial(5)
    120
    >>> fatorial(30)
    265252859812191058636308480000000L
    """
    if n <= 1: return 1
    return n * fatorial(n-1)
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()
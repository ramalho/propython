#!/usr/bin/env python
# coding: utf-8

'''Exemplo de acesso e atribuição dinâmica de atributos de instância.

    >>> n = Nova()
    * self.__setattr__('b')
    >>> print repr(n.a)
    1
    >>> print repr(n.b)
    2
    >>> print repr(n.c)
    * self.__getattr__('c')
    'c?'
    >>> n.a = 10
    * self.__setattr__('a')
    >>> print repr(n.a)
    10
    >>> n.x = 99
    * self.__setattr__('x')
    >>> print repr(n.x)
    99

'''

class Nova(object):
    a = 1

    def __init__(self):
        self.b = 2

    def __getattr__(self, nome):
        print '* self.__getattr__(%r)' % nome
        return nome + '?'

    def __setattr__(self, nome, valor):
        print '* self.__setattr__(%r)' % nome
        self.__dict__[nome] = valor
    
if __name__=='__main__':
    import doctest
    doctest.testmod()

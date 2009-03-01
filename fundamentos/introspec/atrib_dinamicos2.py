#!/usr/bin/env python
# coding: utf-8

'''Demonstração de controle de acesso a um atributos de instância.

Este exemplo compara o funcionamento dos métodos especiais `__getattr__`
e `__getattribute__`. Lembre-se que o `__getattribute__` só funciona em 
classes novas (derivadas de object).

    >>> o = Klass()
    
Os atributos `a` e `b` existem e não recebem tratamento especial. 
Note que o método `__getatttribute__` é sempre invocado::
    
    >>> print o.a
    * self.__getattribute__('a')
    1
    >>> print o.b
    * self.__getattribute__('b')
    2
    
O atributo `c` não existe, então o método `__getattr__` é invocado::
    
    >>> print o.c
    * self.__getattribute__('c')
    * self.__getattr__('c')
    c?
    
O atributo `x` existe, mas no método `__getattribute__` levanta a mesma 
exceção que a implementação herdada da classe `object`, então o método 
`__getattr__` acaba sendo invocado pelo Python, e o resultado é idêntico 
ao atributo que não existe (apenas mais lento, porque estamos fazendo
em Python algo que está implementado em C no CPython)::
    
    >>> print o.x
    * self.__getattribute__('x')
    * self.__getattribute__('__class__')
    * self.__getattr__('x')
    x?
    
Aqui o método `__getattribute__` levanta uma exceção diferente, e o 
mecanismo normal de acesso a atributos do Python é abortado.
    
    >>> print o.y
    Traceback (most recent call last):
       ...
    Exception: Please don't mention attribute 'y'
    
Por que no exemplo acima não apareceu a saída do `print` que ocorre na 
primeira linha do método `__getattribute__`? 

Boa pergunta! Se você souber, me conte!

'''

class Klass(object):
    a = 1

    def __init__(self):
        self.b = 2
        self.x = 7
        self.y = 9

    def __getattribute__(self, name):
        print '* self.__getattribute__(%r)' % name
        if name == 'x':
            msg = "%s instance has no attribute '%s'"
            raise AttributeError(msg % (self.__class__.__name__, name))
        if name == 'y':
            raise Exception("Please don't mention attribute '%s'" % name)
        else: # let the superclasses handle this
            return super(Klass, self).__getattribute__(name)

    def __getattr__(self, name):
        print '* self.__getattr__(%r)' % name
        return name + '?'
    
if __name__=='__main__':
    import doctest
    doctest.testmod()


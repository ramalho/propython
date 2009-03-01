#!/usr/bin/env python
# coding: utf-8

'''
O equivalente do "method_missing" do Ruby pode ser implementado em Python
usando o método __getattr__ que é invocado quando um atributo que não existe
é acessado. Eis uma implementação bem elementar::

    >>> b = Bicho()
    >>> print b.piar()
    piu!
    >>> print b.piar(3)
    piu! piu! piu!
    >>> print b.urrar() # este método não existe
    urru!
    >>> print b.urrar(2)
    urru! urru!
    
'''

class Bicho(object):
    
    def piar(self, vezes=1):
        return ('piu! ' * vezes).strip()

    def fazer_barulho(self, som, vezes):
        barulho = (som+'!').replace('ar!', 'u!')
        return ((barulho+' ') * vezes).strip()
        
    def __getattr__(self, nome):
        def sonar(vezes=1):
            return self.fazer_barulho(nome, vezes)
        return sonar
    
if __name__=='__main__':
    import doctest
    doctest.testmod()

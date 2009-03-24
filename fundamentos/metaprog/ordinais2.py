#!/usr/bin/env python
# coding: utf-8

# Implementação usando properties pré-definidas

'''
Os itens contidos em objetos da classe TuplaOrdinal podem ser acessados pelos
ordinais de 'primeiro' até 'decimo'::

    >>> t = TuplaOrdinal((11, 22, 33, 44, 55))
    >>> t.primeiro
    11
    >>> t.terceiro
    33

O último também pode ser acessado como um atributo, mas a implementação
neste caso é bem diferente:

    >>> t.ultimo
    55

Se não existe o item correspondente::

    >>> t.decimo    
    Traceback (most recent call last):
      ...
    IndexError: tuple index out of range

Porém::

    >>> t.vigesimo    
    Traceback (most recent call last):
      ...
    AttributeError: 'TuplaOrdinal' object has no attribute 'vigesimo'

'''

from operator import itemgetter

class TuplaOrdinal(tuple):
    
    __ordinais = ('primeiro segundo terceiro quarto quinto sexto setimo'
                  ' oitavo nono decimo').split()
        
    def __init__(self, *args, **kwargs):
        super(TuplaOrdinal,self).__init__(*args, **kwargs)
        for i, ordinal in enumerate(self.__ordinais):
            setattr(self.__class__, ordinal, property(itemgetter(i)))
    
    @property        
    def ultimo(self):
        return self[-1]
        
    ult = ultimo    
    
        
if __name__=='__main__':
    import doctest
    doctest.testmod()    
    
    


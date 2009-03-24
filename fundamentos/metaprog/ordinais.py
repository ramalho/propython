#!/usr/bin/env python
# coding: utf-8

'''
Os itens contidos em objetos da classe Lista podem ser acessados pelos
ordinais de 'primeiro' até 'decimo', ou por abreviaturas de três letras
destes ordinais:

    >>> l = Lista([11, 22, 33, 44, 55])
    >>> l.primeiro
    11
    >>> l.ter
    33

Se não existe a posição correspondente::

    >>> l.oitavo
    Traceback (most recent call last):
        ...
    AttributeError: Este objeto 'Lista' nao tem 'oitavo' item.
    
O último também pode ser acessado como um atributo, mas a implementação
neste caso é bem diferente:

    >>> l.ult
    55

Quando não sabemos o que fazer com o atributo acessado, é melhor levantar
a tradicional exceção AttributeError:

    >>> l.spam
    Traceback (most recent call last):
        ...
    AttributeError: 'Lista' object has no attribute 'spam'

Isso vale também para atributos que começam com três letras de uma sigla
mas não coincidem a partir da quarta letra::

    >>> l.primata
    Traceback (most recent call last):
        ...
    AttributeError: 'Lista' object has no attribute 'primata'
    

'''

from itertools import count

class Lista(list):
    
    __ordinais = ('primeiro segundo terceiro quarto quinto sexto setimo'
                  ' oitavo nono decimo').split()
    __abrevs = [s[:3] for s in __ordinais]
    
    def __getattr__(self, atrib):
        for i, ordinal, abrev in zip(count(), self.__ordinais, self.__abrevs):
            if atrib == ordinal or (len(atrib)>=3 and ordinal.startswith(atrib)):
                if i < len(self):
                    return self[i]
                else:
                    msg = "Este objeto '%s' nao tem '%s' item."
                    raise AttributeError(msg % (self.__class__.__name__, atrib))

        msg = "'%s' object has no attribute '%s'"
        raise AttributeError(msg % (self.__class__.__name__, atrib))
    
    @property        
    def ultimo(self):
        return self[-1]
        
    ult = ultimo    


if __name__=='__main__':
    import doctest
    doctest.testmod()    


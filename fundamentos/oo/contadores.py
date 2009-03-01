#!/usr/bin/env python
# coding: utf-8

class Contador(object):
    '''
    Uma instância de contador serve para contar itens.
    
    >>> c = Contador()
    >>> [c.incluir(letra) for letra in 'casa']
    [1, 1, 1, 2]
    >>> c.contar('a'), c.contar('c')
    (2, 1)
    
    Se o item nunca foi incluído, o contador reclama:
    
    >>> c.contar('x')
    Traceback (most recent call last):
        todas as linhas que estiverem endentadas aqui são ignoradas
    KeyError: 'x'
    '''
    def __init__(self):
        self.dic = {}
            
    def incluir(self, item):
        qtd = self.dic.get(item, 0) + 1
        self.dic[item] = qtd
        return qtd
        
    def contar(self, item):
        return self.dic[item]
        
class ContadorTolerante(Contador):
    '''
    Contador que devolve zero sem reclamar 
    quando um item não consta.
    
    >>> c = ContadorTolerante()
    >>> [c.incluir(letra) for letra in 'banana']
    [...]
    >>> c.contar('a'), c.contar('x')
    (3, 0)
    '''

    def contar(self, item):
        return self.dic.get(item, 0)
    
class ContadorTotalizador(Contador):
    '''
    Contador intolerante que armazena o total de itens contados

    >>> c = ContadorTotalizador()
    >>> [c.incluir(letra) for letra in 'banana']
    [...]
    >>> c.contar('a'), c.total
    (3, 6)

    >>> c.contar('x')
    Traceback (most recent call last):
    KeyError: 'x'
    '''

    def __init__(self):
        super(ContadorTotalizador, self).__init__()
        self.total = 0

    def incluir(self, item):
        super(ContadorTotalizador, self).incluir(item)
        self.total += 1
                
class ContadorTotalizadorTolerante(ContadorTotalizador, ContadorTolerante):
    '''
    Contador tolerante que armazena o total de itens contados

    >>> c = ContadorTotalizadorTolerante()
    >>> [c.incluir(letra) for letra in 'uva']
    [...]
    >>> c.contar('a'), c.total
    (1, 3)

    >>> c.contar('x')
    0
    '''
    pass # esta linha é redundante qdo. temos uma docstring

def _testar(): 
    import doctest
    flags = doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS
    falhas, testes = doctest.testmod(optionflags=flags)
    if falhas == 0:
        print 'OK: %s testes' % testes

if __name__ == "__main__": 
    _testar() 

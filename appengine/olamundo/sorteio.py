# coding: utf-8

from random import shuffle

def parear(nomes, embaralhar=True):
    u'''Dada uma lista de nomes, garar uma lista de pares ordenados
        de nomes, onde:
        - cada nome aparece uma vez e apenas uma vez em cada posição
        - se existe um par a, b, não existirá o par b, a
        
    Exemplos:
    
    >>> parear(['a', 'b'], embaralhar=False)
    [('a', 'b'), ('b', 'a')]
    >>> parear(['a', 'b', 'c'], embaralhar=False)
    [('a', 'b'), ('b', 'c'), ('c', 'a')]
    '''
    if embaralhar:
        nomes = nomes.shuffle()
    primeiro = nomes[0]
    pares = []
    try:
        while True:
            pares.append(nomes.pop(0), nomes[0])
    except IndexError:
        print nomes
        print pares
        
if __name__=='__main__':
    from doctest import testmod
    testmod()
    
    
    
    


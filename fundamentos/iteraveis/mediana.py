#!/usr/bin/env python
# coding: utf-8

def mediana(lista):
    '''
    mediana: valor do item central da lista ordenada, ou 
    média dos dois itens centrais
    
        >>> mediana([1,2,3,4,5])
        3
        >>> mediana([1,2,3,4])
        2.5
        >>> mediana([3,2,1,4])
        2.5
        
    '''
    centro = len(lista)/2
    ordem = sorted(lista)
    if len(ordem) % 2:
        return ordem[centro]
    else:
        return float(ordem[centro-1]+ordem[centro])/2

if __name__=='__main__':
    import doctest
    doctest.testmod()
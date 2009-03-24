#!/usr/bin/env python
# coding: utf-8

'''
Instâncias de Romano têm atributos dinâmicos que devolvem o valor
inteiro correspondente ao numeral romano acessado::
    
    >>> r = Romano()
    >>> r.III
    3
    >>> r.mmix # caixa-baixa também funciona
    2009

'''
# Inspirado pela documentação do método Object#method_missing linguagem Ruby
# e aproveitando o código de Mark Pilgrim publicado no livro
# Dive into Python: http://diveintopython.org/

from roman import fromRoman, InvalidRomanNumeralError

class Romano(object):
    def __getattr__(self, s):
        try:
            return fromRoman(s.upper())
        except InvalidRomanNumeralError:
            raise AttributeError('Numeral romano invalido: %r' % s)

if __name__=='__main__':
    import doctest
    doctest.testmod()
    

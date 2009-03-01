#!/usr/bin/env python
# coding: utf-8

"""
Acesso por palavras::
    
    >>> txt = Texto(u'Poema que aconteceu')
    >>> for palavra in txt.palavras(): print palavra
    Poema
    que
    aconteceu

"""

class Texto(object):
    def __init__(self, ustr):
        self.ustr = ustr

    def palavras(self):
        for parte in self.ustr.split():
            yield parte
        raise StopIteration


def testar():
    import doctest
    doctest.testmod()

if __name__=='__main__':
    testar()
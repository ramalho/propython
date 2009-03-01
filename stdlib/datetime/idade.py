#!/usr/bin/env python
# coding: utf-8

"""
Cálculos de idade::

    >>> quando = date(2009,2,28)
    >>> idade(date(2008,2,28))
    1
    >>> idade(date(2008,2,29))
    0
    >>> idade(date(2000,1,1))
    9
    
Definimos algumas faixas etárias::

    >>> f0 = FaixaEtaria(0, 1)
    >>> print f0
    de 0 a 1 ano
    >>> f2 = FaixaEtaria(2, 6)
    >>> print f2
    de 2 a 6 anos
    >>> f7 = FaixaEtaria(7, 7) # de 7 anos a 8 anos menos um dia
    >>> print f7
    7 anos
    >>> f8 = FaixaEtaria(8)
    >>> print f8
    a partir de 8 anos
    
Faixas etárias não podem ser sobrepostas::
    
    >>> fx = FaixaEtaria(1, 3)
    Traceback (most recent call last):
        ...
    FaixaSobreposta: idade minima 1 esta na faixa "de 0 a 1 ano" definida antes
    >>> fx = FaixaEtaria(4, 5)
    Traceback (most recent call last):
        ...
    FaixaSobreposta: idade minima 4 esta na faixa "de 2 a 6 anos" definida antes
    >>> fx = FaixaEtaria(7)
    Traceback (most recent call last):
        ...
    FaixaSobreposta: idade minima 7 esta na faixa "7 anos" definida antes
    >>> fx = FaixaEtaria(8)
    Traceback (most recent call last):
        ...
    FaixaSobreposta: idade minima 8 esta na faixa "a partir de 8 anos" definida antes
    
Dada uma data de corte, verificar em que faixa se encaixam algumas 
datas de nascimento::

    >>> quando = date(2009,2,28)
    >>> nasc = date(2009,1,1)
    >>> print FaixaEtaria.get_faixa_por_nascimento(nasc, quando)
    de 0 a 1 ano
    >>> nasc = date(1900,1,1)
    >>> print FaixaEtaria.get_faixa_por_nascimento(nasc, quando)
    a partir de 8 anos
    >>> nasc = date(2002,2,28)
    >>> print FaixaEtaria.get_faixa_por_nascimento(nasc, quando)
    7 anos
    >>> nasc = date(2002,3,1)
    >>> print FaixaEtaria.get_faixa_por_nascimento(nasc, quando)
    de 2 a 6 anos
    >>> nasc = date(2001,3,1)
    >>> print FaixaEtaria.get_faixa_por_nascimento(nasc, quando)
    7 anos
    >>> nasc = date(2001,2,28)
    >>> print FaixaEtaria.get_faixa_por_nascimento(nasc, quando)
    a partir de 8 anos

Removendo a faixa "de 2 de 6 anos", podemos testar idades que não se encaixam::

    >>> print f2
    de 2 a 6 anos
    >>> FaixaEtaria.remover(f2)
    >>> quando = date(2009,2,28)
    >>> nasc = date(2002,3,1)
    >>> print FaixaEtaria.get_faixa_por_nascimento(nasc, quando)
    None
    
Agora que temos um buraco nas faixas, podemos testar se a sobreposição da 
idade_maxima está sendo corretamente verificada::

    >>> fx = FaixaEtaria(4, 7)
    Traceback (most recent call last):
        ...
    FaixaSobreposta: idade maxima 7 esta na faixa "7 anos" definida antes
    >>> fx = FaixaEtaria(4, 9)
    Traceback (most recent call last):
        ...
    FaixaSobreposta: idade maxima 9 esta na faixa "a partir de 8 anos" definida antes


"""

IDADE_LIMITE = int(2**32-1)

from datetime import date

def idade(nascimento, quando=None):
    if quando is None:
        quando = date.today()
    ja_fez = (nascimento.month, nascimento.day) <= (quando.month, quando.day) 
    if ja_fez:
        return quando.year - nascimento.year
    else:
        return quando.year - nascimento.year - 1
        
class FaixaInvalida(ValueError):
    pass        

class FaixaSobreposta(ValueError):
    pass        
        
class FaixaEtaria(object):
    # XXX: se este dicionario usasse weakrefs, o método FaixaEtaria.remover 
    # poderia ser FaixaEtaria.__del__? investigar!
    __faixas = {}

    def __init__(self, idade_min=0, idade_max=None):
        FaixaEtaria.verificar_consistencia(idade_min, idade_max)
        self.idade_min = idade_min
        self.idade_max = idade_max
        FaixaEtaria.__faixas[(idade_min, idade_max)] = self

    def __unicode__(self):
        if self.idade_max:
            plural = (u'', u's')[self.idade_max!=1]
            if self.idade_min == self.idade_max:
                fmt = u'%s ano' + plural                
                return fmt % (self.idade_max)
            else:
                fmt = u'de %s a %s ano' + plural
                return fmt % (self.idade_min, self.idade_max)
        else:
            plural = (u'', u's')[self.idade_min!=1]
            fmt = u'a partir de %s ano' + plural
            return fmt % self.idade_min
            
    def __str__(self):
        return self.__unicode__().encode('utf-8')

    @classmethod
    def get_faixa(cls, idade_min, idade_max):
        return cls.__faixas.get((idade_min, idade_max))

    @classmethod
    def get_faixas(cls):
        return cls.__faixas

    @classmethod
    def get_faixa_por_idade(cls, idade):
        for imin, imax in sorted(cls.get_faixas()):
            limite_max = imax or IDADE_LIMITE
            if imin <= idade <= limite_max:
                return cls.get_faixa(imin, imax)

    @classmethod
    def verificar_consistencia(cls, idade_min, idade_max):
        if idade_min < 0:
            raise FaixaInvalida('idade minima deve ser >= 0')
        elif idade_max is not None:
            if idade_max < idade_min:
                raise FaixaInvalida('idade maxima deve ser >= idade minima')
            elif idade_max > IDADE_LIMITE:
                raise FaixaInvalida('idade maxima deve ser <= %s' % IDADE_LIMITE)

        faixa = cls.get_faixa_por_idade(idade_min)
        if faixa is not None:
            msg = 'idade minima %s esta na faixa "%s" definida antes'
            raise FaixaSobreposta(msg % (idade_min, faixa))
        faixa = cls.get_faixa_por_idade(idade_max)
        if faixa is not None:
            msg = 'idade maxima %s esta na faixa "%s" definida antes'
            raise FaixaSobreposta(msg % (idade_max, faixa))

    @classmethod
    def get_faixa_por_nascimento(cls, nascimento, quando=None):
        return cls.get_faixa_por_idade(idade(nascimento, quando))
    
    @classmethod    
    def remover(cls, faixa):
        del cls.__faixas[(faixa.idade_min, faixa.idade_max)]
                
        
if __name__=='__main__':
    from doctest import testmod
    testmod()        


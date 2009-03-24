#!/usr/bin/env python
# coding: utf-8

from datetime import date

class Ano(int):
    
    nomes_meses = ('janeiro fevereiro marco abril maio junho julho agosto'
                   ' setembro outubro novembro dezembro').split()

    def __init__(self, gregoriano):
        super(Ano, self).__init__(gregoriano)
        self.gregoriano = gregoriano

    def __getattr__(self, atrib):
        try:
            pos = self.nomes_meses.index(atrib)
        except ValueError:
            msg = "'%s' object has no attribute '%s'"
            raise AttributeError(msg % (self.__class__.__name__, atrib))
        else:
            return Mes(self.gregoriano, pos+1)

    def __getitem__(self, i):
        return Mes(self.gregoriano, i)
        
    def __len__(self):
        return len(self.meses)
        
    def __repr__(self):
        return 'Ano(%r)' % self.gregoriano

class Mes(object):
    def __init__(self, ano, mes):
        self.ano = ano
        try:
            self.mes = int(mes)
        except ValueError:
            self.ano.meses.index(mes)
    def __str__(self):
        return "%s de %s" % (self.mes, self.ano)
    def iso(self):
        return '%s-%s'
    def __repr__(self):
        return 'Mes(%r, %r)' % (self.ano, self.mes)
        
a = Ano(2009)
print repr(a)
print a.janeiro
for mes in a: print mes
        



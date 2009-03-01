#!/usr/bin/env python
#-*- coding:utf-8 -*-

# As classes estão no mesmo arquivo para facilitar 
# o exemplo. Numa situação real elas poderiam estar em arquivos 
# separados e seriam importadas com a seguinte instrução
# from arquivo import classe

class Contador(object):
    def __init__(self):
        self.dic = {}

    def incluir(self, item):
        qtd = self.dic.get(item, 0) + 1
        self.dic[item] = qtd

    def contar(self, item):
        return self.dic[item]

class ContadorTolerante(Contador):
    # esse método sobrescreve o método com o mesmo nome na superclasse
    def contar(self, item):
        return self.dic.get(item, 0)

class ContadorTotalizador(Contador):
    ## esse método inicializador amplia o inicalizador da superclasse
    def __init__(self):
        super(ContadorTotalizador, self).__init__()
        self.__total = 0

    # esse método amplia o método da superclasse
    def incluir(self, item):
        super(ContadorTotalizador, self).incluir(item)
        self.__total += 1
        return self.dic[item]

    @property
    def total(self):
        return self.__total

class ContadorTT(ContadorTotalizador,ContadorTolerante):
    pass


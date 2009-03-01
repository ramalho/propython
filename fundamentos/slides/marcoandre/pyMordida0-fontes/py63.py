#!/usr/bin/env python
#-*- coding:utf-8 -*-

class Contador(object):
    def __init__(self):
        self.dic = {}

    def incluir(self, item):
        qtd = self.dic.get(item, 0) + 1
        self.dic[item] = qtd
        return qtd

    def contar(self, item):
        return self.dic[item]

#!/usr/bin/env python
#-*- coding:utf-8 -*-

naipes = 'copas ouros espadas paus'.split()
cartas = 'A 2 3 4 5 6 7 8 9 10 J Q K'.split()
baralho = [(c, n) for n in naipes for c in cartas]
print baralho
print len(baralho)

#!/usr/bin/env python
#-*- coding:utf-8 -*-

#uma lista de duplas
posicoes = [(1,2),(2,2),(5,2),(0,3)]

#um jeito de percorrer
for pos in posicoes:
    i, j = pos
    print i, j

print

#outro jeito de percorrer
for i, j in posicoes:
    print i, j

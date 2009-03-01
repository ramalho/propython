#!/usr/bin/env python
#-*- coding:utf-8 -*-

qtds = [2,6,12,24]
frutas = ['abacaxis', 'bananas', 'caquis']
produto = [(q,f) for q in qtds for f in frutas]
print produto

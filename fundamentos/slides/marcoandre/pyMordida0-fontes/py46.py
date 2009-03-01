#!/usr/bin/env python
#-*- coding:utf-8 -*-

lista = [n for n in range(30) if n % 7 == 0]

for item in lista:
    print item

for i,item in enumerate(lista):
    print i,item

for i in range(30): 
    if i % 7 == 0: print i

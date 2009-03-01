#!/usr/bin/env python
#-*- coding:utf-8 -*-

def inverter(texto):
    if len(texto) <= 1:
        return texto
    lista = list(texto)
    lista.reverse()
    return ''.join(lista)

print inverter('python')

#!/usr/bin/env python
# encoding: utf-8
"""
proclib.py

Analise dos dominios em processo de liberação

"""

import sys

menor_dom = sys.maxint
menores = []
tam_3 = []

texto = file('proclib-l.txt').read()
lista = texto.split()
print len(lista), 'dominios'
for dom in lista:
	partes = dom.split('.')
	if len(partes) > 3: continue
	if partes[1] != 'com': continue
	tam_dom = len(partes[0])
	if tam_dom == menor_dom:
		menores.append(dom)
	elif tam_dom < menor_dom:
		menor_dom = tam_dom
		menores = [dom]
	if tam_dom == 3:
		tam_3.append(partes[0])
			
print 'menor_dom =', menor_dom
for dom in menores:
	print dom
	
for dom in tam_3:
	print dom, 


	
	
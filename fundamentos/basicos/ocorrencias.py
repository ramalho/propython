#!/usr/bin/env python
# coding: utf-8

"""
Este programa conta as ocorrências das letras de A a Z em um arquivo
texto em formato UTF-8, e exibe uma lista com as letras em ordem 
decrescente de quantidade. 

As letras acentuadas e letras minúsculas são convertidas para seus
equivalentes maiúsculos e sem acentos. O cedilha é contado como C.

Para usar, passe o nome do arquivo texto como argumento na linha de
comando.
"""

import sys
from unicodedata import decomposition
from string import ascii_uppercase

ocorrencias = {}

for linha in file(sys.argv[1]):
    for car_uni in linha.decode('utf-8'): # converter linha para unicode
        if not car_uni.strip():
            continue # ignorar brancos
        try: # primeiro tentamos converter para ASCII
            car = car_uni.encode('ascii')
        except UnicodeEncodeError: # se não dá certo, apelamos
            partes = decomposition(car_uni)
            if partes: # se o caractere pode ser decomposto...
                ascii = partes.split()[0] # a primeira parte é o código ASCII...
                car = chr(int(ascii, 16)) # converter o ASCII hexadecimal
            else: # se o caractere não pode ser decomposto...
                continue # então não tem correspondente na tabela ASCII

        car = car.upper() # converter para maiúsculas
        if car in ascii_uppercase:
            # finalmente, podemos computar a ocorrência
            if car in ocorrencias:
                ocorrencias[car] += 1
            else:
                ocorrencias[car] = 1
                  
indice = [(qtd, car) for (car, qtd) in ocorrencias.items()]
indice = sorted(indice)

print 'letra ocorrencias'
print '----- -----------'
for qtd, car in reversed(indice):
    print '%5s %11d' % (car, qtd)


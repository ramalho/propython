#!/usr/bin/env python2.5

from elementtree.ElementTree import parse
from pprint import pprint

NOME_ARQ = 'LR-GBS-MyLibrary.xml'

tree = parse(NOME_ARQ)
elem = tree.getroot()

catalogo = []
for livro in elem.getiterator('book'):
    reg = {}
    for campo in list(livro):
        if campo.tag == 'identifier':
            tag, valor = [e.text for e in campo]
        else:
            tag = campo.tag
            valor = campo.text
        reg[tag] = valor
    catalogo.append(reg)
    
pprint(catalogo)
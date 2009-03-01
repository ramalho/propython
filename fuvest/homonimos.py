#!/usr/bin/env python
# coding: utf-8

'''
Fuvest 2008: Homônimos convocados
- convocados.txt: lista convocados para a 2a-fase do vestibular
'''
import sys, re

if len(sys.argv) < 2:
    print 'Modo de usar: %s lista1.txt [lista2.txt ...]' % sys.argv[0]
    sys.exit()

padrao_nome = re.compile(r"[^A-Z]*([A-Z][A-Z '-]+[A-Z])[^A-Z ]*",re.I)

for nome_arq in sys.argv[1:]:
    nomes = set()
    qtd = 0
    lin_ant = None
    primeira_dupla = False
    homonimos = 0
    print '*' * 60, nome_arq
    for lin in file(nome_arq):
        lin = lin.strip()
        if not lin or lin.startswith(lin[0]*12):
            continue # remover linhas vazias e separadores alfabeticos
        nome = padrao_nome.match(lin)
        if not nome:
            continue # linha aparentemente sem nome, vamos ignorar
        nome = nome.group(1)
        # if '-' in nome or "'" in nome: print nome
        if nome in nomes:
            if primeira_dupla:
                primeira_dupla = False
            else:
                primeira_dupla = True
                homonimos += 1
                # print lin_ant
            homonimos += 1
            # print lin
        else:
            primeira_dupla = False
        lin_ant = lin
        nomes.add(nome)
        qtd += 1

    nomes_unicos = len(nomes)
    print '%6d nomes' % qtd
    print '%6d nomes unicos' % nomes_unicos
    print '%6d homonimos' % homonimos

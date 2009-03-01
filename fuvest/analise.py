#!/usr/bin/env python
# coding: utf-8

'''
Fuvest 2008: Análise das listas de isentos e convocados
- isentos.txt: lista de isentos da taxa de inscrição
- convocados.txt: lista convocados para a 2a-fase do vestibular

Obs. Não está sendo feito nenhum tratamento para casos de homônimos.
'''
import sys
import re

# ref: http://www.fuvest.br/vest2008/informes/ii092008.stm etc.
INSCRITOS = {
#   2008: 140999,
    2007: 142656,
    2006: 170474,
    2005: 154514,
    2004: 157808,
    2003: 161147,
    2002: 146307
}

padrao_nome = re.compile(r"[^A-Z]*([A-Z][A-Z '-]+[A-Z])[^A-Z ]*")

def ler_nomes(prefixo, ano):
    nomes = set()
    for nlin, lin in enumerate(file('listas/%s%s.txt' % (prefixo, ano))):
        lin = lin.strip().upper()
        if not lin or lin.startswith(lin[0]*12):
            continue # remover linhas vazias e separadores alfabeticos
        nome = padrao_nome.match(lin)
        if not nome:
            continue # linha aparentemente sem nome, vamos ignorar
        nome = nome.group(1)
        if prefixo == 'isen' and ano == 2002: # retirar sigla da UF
            nome = nome[2:].strip()
        assert nome, repr(nome)
        nomes.add(nome)
    #print list(nomes)[:20]    
    return nomes

anos = sorted(INSCRITOS)
try: 
    ano = int(sys.argv[1])
except (IndexError, ValueError):
    ano = None
if ano is None or ano not in anos:
    msg = 'Modo de usar: %s <ano> (de %s a %s)'
    print msg % (sys.argv[0], anos[0], anos[-1])
    sys.exit()

inscritos = INSCRITOS[ano]

print '%6d inscritos no vestibular Fuvest %s' % (inscritos, ano) 
print

isentos = ler_nomes('isen', ano)
print '%6d isentos de taxa de incrição' % len(isentos) 
print '%5.1f%% do total' % (float(len(isentos))/inscritos*100)
print

convocados = ler_nomes('conv', ano)    
print '%6d convocados para a 2a fase' % len(convocados) 
print '%5.1f%% do total' % (float(len(convocados))/inscritos*100)
print

aprovados = ler_nomes('apro', ano)    
print '%6d aprovados na 1a chamada' % len(aprovados) 
print '%5.1f%% do total' % (float(len(aprovados))/inscritos*100)
print

isen_conv = isentos & convocados
print '%6d isentos foram convocados' % len(isen_conv)
print '%5.1f%% dos isentos foram convocados' % (
            float(len(isen_conv))/len(isentos)*100)
print '%5.1f%% dos convocados eram isentos' % (
            float(len(isen_conv))/len(convocados)*100)
print
            
isen_apro = isentos & aprovados
print '%6d isentos foram aprovados' % len(isen_apro)
print '%5.1f%% dos isentos foram aprovados' % (
            float(len(isen_apro))/len(isentos)*100)
print '%5.1f%% dos aprovados eram isentos' % (
            float(len(isen_apro))/len(aprovados)*100)
        

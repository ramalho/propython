#!/usr/bin/env python
# coding: utf-8

import csv
from operator import itemgetter

regioes = {}
total = 0
for reg, uf, pop in csv.reader(file('censo2000.csv')):
    pop = int(pop)
    regioes[reg] = regioes.get(reg, 0) + pop
    total += pop
    
regioes = regioes.items()
regioes.sort(key=itemgetter(1), reverse=True)
for reg, pop in regioes:
    pct = float(pop)/total * 100
    print '%16s %8d (%4.1f%%)' % (reg, pop, pct)

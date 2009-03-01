#!/usr/bin/env python
# coding: utf-8

from mediana import mediana

pops = [int(n) for n in file('censo2000pop.txt')]
total = sum(pops)
pop_mediana = mediana(pops)
maiores = [n for n in pops if n > pop_mediana]
print 'pop.total: %9d' % total
print 'maior    : %9d' % max(pops)
print 'menor    : %9d' % min(pops)
print 'media    : %9d' % (total/len(pops))
print 'mediana  : %9d' % pop_mediana
print 'maiores  : %9d' % sum(maiores)
print '           %0.2f%%' % (float(sum(maiores))/total*100)


# para exibir numeros com separadores de milhares

import locale
locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")
print locale.format("%d", total, True) 


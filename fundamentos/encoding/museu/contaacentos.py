#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import sys

freqs = {}
texto = file(sys.argv[1]).read()
for car in texto:
    if ord(car) > 127:
        freqs[car] = freqs.get(car, 0) + 1

nao_ascii = freqs.items()
nao_ascii = [ (freq, letra) for (letra, freq) in nao_ascii ]
for freq, car in reversed(sorted(nao_ascii)):
    print '%x\t%s' % (ord(car), freq)
    


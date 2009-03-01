#!/usr/bin/env python

import re
padrao = re.compile(r"[^A-Z]*([A-Z][A-Z ]+[A-Z])[^A-Z ]*")

for lin in file('amostra_nomes.txt'):
    lin = lin.strip().upper()
    if not lin or lin.startswith('#'): continue
    print lin
    nome = padrao.match(lin)
    print repr(nome.group(1))
    print

        
        
#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Este programa demonstra a gravação de um 
pickle comprimido.

'''

import sys
from bz2 import BZ2File
from pickle import dump
sys.path.append('temporeal.zip')
from temporeal.catalogo import livros

bzip = BZ2File('temporeal_pickle.bz2','w')
dump(livros, bzip, -1)
bzip.close()
print 'temporeal_pickle.bz2 gravado'






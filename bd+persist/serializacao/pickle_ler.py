#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Este programa demonstra a leitura de um 
pickle comprimido.

'''

from bz2 import BZ2File
from pickle import load
from pprint import pprint

bzip = BZ2File('temporeal_pickle.bz2','r')
livros = load(bzip)
bzip.close()
print 'temporeal_pickle.bz2 lido'

print len(livros), 'livros na lista'

print '_' * 70
print 'O primeiro livro:'
pprint(livros[0])

meio = len(livros)/2
print '_' * 70
print 'O livro do meio (#%s):' % meio
pprint(livros[meio])

print '_' * 70
print 'O último livro:'
pprint(livros[-1])






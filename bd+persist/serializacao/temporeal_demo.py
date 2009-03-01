#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Este programa demonstra a importacao de um pacote
a partir de um arquivo zip.

O arquivo foi criado com o comando:

$ zip temporeal.zip temporeal/*

E o conteudo de temporeal/ é:

  __init__.py
  catalogo.py
'''

import sys
from pprint import pprint
sys.path.append('temporeal.zip')
from temporeal.catalogo import livros
print len(livros), 'livros no catalogo'

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



#!/usr/bin/env python
#-*- coding:utf-8 -*-
from random import shuffle

palavra = 'python'
print palavra
l = list(palavra)
print l
shuffle(l)
print l
palavraEmbaralhada = ''.join(l)
print palavraEmbaralhada

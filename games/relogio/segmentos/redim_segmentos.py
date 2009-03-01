#!/usr/bin/env python

from PIL import Image

for nome in ['%x' % i for i in range(16)]:
    nome_arq = nome.upper() + '.png'
    print 'lendo', nome_arq
    im = Image.open(nome_arq)
    im = im.resize((60,88), Image.ANTIALIAS)
    im.save('60x88/'+nome_arq)

#!/usr/bin/env python

from PIL import Image

mapa_segmentos = (
    ('0','01234567AE'),
    ('1','23'),
    ('2','012BF654'),
    ('3','012345B'),
    ('4','7FB23'),
    ('5','017FB345'),
    ('6','017FB3456'),
    ('7','01AE'),
    ('8','01234567FB'),
    ('9','0123457FB'),
    ('A','EA23B'),
    ('B','8F7654C'),
    ('C','017654'),
    ('D','786E'),
    ('E','017F654'),
    ('F','017F6'),
    ('G','0176543B'),
    ('H','2367FB'),
    ('I','019D54'),
    ('J','23456'),
    ('K','76FAC'),
    ('L','7654'),
    ('M','768A23'),
    ('N','768C23'),
    ('O','01234567'),
    ('P','01AF67'),
    ('Q','01234567C'),
    ('R','01AF67C'),
    ('S','018C54'),
    ('T','019D'),
    ('U','234567'),
    ('V','76EA'),
    ('W','76EC23'),
    ('X','8AEC'),
    ('Y','8AD'),
    ('Z','01AE54'),
) 

segmentos = {}

for nome in ['%X'% i for i in range(16)]:
    nome_arq = nome.upper() + '.png'
    segmentos[nome] = Image.open('seg60x88/'+nome_arq)

print segmentos  
dimensoes = segmentos['0'].size
    
for car, seq_segs in mapa_segmentos:
    im = Image.new('RGBA', dimensoes)
    for s in seq_segs:
        im.paste(segmentos[s],None,segmentos[s])
    im.save('completos/'+car+'.png')
    print car
    

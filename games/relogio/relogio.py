#!/usr/bin/env python

import pygame, sys
from pygame.locals import *

from romanos import romanoFormatado
from time import localtime

screen = pygame.display.set_mode((1024, 768))
screen = pygame.display.set_mode((1024, 768), FULLSCREEN | DOUBLEBUF)

digitos = {}
for car in [str(d) for d in range(10)]:
    digitos[car] = pygame.image.load('60x88/%s.png' % car)

clock = pygame.time.Clock()

def tratar_eventos():
    for event in pygame.event.get():
        if not hasattr(event, 'key'): continue
        if event.key == K_ESCAPE: sys.exit(0)
        
def exibir_numero(num, formato, y):
    ns = formato % num
    for pos, dig in enumerate(ns):
        if dig in digitos:
            screen.blit(digitos[dig], (10+64*pos, y))

alt_linha = 768/7
margem_topo = (768-alt_linha*7) / 2

contador = 1
while 1:
    screen.fill(0)
    dh_atual = localtime()[:6]
    ano = dh_atual[0]
    for linha, parte_hora in enumerate(dh_atual):
        if linha == 0: # ano
            formato = '%04d'
        else:
            formato = '%02d'
        exibir_numero(parte_hora, formato, linha*alt_linha + margem_topo)
    tratar_eventos()
    pygame.display.flip()
    clock.tick(60)
    contador += 1     
    if contador > 3999: 
        contador = 1   


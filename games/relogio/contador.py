#!/usr/bin/env python

import pygame, sys
from pygame.locals import *
screen = pygame.display.set_mode((1024, 768))
screen = pygame.display.set_mode((1024, 768), FULLSCREEN | DOUBLEBUF)

digitos = [pygame.image.load('60x88/%s.png' % c) for c in range(10)]

clock = pygame.time.Clock()

def tratar_eventos():
    for event in pygame.event.get():
        if not hasattr(event, 'key'): continue
        if event.key == K_ESCAPE: sys.exit(0)

while 1:
    for d in digitos:
        tratar_eventos()
        screen.fill(0)
        screen.blit(d, (100, 100))
        pygame.display.flip()
        clock.tick(1)
        


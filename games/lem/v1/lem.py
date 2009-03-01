#!/usr/bin/env python

import os, pygame
from pygame.locals import *
from random import randrange, choice
from vetor import Vetor as V

class Nave(pygame.sprite.Sprite):
    def __init__(self, imagem, pos, vel):
        pygame.sprite.Sprite.__init__(self) #inicializar Sprite
        self.poses = []
        self.image = pygame.image.load(imagem)
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = tuple(pos)
        self.vel = vel

    def acelerar(self, acel):
        self.vel = self.vel + acel

    def update(self):
        self.rect.move_ip( tuple(self.vel) )
        if self.rect.topleft[0] > 900: 
            self.rect.topleft = (-20,self.rect.topleft[1])
                
class Lem:
   def __init__(self, pos, vel):
       self.top = Nave('lem-top.png',pos,vel)
       offBase = V(-11,20)
       self.base = Nave('lem-base.png',pos+offBase,vel)
       self.acoplado = 1

   def acelerar(self, acel):
        self.top.vel = self.top.vel + acel
        if self.acoplado:
            self.base.vel = self.base.vel + acel
            
   def desacoplar(self):
       if tuple(self.base.vel) == (0,0):
           self.acoplado = 0          

   def update(self):
       self.top.update()
       self.base.update()
               
def main():
    #Initialize Everything
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.toggle_fullscreen()

    clock = pygame.time.Clock()

    fundo = pygame.image.load('earthrise800x600.jpg')
    fundo = fundo.convert()
    screen.blit(fundo, (0, 0))
    cm = Nave('cm-corgi.png',V(3,30),(1,0))
    lem = Lem(V(0,95),V(1,0))
    sprites = pygame.sprite.RenderPlain((lem.top, lem.base, cm,))

    while 1:
        clock.tick(60)

        #Handle Input Events
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            elif event.type == KEYDOWN :
                if   event.key == K_UP:    lem.acelerar(V(0,-1))
                elif event.key == K_DOWN:  lem.acelerar(V(0,1))
                elif event.key == K_LEFT:  lem.acelerar(V(-1,0))
                elif event.key == K_RIGHT: lem.acelerar(V(1,0))
                elif event.key == K_SPACE: lem.desacoplar()
                elif event.key == K_ESCAPE:
                    pygame.display.toggle_fullscreen()
                    raise SystemExit

        screen.blit(fundo, cm.rect, cm.rect)
        screen.blit(fundo, lem.top.rect, lem.top.rect)
        screen.blit(fundo, lem.base.rect, lem.base.rect)
        sprites.update()
        sprites.draw(screen)
        pygame.display.flip()
            
if __name__ == '__main__':
    main()



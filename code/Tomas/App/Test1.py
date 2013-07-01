from ejercicio import *

import sys

import pygame

pygame.init()

width = 680
height = 480

redColor = pygame.Color(255,0,0)
greenColor = pygame.Color(0,255,0)
blueColor = pygame.Color(0,0,255)
whiteColor = pygame.Color(255,255,255)
blackColor = pygame.Color(0,0,0)

window = pygame.display.set_mode((width,height))
window.fill(pygame.Color(255,255,255))
pygame.display.flip()

teclados = [0, 1, 2]

e = setup(teclados, width / 4, height / 4, width / 2, height / 2);

window.blit(e.canvas,(e.pos_x,e.pos_y))
pygame.display.flip()


while True:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit() 

from clases import *

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

LV = Listview(["Opcion 1", "Opcion 2", "Opcion 3", "Opcion 4"],width/4,height/4,width/2,height/2)

window.blit(LV.canvas,(LV.pos_x,LV.pos_y))
pygame.display.flip()

LV.react("-v")
LV.react("-v")
LV.react("-v")
LV.react("-v")
LV.react("-v")
LV.react("-v")
LV.react("-v")
LV.react("-v")
window.blit(LV.canvas,(LV.pos_x,LV.pos_y))
pygame.display.flip()

while True:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            sys.exit(0) 

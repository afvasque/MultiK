# coding: utf-8
from ejercicio import *
from Alumno import *

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

alumnos = []
for i in range(12):
    alumnos.append(Alumno(i))
    alumnos[i].audio = i
    alumnos[i].grupo = int(i/3)
 
alumnos[0].name = u"Tomás"
alumnos[1].name = "Andrea"
alumnos[2].name = "Esteban"
alumnos[3].name = "Gabriel"
alumnos[4].name = "Enzo"
alumnos[5].name = "Aldo"
alumnos[6].name = "Miguel"
alumnos[7].name = "Jose"
alumnos[8].name = "Isidora"
alumnos[9].name = "Vale"
alumnos[10].name = "Igor"
alumnos[11].name = u"Simón"

Grupos = []
for i in range(4):
    Grupos.append([])
    Grupos[i].append(alumnos[3 * i])
    Grupos[i].append(alumnos[3 * i + 1])
    Grupos[i].append(alumnos[3 * i + 2])

ejercicios = []
ejercicios.append(ejercicio3(Grupos[0],0,0,width / 2, height / 2))
ejercicios.append(ejercicio3(Grupos[1],1,0,width / 2, height / 2))
ejercicios.append(ejercicio3(Grupos[2],0,1,width / 2, height / 2))
ejercicios.append(ejercicio3(Grupos[3],1,1,width / 2, height / 2))


ejercicios[0].react(1,"->")
ejercicios[0].react(2,"->")

ejercicios[1].react(3,"->")
ejercicios[1].react(4,"->")
ejercicios[1].react(3,"Enter")
ejercicios[1].react(5,"Enter")

ejercicios[2].react(7,"Enter")
ejercicios[2].react(8,"Enter")

'''
ejercicios[0].react(0,"a")
ejercicios[1].react(3,"x")
ejercicios[1].react(4,"h")
ejercicios[1].react(5,"m")
ejercicios[1].react(5,"Enter")
ejercicios[2].react(6,"a")
ejercicios[2].react(7,"s")
ejercicios[2].react(8,"t")
ejercicios[2].react(6,"Enter")
ejercicios[2].react(7,"Enter")
'''

for i in range(4):
    window.blit(ejercicios[i].screen(),(ejercicios[i].pos_x * width / 2,ejercicios[i].pos_y * height / 2))
#window.blit(e.canvas,(e.pos_x,e.pos_y))
pygame.display.flip()


while True:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit() 

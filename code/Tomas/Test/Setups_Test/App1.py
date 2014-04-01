# coding=utf-8
import math
import sys
import pygame
from Setups import *
from pygame.locals import *

#Setup inicial
width = 900
height = 500

num_teclados = 21

num_grupos = int(num_teclados/3)
if num_teclados%3 > 0:
    num_grupos+=1
	
line_number_x = int(math.sqrt(num_grupos))
line_number_y = int(math.sqrt(num_grupos))

if line_number_x * line_number_y < num_grupos:
    line_number_x+=1

if line_number_x * line_number_y < num_grupos:
    line_number_y+=1

window = pygame.display.set_mode((width,height))#, pygame.FULLSCREEN)

#ejercicios = []

#Pareamiento y grupos

Grupos_inicial = []
Alumnos_grupo = []
Audio = []
Setups = []
Alumnos = []
Managers = []

Grupos_Listos = []
Espacios_Listos = []

lib_play_proc = []
text_to_speech_queue = []


for i in range(num_grupos):
	if num_teclados >= 3 * i + 2:
		Grupos_inicial.append([3 * i, 3 * i + 1, 3 * i + 2])
	elif num_teclados == 3 * i + 1:
		Grupos_inicial.append([3 * i, 3 * i + 1])
	else:
		Grupos_inicial.append([3 * i])

for i in range(num_grupos):
	for j in range(len(Grupos_inicial[i])):
		Setups.append(Pareamiento(Grupos_inicial[i][j],i%line_number_x, 3 * (i/line_number_x) + j, width/line_number_x,height/(3 * line_number_y)))
		Setups[3 * i + j].value = 3*i+j
		window.blit(Setups[3 * i + j].screen(),(Setups[3 * i + j].width *Setups[3 * i + j].pos_x,Setups[3 * i + j].height *Setups[3 * i + j].pos_y))

pygame.display.flip()

fpsClock = pygame.time.Clock()

while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
			
	fpsClock.tick(30)

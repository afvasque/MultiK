import usb.core
import threading
import math
from keyboard_library_queue import *
import event
import sys
import pygame
from clases import *
from threading import Thread

width = 900
height = 700

lib = KeyboardLibrary()

lib.detect_all_keyboards(0x0e8f,0x0022)
num_teclados = lib.get_total_keyboards()

num_grupos = num_teclados/3
if num_teclados%3 > 0:
    num_grupos+=1
	
line_number_x = int(math.sqrt(num_grupos))
line_number_y = int(math.sqrt(num_grupos))

if line_number_x * line_number_y < num_grupos:
    line_number_x+=1

if line_number_x * line_number_y < num_grupos:
    line_number_y+=1

window = pygame.display.set_mode((width,height))#, pygame.FULLSCREEN)

ejercicios = []

for i in range(num_grupos):
    teclados_grupo = []
    if num_teclados >= 3 * i + 2:
        teclados_grupo = [3 * i, 3 * i + 1, 3 * i + 2]
    elif num_teclados == 3 * i + 1:
        teclados_grupo = [3 * i, 3 * i + 1]
    else:
        teclados_grupo = [3 * i]
    #ejercicios.append(ejercicio1(teclados_grupo,i%line_number_x,i/line_number_x,width/line_number_x,height/line_number_y))
    #ejercicios.append(Textbox(teclados_grupo[i],i%line_number_x,i/line_number_x,width/line_number_x,height/line_number_y))
    ejercicios.append(Textbox(teclados_grupo[i],0,0,300,40))
    window.blit(ejercicios[i].screen(),(ejercicios[i].width *ejercicios[i].pos_x,ejercicios[i].height *ejercicios[i].pos_y))

pygame.display.flip()

def Keyboard_event(sender, earg):
    print "#%s : %s" % (earg['id'], earg['char'])  # 0: id, 1: teclas
    grupo = int(int(earg['id'])/3)
    ejercicios[grupo].react(int(earg['id']), earg['char'])    
    window.blit(ejercicios[grupo].screen(),(ejercicios[grupo].width *ejercicios[grupo].pos_x,ejercicios[grupo].height *ejercicios[grupo].pos_y))
    pygame.display.flip()

def close():
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

Thread(target=close).start()

lib.keypress += Keyboard_event

lib.run(0x0e8f,0x0022)

#while True:
#    for event in pygame.event.get(): 
#        if event.type == pygame.QUIT: 
#            sys.exit(0)


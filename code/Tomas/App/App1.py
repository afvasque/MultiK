import usb.core
import threading
import math
from keyboard_library_queue import *
import event
import sys
import pygame
from ejercicio import *

width = 1200
height = 800

lib = KeyboardLibrary()

lib.detect_all_keyboards(0x0e8f,0x0022)
num_teclados = lib.get_total_keyboards()

num_grupos = num_teclados/3
if num_teclados%3 > 0:
    num_grupos+=1
	
line_number = int(math.sqrt(num_grupos))

if math.floor(math.sqrt(num_grupos)) < math.sqrt(num_grupos):
    line_number+=1

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
    ejercicios.append(ejercicio1(teclados_grupo,i%line_number,i/line_number,width/line_number,height/line_number))
    window.blit(ejercicios[i].screen(),(ejercicios[i].width *ejercicios[i].pos_x,ejercicios[i].height *ejercicios[i].pos_y))

pygame.display.flip()

def Keyboard_event(sender, earg):
    print "#%s : %s" % (earg['id'], earg['char'])  # 0: id, 1: teclas
    grupo = int(int(earg['id'])/3)
    ejercicios[grupo].react(int(earg['id']), earg['char'])
    if(ejercicios[grupo].finished):
        ejercicios[grupo] = ejercicio2(ejercicios[grupo].teclados, ejercicios[grupo].pos_x, ejercicios[grupo].pos_y, ejercicios[grupo].width, ejercicios[grupo].height)
    window.blit(ejercicios[grupo].screen(),(ejercicios[grupo].width *ejercicios[grupo].pos_x,ejercicios[grupo].height *ejercicios[grupo].pos_y))
    pygame.display.flip()

def close():
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()

Thread(target=close).start()

lib.keypress += Keyboard_event

lib.run(0x0e8f,0x0022)

#while True:
#    for event in pygame.event.get(): 
#        if event.type == pygame.QUIT: 
#            sys.exit(0)


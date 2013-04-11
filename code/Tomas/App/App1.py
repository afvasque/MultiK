#import usb.core
import threading
import math
#from keyboard_library_queue import *
import event
import sys
import pygame
from ejercicio import *

width = 1366
height = 768

#lib.detect_all_keyboards(0x0e8f,0x0022)
#num_teclados = lib.get_total_keyboards()
num_teclados = 43;

num_grupos = num_teclados/3
if num_teclados%3 > 0:
    num_grupos+=1
	
line_number = int(math.sqrt(num_grupos))

if math.floor(math.sqrt(num_grupos)) < math.sqrt(num_grupos):
    line_number+=1

window = pygame.display.set_mode((width,height))

ejercicios = []

for i in range(num_grupos):
    teclados_grupo = []
    if num_teclados >= i + 2:
        teclados_grupo = [0,1,2]
    elif num_teclados == i + 1:
        teclados_grupo = [0,1]
    else:
        teclados_grupo = [0]
    ejercicios.append(ejercicio1(teclados_grupo,i%line_number,i/line_number,width/line_number,height/line_number))
    window.blit(ejercicios[i].screen(),(ejercicios[i].width *ejercicios[i].pos_x,ejercicios[i].height *ejercicios[i].pos_y))

pygame.display.flip()

while True:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            sys.exit(0)


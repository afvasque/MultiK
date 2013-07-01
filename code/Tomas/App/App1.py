# coding=utf-8
import usb.core
import threading
import math
from keyboard_library_queue import *
import event
import sys
import pygame
from ejercicio import *
import multiprocessing
from threading import Thread
from Alumno import *
from Setups import *
import audio_library

audio_lib = audio_library.AudioLibrary()

#Setup inicial
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

#Pareamiento y grupos

Grupos = []
Grupos_inicial = []
Alumnos_grupo = []
Audio = []
Setups = []
Alumnos = []

lib_play_proc = []
text_to_speech_queue = []

for i in range(num_teclados):
	Grupos.append(False)
	Audio.append(False)
	Alumnos.append(Alumno(i))
	text_to_speech_queue.append(multiprocessing.Queue())
	lib_play_proc.append(multiprocessing.Process(target=audio_lib.play, args=(i, text_to_speech_queue[i])))
	lib_play_proc[i].start()

for i in range(num_grupos):
	Alumnos_grupo.append([])
	if num_teclados >= 3 * i + 2:
		Grupos_inicial.append([3 * i, 3 * i + 1, 3 * i + 2])
	elif num_teclados == 3 * i + 1:
		Grupos_inicial.append([3 * i, 3 * i + 1])
	else:
		Grupos_inicial.append([3 * i])

for i in range(num_grupos):
	for j in range(len(Grupos_inicial[i])):
		Setups.append(Pareamiento(Grupos_inicial[i][j],i%line_number_x,i/line_number_x + j,width/line_number_x,height/(3 * line_number_y)))
		window.blit(Setups[3 * i + j].screen(),(Setups[3 * i + j].width *Setups[3 * i + j].pos_x,Setups[3 * i + j].height *Setups[3 * i + j].pos_y))

pygame.display.flip()


def TexttoSpeech(text_to_speech, id_audifono):
	global lib_play_proc
	global text_to_speech_queue
	#if lib_play_proc is None:
	#	text_to_speech_queue = multiprocessing.Queue()
	#	lib_play_proc = multiprocessing.Process(target=audio_lib.play, args=(id_audifono, text_to_speech_queue))
	#	lib_play_proc.start()          
		
	if len(text_to_speech)>0:
		print "Reproduciendo en audifono #%s: \"%s\"" % (id_audifono, text_to_speech)
		audio_lib.reproduciendo[id_audifono]=True
		print str(id_audifono)+" "+str(audio_lib.reproduciendo[id_audifono])
		text_to_speech_queue[id_audifono].put(text_to_speech)

def Keyboard_event(sender, earg):
	print "#%s : %s" % (earg['id'], earg['char'])  # 0: id, 1: teclas
	alumno = Alumnos[int(earg['id'])]
	text = str(earg['char']).decode('utf-8')
	if alumno.ready:
		grupo = alumno.grupo
	else: #Todo lo que es el pareamiento y organizacion en grupos
		if text=="Pow":
			if Audio[alumno.id] == False:
				for i in range(num_teclados):
					if Audio[i] == False:
						TexttoSpeech("Escribe el número %d" % i, i)
			else:
				TexttoSpeech("Repitiendo", Audio[alumno.id])
		else:
			Setups[alumno.id].react(text)
			window.blit(Setups[alumno.id].screen(),(Setups[alumno.id].width * Setups[alumno.id].pos_x, Setups[alumno.id].height * Setups[alumno.id].pos_y))
	pygame.display.flip()

lib.keypress += Keyboard_event

lib.run(0x0e8f,0x0022)
		
'''
for i in range(num_grupos):
    teclados_grupo = []
    if num_teclados >= 3 * i + 2:
        teclados_grupo = [3 * i, 3 * i + 1, 3 * i + 2]
    elif num_teclados == 3 * i + 1:
        teclados_grupo = [3 * i, 3 * i + 1]
    else:
        teclados_grupo = [3 * i]
    ejercicios.append(ejercicio1(teclados_grupo,i%line_number_x,i/line_number_x,width/line_number_x,height/line_number_y))
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
'''

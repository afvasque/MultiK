# coding=utf-8

from Alumno import *
import usb.core
import threading
import math
from keyboard_library_queue import *
import event
import time
import logging

import pygame
import audio_library

import sys
from ejercicio import *
import multiprocessing
from threading import Thread
from Setups import *
from Manager import *
from PreguntaColaborativa import *



audio_lib = audio_library.AudioLibrary()

logging.basicConfig(filename='multik.log',level=logging.INFO)

#Setup inicial
width = 800
height = 600

lib = KeyboardLibrary()

#lib.detect_all_keyboards(0x0e8f,0x0022)
#lib.detect_all_keyboards([[0x0e8f,0x0022],[0x0e6a,0x6001]])

#num_teclados = lib.get_total_keyboards()
num_teclados = lib.total_keyboards

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

for i in range(num_teclados):
	Audio.append(None)
	Alumnos.append(Alumno(i))
	text_to_speech_queue.append(multiprocessing.Queue())
	lib_play_proc.append(multiprocessing.Process(target=audio_lib.play, args=(i, text_to_speech_queue[i])))
	lib_play_proc[i].start()

for i in range(num_grupos):
	Alumnos_grupo.append([])
	Managers.append(None)
	#ejercicios.append(False)
	#Manejo de no multiplos de 3, completar
	if num_teclados >= 3 * i + 2:
		Grupos_inicial.append([3 * i, 3 * i + 1, 3 * i + 2])
	elif num_teclados == 3 * i + 1:
		Grupos_inicial.append([3 * i, 3 * i + 1])
	else:
		Grupos_inicial.append([3 * i])

for i in range(num_grupos):
	for j in range(len(Grupos_inicial[i])):
		Setups.append(Pareamiento(Grupos_inicial[i][j],i%line_number_x, 3 * (i / line_number_x) + j, width/line_number_x,height/(3 * line_number_y)))
		#hhhffhtyytyrtySetups[3 * i + j].value = 3*i+j
		window.blit(Setups[3 * i + j].screen(),(Setups[3 * i + j].width *Setups[3 * i + j].pos_x,Setups[3 * i + j].height *Setups[3 * i + j].pos_y))
	pygame.event.set_allowed([pygame.QUIT, pygame.MOUSEBUTTONUP])

#Agregar los espacios que sobran a los espacios disponibles
if (line_number_x * line_number_y) > num_grupos:
	espacios_sobrantes = (line_number_x * line_number_y) - num_grupos
	print "Espacios sobrantes: %d" % espacios_sobrantes
	for i in range(espacios_sobrantes):
		indice = num_grupos + i
		print indice
		Setups.append(empty_setup(indice/line_number_x, (indice % line_number_x), width/line_number_x,height/(3 * line_number_y)))
		Espacios_Listos.append(len(Setups) - 1)
		#window.blit(Setups[len(Setups) - 1].screen(),(Setups[len(Setups) - 1].width *Setups[len(Setups) - 1].pos_x,Setups[len(Setups) - 1].height *Setups[len(Setups) - 1].pos_y))
		
		
pygame.display.flip()


def TexttoSpeech(text_to_speech, id_audifono):
	audio_lib.play(id_audifono, text_to_speech)
	#global lib_play_proc
	#global text_to_speech_queue        
		
	#if len(text_to_speech)>0:
	#	print "Reproduciendo en audifono #%s: \"%s\"" % (id_audifono, text_to_speech)
	#	audio_lib.reproduciendo[id_audifono]=True
	#	print str(id_audifono)+" "+str(audio_lib.reproduciendo[id_audifono])
	#	text_to_speech_queue[id_audifono].put(text_to_speech)

def Keyboard_event(sender, earg):
	print "#%s : %s" % (earg['id'], earg['char'])  # 0: id, 1: teclas
	alumno = Alumnos[int(earg['id'])]
	text = str(earg['char']).decode('utf-8')
	if alumno.ready:
		if text=="Pow":#Repetir la instruccion
			TexttoSpeech(u"%s" % Managers[alumno.grupo].getAudio(), alumno.audio)
		else:
			Managers[alumno.grupo].ejercicio.react(int(earg['id']),text)
		if(Managers[alumno.grupo].ejercicio.finished):#Vemos si avanzamos al siguiente ejercicio
			print "Grupo Listo"
			if Managers[alumno.grupo].correct():
				print "Grupo respuesta correcta"
				if Managers[alumno.grupo].nivel > 0:
					for a in Alumnos_grupo[alumno.grupo]:				
						# CORRECT_ANSWER, pregunta, audio_pregunta, respuesta
						logging.info(u"[%f: [%d, %s, %s, %s, %s] ], " % (time.time(), a.numero_lista, 'CORRECT_ANSWER', Managers[alumno.grupo].ejercicio.pregunta.preguntas[0],Managers[alumno.grupo].ejercicio.pregunta.audios[0],Managers[alumno.grupo].ejercicio.inputs[Managers[alumno.grupo].ejercicio.teclados.index(a.id)]))	
				Managers[alumno.grupo].advance()
				for a in Alumnos_grupo[alumno.grupo]:
					TexttoSpeech(u"Muy bien.. %s" % Managers[alumno.grupo].getAudio(), a.audio)
					#TexttoSpeech(Managers[alumno.grupo].getAudio(), a.audio)
				#ejercicios[alumno.grupo] = ejercicios[alumno.grupo].next()
			else:
				for a in Alumnos_grupo[alumno.grupo]:
					TexttoSpeech(u"Intentelo de nuevo.. %s" % Managers[alumno.grupo].getAudio(), a.audio)
					if Managers[alumno.grupo].nivel > 0:
						for a in Alumnos_grupo[alumno.grupo]:
							# WRONG_ANSWER, pregunta, audio_pregunta, respuesta alumno, respuesta
							logging.info("[%f: [%d, %s, %s, %s, %s, %s] ], " % (time.time(), a.numero_lista, 'WRONG_ANSWER', Managers[alumno.grupo].ejercicio.pregunta.preguntas[0],Managers[alumno.grupo].ejercicio.pregunta.audios[0],Managers[alumno.grupo].ejercicio.inputs[Managers[alumno.grupo].ejercicio.teclados.index(a.id)],Managers[alumno.grupo].ejercicio.pregunta.respuestas[0]))	
					
				print "Grupo respuesta incorrecta"
		window.blit(Managers[alumno.grupo].ejercicio.screen(),(Managers[alumno.grupo].width * Managers[alumno.grupo].pos_y, Managers[alumno.grupo].height * Managers[alumno.grupo].pos_x)) #Actualizamos el ejercicio
	else: #Todo lo que es el pareamiento y organizacion en grupos
		if text=="Pow":#Repetir el texto
			if alumno.audio == "":#Repetirselo a todos lo que no estan pareados
				for i in range(num_teclados):
					if Audio[i] is None:
						TexttoSpeech("Escribe el número %d" % i, i)
			else:
				TexttoSpeech(Setups[alumno.id].get_audio_text(), alumno.audio)
		elif text=="Enter":#Recibir el input
			if alumno.audio == "":#Revisar si esta pareando el audio
				value = Setups[alumno.id].value
				if value < 0 or value >= len(Audio):#Revisar que sea un valor valido
					while Setups[alumno.id].value > 0:
						Setups[alumno.id].react("Back")#Borramos lo que haya metido
				elif Audio[value] is None: #Revisar que nadie mas tenga ese audio
					Audio[value] = alumno.id
					alumno.audio = value
					Setups[alumno.id] = setup_nombre(Setups[alumno.id])#Siguiente setup
					TexttoSpeech(Setups[alumno.id].get_audio_text(), alumno.audio)#Le mandamos la instruccion
				else: #asumimos que si mete un audio que ya fue asignado es porque esta cometiendo el error ahora, no el de antes
					while Setups[alumno.id].value > 0:
						Setups[alumno.id].react("Back")#Borramos lo que haya metido
			elif alumno.name == "": #Si ya tiene audio puede que este metiendo su nombre
				if(Setups[alumno.id].value() > 0): #Si ingreso su nombre
					alumno.set_name(Setups[alumno.id].value())
					Setups[alumno.id] = setup_grupo(Setups[alumno.id])#Siguiente setup
					TexttoSpeech(Setups[alumno.id].get_audio_text(), alumno.audio)#Le mandamos la instruccion
				else: #Se le repite la instruccion
					TexttoSpeech(Setups[alumno.id].get_audio_text(), alumno.audio)#Le mandamos la instruccion
			elif alumno.grupo == -1: #Lo ultimo que queda es que sea la formacion de grupos
				value = Setups[alumno.id].value()
				if value < 0 or value >= num_grupos: #Ingresado un valor no valido
					TexttoSpeech("Ese grupo no existe", alumno.audio)#Se le avisa que no existe
				elif len(Alumnos_grupo[value]) >= 3: #Revisamos si el grupo ya esta lleno
					TexttoSpeech("Ese grupo ya esta lleno", alumno.audio)#Se le avisa que esta lleno
				else: #Se agrega el alumno al grupo
					alumno.grupo = value
					Alumnos_grupo[value].append(alumno)
					Setups[alumno.id] = setup_wait(Setups[alumno.id]) #Pantalla para esperar a que el grupo este listo y halla un espacio disponible
					window.blit(Setups[alumno.id].screen(),(Setups[alumno.id].width * Setups[alumno.id].pos_x, Setups[alumno.id].height * Setups[alumno.id].pos_y))
					if len(Alumnos_grupo[alumno.grupo]) == 3:#Revisamos si el grupo esta listo
						Grupos_Listos.append(alumno.grupo)
						print "Grupo %s listo" % (alumno.grupo)
					index_espacio = int(alumno.id / 3)
					if Setups[3 * index_espacio].waiting() and Setups[3 * index_espacio + 1].waiting() and Setups[3 * index_espacio + 2].waiting(): #revisamos si el espacio esta listo
						Espacios_Listos.append(index_espacio)
						print "Espacio %s listo" % (index_espacio)
					if len(Grupos_Listos) > 0 and len(Espacios_Listos) > 0: #Revisamos si hay un grupo listo y un espacio en el que meterlos
						Espacio_Listo = Espacios_Listos.pop(0)
						Grupo_Listo = Grupos_Listos.pop(0)
						Grupo_Listo = Alumnos_grupo[Grupo_Listo]
						for i in range(len(Grupo_Listo)): #Setemos a los alumnos como listos para empezar
							Grupo_Listo[i].ready = True
							print "Alumno %s listo" % (Grupo_Listo[i].name)
						Managers[Grupo_Listo[0].grupo] = Manager(Grupo_Listo, Setups[Espacio_Listo].pos_x, Setups[Espacio_Listo].pos_y, Setups[Espacio_Listo].width, 3 * Setups[Espacio_Listo].height) #Creamos el primer ejercicio
						print "Asignado espacio %s a grupo %s" % (Espacio_Listo, Grupo_Listo[0].grupo)
						print "Posicion x:%d y:%d" %(Setups[Espacio_Listo].pos_x, Setups[Espacio_Listo].pos_y)
						window.blit(Managers[Grupo_Listo[0].grupo].ejercicio.screen(),(Managers[Grupo_Listo[0].grupo].width * Managers[Grupo_Listo[0].grupo].pos_y, Managers[Grupo_Listo[0].grupo].height * Managers[Grupo_Listo[0].grupo].pos_x)) #Lo metemos a la pantalla
						for i in range(len(Grupo_Listo)):
							TexttoSpeech(Managers[Grupo_Listo[0].grupo].getAudio(), Grupo_Listo[i].audio)
		else:
			Setups[alumno.id].react(text)
		if alumno.grupo == -1:
			window.blit(Setups[alumno.id].screen(),(Setups[alumno.id].width * Setups[alumno.id].pos_x, Setups[alumno.id].height * Setups[alumno.id].pos_y))
	pygame.display.flip()

class PygameThread(threading.Thread):    
    def run(self):
        clock = pygame.time.Clock()
        print("RUNNING")
        running = True
        while running:
            for ev in pygame.event.get():
                if ev.type == pygame.MOUSEBUTTONUP:
                    print("SALIR")
                    running = False
            clock.tick(20)            
        pygame.quit()
        sys.exit()
		
	
lib.keypress += Keyboard_event

try:

    pygame_thread = PygameThread()
    pygame_thread.start()
except:
    print("-----===== EXCEPTION threading exception =====-----")

lib.run()

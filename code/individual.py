# coding=utf-8
#Boa:Frame:Frame2

from src_pygame.Alumno import *
import usb.core
import threading
import math
from librerias.keyboard_library_queue import KeyboardLibrary
from src_pygame.event import Event
import time
import logging
import csv
import datetime

import pygame
import src_pygame.clases
from src_pygame.ejercicio import ejercicio
from src_pygame.Pareamiento import *
import librerias.audio_library






logging.basicConfig(filename='multik.log',level=logging.INFO)
logging.info("[%f: [%s] ], " % (time.time(),'APP_START'))




diccionario= []
lib = KeyboardLibrary()
Pareamientos= []
Alumnos = []
Audio= []
audio_lib = audio_library.AudioLibrary()
# Lee el archivo de persistencia y asocia el nro de alumno
# con el nivel del cual debe comenzar
alumnos_niveles = {}


def leer_persistencia(nombre_archivo):
    with open(nombre_archivo, 'rb') as csvfile:
        lista_reader = csv.reader(csvfile)
        for row in lista_reader:
            alumnos_niveles[row[0]] = row[1]



def Keyboard_event(sender, earg):
    id_sent= int(earg['id'])
    text= str(earg['char']).decode('utf-8')
    time_pressed = earg['time_pressed']

    alumno = Alumnos[id_sent]

    # Action to take is being determined. Log as event.
    logging.info("[%f: [%d, %f, %s, '%s'] ], " % (time.time(), id_sent, time_pressed, 'CHAR_ACTION_DETERMINATION', text))

    # Alumno se encuentra pareado
    if alumno.ready:

        if text=="Pow": 
            diccionario[alumno.Id].RepetirPregunta()
        else:

            diccionario[alumno.Id].Keyboard_Pressed(sender,earg)
            window.blit(diccionario[alumno.Id].screen(),(diccionario[alumno.Id].width *diccionario[alumno.Id].pos_x,diccionario[alumno.Id].height *diccionario[alumno.Id].pos_y))

    # Alumno no se encuentra pareado
    else:
        if text=="Pow": 
            if Audio[alumno.Id] is None:
                for i in range(len(Audio)):
                    if i not in Audio:
                        TexttoSpeech(i,"Escribe el número "+str(i))
            else:
                TexttoSpeech(Audio[alumno.Id],"Ingresa tu número de lista")

        else:
            Pareamientos[alumno.Id].ModificarPareamiento(alumno,Audio,earg)
            window.blit(Pareamientos[alumno.Id].screen(),(Pareamientos[alumno.Id].width *Pareamientos[alumno.Id].pos_x,Pareamientos[alumno.Id].height *Pareamientos[alumno.Id].pos_y))

            if Pareamientos[alumno.Id].recien_pareado == True:
                TexttoSpeech(Audio[alumno.Id],"Ingresa tu número de lista")
                Pareamientos[alumno.Id].recien_pareado= False 

            if Pareamientos[alumno.Id].pareado == True and  Pareamientos[alumno.Id].nombre_ingresado == True:
                alumno.ready= True
                
                #Obtener nivel inicial (persistencia)
                if alumno.nro_lista in alumnos_niveles.keys():
                    alumno.nivel_inicial = alumnos_niveles[alumno.nro_lista]

                ej=ejercicio.ejercicio(Pareamientos[alumno.Id].pos_x,Pareamientos[alumno.Id].pos_y,Pareamientos[alumno.Id].width,Pareamientos[alumno.Id].height,Pareamientos[alumno.Id].numero_audifono, alumno)
                diccionario[alumno.Id]=ej
                i= alumno.Id
                window.blit(diccionario[i].screen(),(diccionario[i].width *diccionario[i].pos_x,diccionario[i].height *diccionario[i].pos_y))

    pygame.display.flip()


def TexttoSpeech(audifono, tts):
    audio_lib.play(audifono, tts)

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



width = 1000
height = 700

# Parametros para leer persistencia
fecha_de_hoy = '2014-06-05' #str(datetime.date.today())
# Mitad 1 o 2 del curso
curso= "1"


keyboardsNum= lib.total_keyboards
print "Total de teclados: "+str(keyboardsNum)

leer_persistencia('archivos/ListasCSV/'+fecha_de_hoy+"_3B_"+curso+".csv")


line_number_x= int(math.sqrt(keyboardsNum))
line_number_y= int(math.sqrt(keyboardsNum))

if line_number_x * line_number_y < keyboardsNum:
    line_number_x+=1

if line_number_x * line_number_y < keyboardsNum:
    line_number_y+=1


window = pygame.display.set_mode((width,height))#, pygame.FULLSCREEN)


for i in range(keyboardsNum):    
    # Crear tantos alumnos como teclados se hayan detectado
    alumno= Alumno(i)
    Alumnos.append(alumno)
    Audio.append(None)
    diccionario.append(None)

    Pareamientos.append(Pareamiento(i%line_number_x,i/line_number_x,width/line_number_x,height/line_number_y))
    window.blit(Pareamientos[i].screen(),(Pareamientos[i].width *Pareamientos[i].pos_x,Pareamientos[i].height *Pareamientos[i].pos_y))

    TexttoSpeech(i, "Escribe el número "+str(i))
        
    pygame.event.set_allowed([pygame.QUIT, pygame.MOUSEBUTTONUP])

pygame.display.flip()               

lib.keypress += Keyboard_event

try:
    pygame_thread = PygameThread()
    pygame_thread.start()
except:
    print("-----===== EXCEPTION threading exception =====-----")

lib.run()


# coding=utf-8
#Boa:Frame:Frame2

from Alumno import *
import usb.core
import threading
import math
from keyboard_library_queue import *
import event
import time
import logging

import pygame
from Prueba_clases.clases import *
from Prueba_clases.ejercicio import *
from Pareamiento import *
import audio_library


diccionario= []
lib = KeyboardLibrary()
Pareamientos= []
Alumnos = []
Audio= []

logging.basicConfig(filename='multik.log',level=logging.INFO)

audio_lib = audio_library.AudioLibrary()


def Keyboard_event(sender, earg):
    
    print "#%s : %s" % (earg['id'], earg['char'])  # 0: id, 1: teclas
    text= str(earg['char']).decode('utf-8')
    id_sent= int(earg['id'])

    alumno = Alumnos[id_sent]

    # Alumno se encuentra pareado
    if alumno.ready:
        print "alumno listo"

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
                TexttoSpeech(Audio[alumno.Id],"Ingresa tu nombre")

        else:
            print "not par"
            Pareamientos[alumno.Id].ModificarPareamiento(alumno,Audio,earg)
            window.blit(Pareamientos[alumno.Id].screen(),(Pareamientos[alumno.Id].width *Pareamientos[alumno.Id].pos_x,Pareamientos[alumno.Id].height *Pareamientos[alumno.Id].pos_y))

            if Pareamientos[alumno.Id].pareado == True and  Pareamientos[alumno.Id].nombre_ingresado == False:
                TexttoSpeech(Audio[alumno.Id],"Ingresa tu nombre")

            if Pareamientos[alumno.Id].pareado == True and  Pareamientos[alumno.Id].nombre_ingresado == True:
                alumno.ready= True
                ej=ejercicio(Pareamientos[alumno.Id].pos_x,Pareamientos[alumno.Id].pos_y,Pareamientos[alumno.Id].width,Pareamientos[alumno.Id].height,Pareamientos[alumno.Id].numero_audifono, alumno)
                diccionario[alumno.Id]=ej
                i= alumno.Id
                window.blit(diccionario[i].screen(),(diccionario[i].width *diccionario[i].pos_x,diccionario[i].height *diccionario[i].pos_y))

    pygame.display.flip()



    '''
    if text=="Pow":
        temp= int(earg['id'])

        
        if diccionario[temp].pareado==True:
            diccionario[temp].RepetirPregunta()
            return
            
        for a in range(0,len(diccionario)):
            print str(a)+" estado:"+str(diccionario[a].pareado)
            if diccionario[a].pareado==False:
                print "repitiendo en: "+str(diccionario[a].numero_audifono)
                diccionario[a].RepetirPregunta()
        return

    if ((diccionario[int(earg['id'])].pareado == False) or (diccionario[int(earg['id'])].nombre_ingresado == False) ):
        temp= int(earg['id'])
        diccionario[temp].ModificarPareamiento(diccionario,earg)
        window.blit(diccionario[temp].screen(),(diccionario[temp].width *diccionario[temp].pos_x,diccionario[temp].height *diccionario[temp].pos_y))
        print "#%s : %s" % (earg['id'], earg['char'])  # 0: id, 1: teclas
        
    else:
        temp = int(earg['id'])

        op_type   = str(diccionario[temp].Operacion_actual.TipoOperacion)
        op_level  = str(diccionario[temp].Operacion_actual.nivelOperacion)
        user_name = str(diccionario[temp].Alumno_actual.Nombre)

        timestamp = time.time()

        diccionario[temp].Keyboard_Pressed(sender,earg)
        window.blit(diccionario[temp].screen(),(diccionario[temp].width *diccionario[temp].pos_x,diccionario[temp].height *diccionario[temp].pos_y))
        print "#%s : %s" % (earg['id'], earg['char'])  # 0: id, 1: teclas
    '''
    


def TexttoSpeech(audifono, tts):

    print "Reproduciendo en audifono #%s: \"%s\"" % (audifono, tts)
                    
    audio_lib.play(audifono, tts)


  #TODO: poner thread como padre
class ThreadKeyboard(threading.Thread):
    def run(self):
        lib.run([[0x0e8f,0x0022],[0x0e6a,0x6001]])

width = 1000
height = 700

lib.keypress += Keyboard_event
lib.detect_all_keyboards([[0x0e8f,0x0022],[0x0e6a,0x6001]])

keyboardsNum= lib.get_total_keyboards()
print "teclados: "+str(keyboardsNum)


line_number_x= int(math.sqrt(keyboardsNum))
line_number_y= int(math.sqrt(keyboardsNum))

if line_number_x * line_number_y < keyboardsNum:
    line_number_x+=1

if line_number_x * line_number_y < keyboardsNum:
    line_number_y+=1


window = pygame.display.set_mode((width,height))#, pygame.FULLSCREEN)
               

for i in range(keyboardsNum):    
        
    
    alumno= Alumno(i)
    Alumnos.append(alumno)
    Audio.append(None)
    diccionario.append(None)
    #ej=ejercicio(i%line_number_x,i/line_number_x,width/line_number_x,height/line_number_y,i,alumno)
    #diccionario[i]=ej

    Pareamientos.append(Pareamiento(i%line_number_x,i/line_number_x,width/line_number_x,height/line_number_y))
    window.blit(Pareamientos[i].screen(),(Pareamientos[i].width *Pareamientos[i].pos_x,Pareamientos[i].height *Pareamientos[i].pos_y))

    TexttoSpeech(i, "Escribe el número "+str(i))

pygame.display.flip()
        

t = ThreadKeyboard()
t.start()

  
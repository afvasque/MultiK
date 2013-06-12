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


diccionario= {}
lib = KeyboardLibrary()

logging.basicConfig(filename='multik.log',level=logging.INFO)


def Keyboard_event(sender, earg):
    
    text= str(earg['char']).decode('utf-8')
    if text=="Pow":
        temp= int(earg['id'])

        print "#%s : %s" % (earg['id'], earg['char'])  # 0: id, 1: teclas
        if diccionario[temp].pareado==True:
            diccionario[temp].RepetirPregunta()
            return
            
        for a in range(0,len(diccionario)):
            if (diccionario[a].pareado==False) or (diccionario[a].nombre_ingresado==False):
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

        
        logging.info("[%d: [%s, %s, %s, %s, %s] ], " % (timestamp, text, op_type, op_level, user_name, temp))

        diccionario[temp].Keyboard_Pressed(sender,earg)
        window.blit(diccionario[temp].screen(),(diccionario[temp].width *diccionario[temp].pos_x,diccionario[temp].height *diccionario[temp].pos_y))
        print "#%s : %s" % (earg['id'], earg['char'])  # 0: id, 1: teclas

    pygame.display.flip()


  #TODO: poner thread como padre
class ThreadKeyboard(threading.Thread):
    def run(self):
        lib.run(0x0e8f,0x0022)

width = 1000
height = 700

lib.keypress += Keyboard_event
lib.detect_all_keyboards(0x0e8f,0x0022)

keyboardsNum= lib.get_total_keyboards()
print "teclados: "+str(keyboardsNum)


line_number_x= int(math.sqrt(keyboardsNum))
line_number_y= int(math.sqrt(keyboardsNum))

if line_number_x * line_number_y < keyboardsNum:
    line_number_x+=1

if line_number_x * line_number_y < keyboardsNum:
    line_number_y+=1


window = pygame.display.set_mode((width,height))#, pygame.FULLSCREEN)


'''
Alumnos = list()

Alumnos.append(Alumno(1,"Andrea","Teclados"))
Alumnos.append(Alumno(2,"Miguel","Teclados"))
Alumnos.append(Alumno(3,"Esteban","Teclados"))
Alumnos.append(Alumno(4,"Enzo","Teclados"))
Alumnos.append(Alumno(5,"Felipe","Teclados"))
Alumnos.append(Alumno(6,"Tomás","Teclados"))
Alumnos.append(Alumno(7,"Gabriel","Teclados"))
Alumnos.append(Alumno(8,"José","Teclados"))
'''                     

for i in range(keyboardsNum):    
        
    
    alumno= Alumno(i,"","Teclados")
    ej=ejercicio(i%line_number_x,i/line_number_x,width/line_number_x,height/line_number_y,i,alumno)
    diccionario[i]=ej
    window.blit(diccionario[i].screen(),(diccionario[i].width *diccionario[i].pos_x,diccionario[i].height *diccionario[i].pos_y))

pygame.display.flip()
        

t = ThreadKeyboard()
t.start()

  
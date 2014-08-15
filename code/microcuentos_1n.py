# -*- coding: utf-8 -*-

from librerias.keyboard_library_queue import KeyboardLibrary
from librerias import audio_library
import manejo_pantalla
import pareamiento
import player

# Creacion objetos librerias
lib_teclados = KeyboardLibrary()
lib_audio = audio_library.AudioLibrary()

# Variables para mantener el estado actual del juego
en_pareamiento = False

num_keyboards = lib_teclados.total_keyboards

# Evento de teclado
def Keyboard_event(sender, earg):

    global en_pareamiento
    id_sent= int(earg['id'])
    text= str(earg['char']).decode('utf-8')
    time_pressed = earg['time_pressed']

    if text =="Enter":
    	if en_pareamiento:
    		en_pareamiento = pareamiento.parear(int(id_sent), manejo_pantalla.get_value(id_sent))
    elif text == "Pow":
    	# Repetir ultima instruccion
    	if en_pareamiento:
    		pareamiento.replay_pareamiento(lib_audio, int(id_sent))
    else:
    	manejo_pantalla.react(id_sent, text)


# Subscripcion a evento teclado
lib_teclados.keypress += Keyboard_event

manejo_pantalla.start(num_keyboards)


print "Total de teclados: "+str(lib_teclados.total_keyboards)


# Pareamiento
en_pareamiento = True
pareamiento.start(num_keyboards, lib_audio)

# Proceso teclados
lib_teclados.run()





    

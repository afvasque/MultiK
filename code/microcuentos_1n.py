# -*- coding: utf-8 -*-

from librerias.keyboard_library_queue import KeyboardLibrary
from librerias import audio_library
import manejo_pantalla
import pareamiento
import player
from manager_microcuentos import ManagerMicrocuentos
import time
import logging

logging.basicConfig(filename='multik.log',level=logging.INFO)

# Creacion objetos librerias
lib_teclados = KeyboardLibrary()
lib_audio = audio_library.AudioLibrary()
manager = ManagerMicrocuentos(lib_audio, lib_teclados)


# Variables para mantener el estado actual del juego
en_pareamiento = False
en_juego = False

num_keyboards = lib_teclados.total_keyboards


# Evento de teclado
def Keyboard_event(sender, earg):

    global en_pareamiento
    global en_juego
    id_sent= int(earg['id'])
    text= str(earg['char']).decode('utf-8')
    time_pressed = earg['time_pressed']

    if text =="Enter":
        if en_pareamiento:
            # Pareamiento.parear recibe num teclado, num audifono
            en_pareamiento = pareamiento.parear(id_sent, manejo_pantalla.get_value(id_sent))
            manager.add_player(id_sent, pareamiento.pareamientos[id_sent])
            en_juego = not en_pareamiento
        else:#elif en_juego:
            # Logica para cada jugador
            text = manejo_pantalla.get_value(id_sent)
            manager.verificar_respuesta(id_sent, text)
    elif text == "Pow":
        # Repetir ultima instruccion
        if en_pareamiento:
            pareamiento.replay_pareamiento(lib_audio, int(id_sent))
        else:
            manager.replay(id_sent)
    else:
        manejo_pantalla.react(id_sent, text)

    # Tiempo respuesta desde decision de Pucca
    logging.info("[%f: [%s, %f, %s, %s, %s, %s] ], " % (time.time(), id_sent, time_pressed, 'COCOYOC'))


# Subscripcion a evento teclado
lib_teclados.keypress += Keyboard_event

manejo_pantalla.start(num_keyboards)


print "Total de teclados: "+str(lib_teclados.total_keyboards)


# Pareamiento
en_pareamiento = True
pareamiento.start(num_keyboards, lib_audio)

# Proceso teclados
lib_teclados.run()





    

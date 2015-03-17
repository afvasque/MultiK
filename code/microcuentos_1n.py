# -*- coding: utf-8 -*-

from librerias.keyboard_library_queue import KeyboardLibrary
from librerias import audio_library
import manejo_pantalla
import pareamiento
import player
from manager_microcuentos import ManagerMicrocuentos
import time
import logging
import threading


logging.basicConfig(filename='multik.log',level=logging.INFO)

# Creacion objetos librerias
lib_teclados = KeyboardLibrary()
time.sleep(1)
lib_audio = audio_library.AudioLibrary()
manager = ManagerMicrocuentos(lib_audio, lib_teclados)


# Variables para mantener el estado actual del juego
en_pareamiento = False
en_juego = False
salido_de_pareamiento = 0


num_keyboards = lib_teclados.total_keyboards


# Evento de teclado
def Keyboard_event(sender, earg):
    try:
        global en_pareamiento
        global en_juego
        global salido_de_pareamiento
        id_sent= int(earg['id'])
        text= str(earg['char']).decode('utf-8')
        time_pressed = earg['time_pressed']

        # Action to take is being determined. Log as event.
        logging.info("[%f: [%d, %f, %s, '%s'] ], " % (time.time(), id_sent, time_pressed, 'CHAR_ACTION_DETERMINATION', text))

        if text =="Enter":
            if en_pareamiento:
                # Pareamiento.parear recibe num teclado, num audifono
                en_pareamiento = pareamiento.parear(id_sent, manejo_pantalla.get_value(id_sent))
                manager.add_player(id_sent, pareamiento.pareamientos[id_sent])
                en_juego = not en_pareamiento
            else:
                # Logica para cada jugador
                text = manejo_pantalla.get_value(id_sent)
                if text != "" or salido_de_pareamiento == 0:
                    manager.verificar_respuesta(id_sent, text)
                    salido_de_pareamiento = 1
                else:
                    lib_audio.play(pareamiento.pareamientos[id_sent], "¡No olvides escribir.!")
        elif text == "Pow":
            # Repetir ultima instruccion
            if en_pareamiento:
                pareamiento.replay_pareamiento(lib_audio, int(id_sent))
            else:
                manager.replay(id_sent)
        else:
            if not en_pareamiento and manager.lista_jugadores[id_sent].waiting_flag:
                pass
            else:
                manejo_pantalla.react(id_sent, text)

        # Tiempo respuesta desde decision de Pucca
        logging.info("[%f: [%d, %f, %s] ], " % (time.time(), id_sent, time_pressed, 'COCOYOC'))

    except Exception as e:
        print e

# Subscripcion a evento teclado
lib_teclados.keypress += Keyboard_event

pygame_thread = manejo_pantalla.start(num_keyboards)

print "Total de teclados: "+str(lib_teclados.total_keyboards)

# Pareamiento
en_pareamiento = True

pareamiento.start(num_keyboards, lib_audio)

#Proceso teclados
keyboards_thread = threading.Thread(target=lib_teclados.run, args=())
keyboards_thread.daemon = True
keyboards_thread.start()


while pygame_thread.isAlive():
    pass

print("---=== SALIENDO ===---")

#Generando microcuentos
manager.leer_cuento_final()

#Cerrando recursos
lib_audio.close_alsa_cards()
lib_teclados.close_keyboards()
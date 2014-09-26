# -*- coding: utf-8 -*-

import manejo_pantalla
from librerias.keyboard_library_queue import KeyboardLibrary
from librerias import audio_library
import time

pareamientos= {}
players = 0

def start(num_players, lib_audio):
	global players
	players = num_players
	frase = u"Escribe el número..."
	for i in range(num_players):
		lib_audio.play(i, frase + str(i))
		manejo_pantalla.write(i, frase, 0, 0)
		manejo_pantalla.draw_textbox(i,0.8)

def parear(num_keyboard, num_phone):
	global pareamientos
	global players_id

	pareamientos[num_keyboard] = int(num_phone)
	manejo_pantalla.reset_layout(num_keyboard)
	manejo_pantalla.write(num_keyboard, "Espera",0,0)

	logging.info("[%f: [%d, %d, %s, %s] ], " % (time.time(), num_phone, num_keyboard, 'PAREAMIENTO'))


	if len(pareamientos) == players:
		return False
	else:
		return True

def replay_pareamiento(lib_audio, id_sent):
	global players
	global pareamientos

	if id_sent not in pareamientos.keys():
		print(pareamientos.values())
		lista_pendiente = [x for x in range(players) if x not in pareamientos.values()]
		print(lista_pendiente)
		for i in lista_pendiente:
			frase = u"Escribe el número..."
			lib_audio.play(i, frase + str(i))

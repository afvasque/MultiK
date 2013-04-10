# coding=utf-8
import audio_library_2

import time
import multiprocessing


def imprimir_algo_en_pantalla(sender, earg):
	print "Terminó audio en " + str(earg)



lib = audio_library_2.AudioLibrary()
lib.finished += imprimir_algo_en_pantalla


for i in range(0,lib.get_total_usb_cards()):
	# text to play
	text_to_speech = "Hola. Tarjeta %d. Chao." % i
	lib.play(i, text_to_speech)

# wait for keypress before exiting
raw_input('Press [Enter] to exit.')

# coding=utf-8
import audio_library

def imprimir_algo_en_pantalla(sender, earg):
	print "Terminó audio en " + str(earg)



lib = audio_library.AudioLibrary()
lib.finished += imprimir_algo_en_pantalla

for i in range(0,lib.get_total_usb_cards()):
	print "Audio en tarjeta " + str(i) + "..."
	lib.play(i, "Hola. Tarjeta " + str(i) + ". Chao.")

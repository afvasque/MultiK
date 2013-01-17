# coding=utf-8
import audio_library
import time
import multiprocessing


def imprimir_algo_en_pantalla(sender, earg):
	print "Terminó audio en " + str(earg)



lib = audio_library.AudioLibrary()
lib.finished += imprimir_algo_en_pantalla

all_p = []

for i in range(0,lib.get_total_usb_cards()):
	# text to play
	text_to_speech = "Hola. Tarjeta %d. Chao." % i
	# create a process for each audio to play
	p = multiprocessing.Process(target=lib.play, args=(i, text_to_speech))
	# append to the process array
	all_p.append(p)
	# start it
	p.start()

# join all the processes...
for p in all_p:
	p.join()

# ...and continue running from here when they're joined
print "Chai."

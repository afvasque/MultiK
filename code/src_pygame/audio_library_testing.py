# coding=utf-8
import audio_library
import time
import multiprocessing

class LibTest:
	lib = audio_library.AudioLibrary()

	all_p = []
	all_q = []


	def imprimir_algo_en_pantalla(self, sender, earg):
		print "Terminó audio. Datos: " + str(earg)

	def terminate_proc(self, sender, earg):
		if earg['terminate']:
			print "Terminando proceso %s..." % str(self.all_p[earg['id']])
			self.all_p[earg['id']].terminate()

	def __init__(self):
		self.lib.finished += self.imprimir_algo_en_pantalla
		self.lib.finished += self.terminate_proc


		for i in range(0,self.lib.get_total_usb_cards()):
			# get a text from the queue
			text_to_speech_queue = multiprocessing.Queue()
			# create a process for each card
			p = multiprocessing.Process(target=self.lib.play, args=(i, text_to_speech_queue))
			# set as daemon
			p.daemon = True	
			# append to the process array
			self.all_p.append(p)
			# start it
			p.start()

			# append the queue to the queue array
			self.all_q.append(text_to_speech_queue)

			# text to play
			text_to_speech = "Hola. Tarjeta %d. Chao." % i
			tts_id = i # random id, used to identify the finished event
			# put the text into the corresponding queue
			text_to_speech_queue.put({'tts': text_to_speech, 'terminate': False, 'tts_id': tts_id})


		# Iterar de nuevo por todas las colas de tarjetas y terminar los procesos cuando terminen
		for idx, queue in enumerate(self.all_q):
			tts_id = idx + 1000
			text_to_speech = "Hola de nuevo, tarjeta %d." % idx
			queue.put({'tts': text_to_speech, 'terminate': True, 'tts_id': tts_id}) # True para terminar el proceso cuando termine de reproducir el audio

		for p in self.all_p:
			p.join()

LibTest()
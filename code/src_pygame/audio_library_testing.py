# coding=utf-8
import audio_library
import time
import multiprocessing

class LibTest:
	lib = audio_library.AudioLibrary()

	def print_finished_event(self, sender, earg):
		print "Terminó audio. Datos: " + str(earg)

	def __init__(self):
		self.lib.finished += self.print_finished_event


		for i in range(0,self.lib.get_total_usb_cards()):
			# text to play
			text_to_speech = "En Cocoyoc abundan los perros pug, querido alumno %d." % i
			# tell the lib to play the tts
			self.lib.play(i, text_to_speech)


		time.sleep(10)


LibTest()
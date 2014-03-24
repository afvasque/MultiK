# coding=utf-8
import audio_library
import time
import multiprocessing

class LibTest:
	lib = audio_library.AudioLibrary()

	def print_finished_event(self, sender, earg):
		print "Terminó audio. Datos: " + str(earg)

	def __init__(self):
		
		#while True:
		self.lib.finished += self.print_finished_event

		for i in range(0,self.lib.get_total_usb_cards()):
			# text to play
			text_to_speech = "Auricular %d." % i
			# tell the lib to play the tts
			self.lib.play(i, text_to_speech)
		time.sleep(2)


		for i in range(0,self.lib.get_total_usb_cards()):
			text_to_speech = "La primavera besaba"
			self.lib.play(i, text_to_speech)
		time.sleep(2)

		for i in range(0,self.lib.get_total_usb_cards()):
			text_to_speech = "suavemente la arboleda,"
			self.lib.play(i, text_to_speech)
		time.sleep(2)

		for i in range(0,self.lib.get_total_usb_cards()):
			text_to_speech = "y el verde nuevo brotaba"
			self.lib.play(i, text_to_speech)
		time.sleep(2)

		for i in range(0,self.lib.get_total_usb_cards()):
			text_to_speech = "como una verde humareda."
			self.lib.play(i, text_to_speech)
		time.sleep(2)



		for i in range(0,self.lib.get_total_usb_cards()):
			text_to_speech = "Las nubes iban pasando"
			self.lib.play(i, text_to_speech)
		time.sleep(2)

		for i in range(0,self.lib.get_total_usb_cards()):
			text_to_speech = "sobre el campo juvenil..."
			self.lib.play(i, text_to_speech)
		time.sleep(2)

		for i in range(0,self.lib.get_total_usb_cards()):
			text_to_speech = "Yo vi en las hojas temblando"
			self.lib.play(i, text_to_speech)
		time.sleep(2)

		for i in range(0,self.lib.get_total_usb_cards()):
			text_to_speech = "las frescas lluvias de abril."
			self.lib.play(i, text_to_speech)
		time.sleep(2)


		for i in range(0,self.lib.get_total_usb_cards()):
			text_to_speech = "Bajo ese almendro florido,"
			self.lib.play(i, text_to_speech)
		time.sleep(2)

		for i in range(0,self.lib.get_total_usb_cards()):
			text_to_speech = "todo cargado de flor"
			self.lib.play(i, text_to_speech)
		time.sleep(2)

		for i in range(0,self.lib.get_total_usb_cards()):
			text_to_speech = "-recordé-, yo he maldecido"
			self.lib.play(i, text_to_speech)
		time.sleep(2)

		for i in range(0,self.lib.get_total_usb_cards()):
			text_to_speech = "mi juventud sin amor."
			self.lib.play(i, text_to_speech)
		time.sleep(2)


		for i in range(0,self.lib.get_total_usb_cards()):
			text_to_speech = "Hoy en mitad de la vida,"
			self.lib.play(i, text_to_speech)
		time.sleep(2)

		for i in range(0,self.lib.get_total_usb_cards()):
			text_to_speech = "me he parado a meditar..."
			self.lib.play(i, text_to_speech)
		time.sleep(2)

		for i in range(0,self.lib.get_total_usb_cards()):
			text_to_speech = "Juventud nunca vivida,"
			self.lib.play(i, text_to_speech)
		time.sleep(2)

		for i in range(0,self.lib.get_total_usb_cards()):
			text_to_speech = "quién te volviera a soñar!"
			self.lib.play(i, text_to_speech)

		time.sleep(10)


LibTest()
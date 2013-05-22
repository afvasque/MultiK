# coding=utf-8

import usb.core
import usb.util
import wave
import os
import event
import time
import datetime
import alsaaudio
import subprocess
import multiprocessing


class AudioLibrary:

	card_array = []
	card_word_id_dictionary = {}

	finished = event.Event('Audio has finished playing.')
	
	# semaphore with limit of 7 because of the hub bandwidth limit of 12Mbit/s
	# since our bitrate is 1.54Mbit/s,
	# 12 / 1.54 = 7.7922 gives us that the limit is 7
	semaphore = multiprocessing.Semaphore(7)

	def __init__(self):
		cards1 = usb.core.find(find_all = True, idVendor=0x0d8c)
		cards2 = usb.core.find(find_all = True, idVendor=0x0c76)
		cards3 = usb.core.find(find_all = True, idVendor=0x1130)

		# Join the arrays into a single one
		self.card_array = cards1 + cards2 + cards3

		# Show how many were detected
		print '\033[94m' + "Detected " + str(self.get_total_usb_cards()) + " sound cards of the specified type(s)." + '\033[0m'
		
		# Find the word id for every card and save it into a dictionary
		#self.find_all_card_word_ids()

		# Detach the kernel driver from all the cards
		self.detach_all_cards()

	def get_total_usb_cards(self):
		return len(self.card_array)


	def detach_all_cards(self):
		count = 0

		for t in self.card_array:
			if t.is_kernel_driver_active(0):
				t.detach_kernel_driver(0)
				count = count + 1

		print "Detached the kernel driver from %d cards." % count

	def find_all_card_word_ids(self):
		for t in self.card_array:
			# Convert, for example, 2 into 002, 34 into 034, etc.
			usb_bus = '{s:{c}>{n}}'.format(s=t.bus,n=3,c='0')
			usb_address = '{s:{c}>{n}}'.format(s=t.address,n=3,c='0')

			# Find the card with the corresponding bus and address
			command = "grep \"%s/%s\" /proc/asound/card*/*" % (usb_bus, usb_address)
			usbbus = subprocess.check_output(command, shell=True)
			card_number = usbbus.split("/")
			
			# Find the word id for that device
			command = "cat /proc/asound/%s/id" % card_number[3]
			id_word = subprocess.check_output(command, shell=True)
			# Delete the \n at the end
			id_word = id_word[:-1]

			# Create element in dictionary
			self.card_word_id_dictionary[t] = id_word

	def find_card_word_id(self, device_index):
		t = self.card_array[device_index]
		usb_bus = '{s:{c}>{n}}'.format(s=t.bus,n=3,c='0')
		usb_address = '{s:{c}>{n}}'.format(s=t.address,n=3,c='0')

		# Find the card with the corresponding bus and address
		command = "grep \"%s/%s\" /proc/asound/card*/*" % (usb_bus, usb_address)
		usbbus = subprocess.check_output(command, shell=True)
		card_number = usbbus.split("/")
		
		# Find the word id for that device
		command = "cat /proc/asound/%s/id" % card_number[3]
		id_word = subprocess.check_output(command, shell=True)
		# Delete the \n at the end
		id_word = id_word[:-1]

		# Create element in dictionary
		self.card_word_id_dictionary[t] = id_word

		return id_word

	def play(self, device_index, text_to_speech):
		timestamp = time.mktime(datetime.datetime.now().timetuple())
		filename = "%d_%s" % (timestamp, device_index)

		# create the wav file
		# text2wave default voice can be changed in /etc/festival.scm. Add at the end, e.g.: (set! voice_default 'voice_JuntaDeAndalucia_es_sf_diphone)
		os.system("echo \"%s\" | text2wave -F 48000 -o %s.tmp" % (self.convert_intl_characters(text_to_speech), filename))
		# convert to stereo, thus doubling the bitrate
		os.system("sox %s.tmp -c 2 %s.wav" % (filename, filename))
		# remove the temporary file
		os.remove("%s.tmp" % filename)

		# acquire the semaphore, or wait until available
		self.semaphore.acquire()

		try:
			#find the usb device object representing the card
			card = self.card_array[device_index]
			#find the word id for the specified card
			#card_word_id = self.card_word_id_dictionary[card]
			
			#attach the kernel driver for the card
			print "\033[33mAttaching the kernel driver to card (device_index = %d)...\033[0m" % (device_index)
			card.attach_kernel_driver(0)
			if card.is_kernel_driver_active(0):
				print "\033[33mDone (device_index = %d).\033[0m" % device_index
			
			card_word_id = self.find_card_word_id(device_index)

			#open the audio card
			print "\033[36mOpening card \"%s\" (device_index = %d)...\033[0m" % (card_word_id, device_index)
			######### ESTA LINEA FALLA :( #############
			dev = alsaaudio.PCM(card="hw:CARD=%s" % card_word_id)

			print "\033[36mDone (device_index = %d).\033[0m" % device_index
			
			# we hard code the values because of our sound card capabilities,
			# audio files to be played have to match these.
			dev.setchannels(2) # hard-coded 2 channels (stereo).
			dev.setrate(48000)  # hard-coded sample rate 48000 Hz.
			dev.setformat(alsaaudio.PCM_FORMAT_S16_LE) # sample encoding: 16-bit Signed Integer PCM
			dev.setperiodsize(320)
			
			# play the wav file
			f = wave.open(filename + ".wav" , 'rb')
			
			data = f.readframes(320)
			while data:
				dev.write(data)
				data = f.readframes(320)

			# close the wav file
			f.close()

			# close the audio card
			dev.close()
		except Exception as e:
			print "Exception: %s" % str(e)
			pass

		# remove the played wav file
		os.remove("%s.wav" % filename)

		# release the semaphore
		self.semaphore.release()

		# fire 'finished' event
		values = {"id": str(device_index)}
		self.finished(values)



	def convert_intl_characters(self, text):
		# lower case
		text = text.replace("á", "'a")
		text = text.replace("é", "'e")
		text = text.replace("í", "'i")
		text = text.replace("ó", "'o")
		text = text.replace("ú", "'u")
		text = text.replace("ü", "''u")

		text = text.replace("ñ", "~n")

		# upper case
		text = text.replace("Á", "'A")
		text = text.replace("É", "'E")
		text = text.replace("Í", "'I")
		text = text.replace("Ó", "'O")
		text = text.replace("Ú", "'U")
		text = text.replace("Ü", "''U")

		text = text.replace("Ñ", "~N")

		return text
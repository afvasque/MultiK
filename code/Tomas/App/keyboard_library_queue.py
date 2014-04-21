# coding=utf-8

import sys
import event
import time

import time
import logging

# Evdev library: http://python-evdev.readthedocs.org/en/latest/tutorial.html
from evdev import InputDevice, categorize, ecodes

from select import select
from threading import Thread
from asyncore import file_dispatcher, loop
import string

import re
from subprocess import check_output


# Avoids while True for reading input
class InputDeviceDispatcher(file_dispatcher):
	
	diaeresis = False
	acute = False
	is_leftshift = False

	keypress = event.Event('A key has been pressed')

	vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
	vowels_acute = ['á', 'é', 'í', 'ó', 'ú', 'Á', 'É', 'Í', 'Ó', 'Ú']
	vowels_diaeresis = ['ä', 'ë', 'ï', 'ö', 'ü', 'Ä', 'Ë', 'Ï', 'Ö', 'Ü']

	def __init__(self, device):
		self.device = device
		file_dispatcher.__init__(self, device)

	def recv(self, ign=None):
		return self.device.read()

	def handle_read(self):		
		
		time_pressed = time.time()

		for event in self.recv():
			if event.value == 1:
				path = self.device.fn
				
				# Deletes /dev/input/event before ID
				device_id = path[(path.find("event")+5):]	
				
				keycode = ecodes.KEY[event.code]
				result = self.get_key_to_screen(keycode)
				
				if "KEY_" in result:
					result = self.get_punctuation_marks(event.code)
				
				if result != "":
					print([device_id,result])
					values = {"id": device_id, "char": result, "time_pressed": time_pressed}
					logging.info("[%f: [%d, %s, '%s'] ], " % (time_pressed, int(device_id), 'KEYPRESS', result))
					self.keypress(values)

	# Receives eventcode instead of keycode to avoid mapping mess. Eventcode is the same
	# no matter the active keyboard layout
	def get_punctuation_marks(self, eventcode):
		if eventcode == 12:
			if self.is_leftshift:
				self.is_leftshift = False
				return "?"
		elif eventcode == 13:
			if self.is_leftshift:
				self.is_leftshift = False
				return "¿"
			else:
				return "¡"
		elif eventcode == 14:
			return 'Back'
		elif eventcode == 28:
			return 'Enter'
		elif eventcode == 103:
			return '-^'
		elif eventcode == 108:
			return '-v'
		elif eventcode == 105:
			return '<-'
		elif eventcode == 106:
			return '->'
		elif eventcode == 127:
			return 'Pow'
		elif eventcode == 39:
			if self.is_leftshift:
				self.is_leftshift = False
				return 'Ñ'
			else:
				return 'ñ'
		else:
			return eventcode
			

	def get_key_to_screen(self, keycode):

		# Deletes KEY_
		key = keycode[keycode.find("KEY_")+4:] 
		
		# If is a letter
		if key in string.ascii_letters:

			if not self.is_leftshift:
				key = key.lower()

			if key in self.vowels:
				vowel_pos = self.vowels.index(key)
				if self.acute:
					return self.vowels_acute[vowel_pos]
				elif self.diaeresis:
					return self.vowels_diaeresis[vowel_pos]

			self.is_leftshift = False
			self.acute = False

			return key

		# If key is a number
		elif key in string.digits:
			if key == "1" and self.is_leftshift:
				self.is_leftshift = False
				return "!"
			return key

		# Uppercase
		elif keycode == "KEY_LEFTSHIFT":
			self.is_leftshift = True
			return ''
		# Acute
		elif keycode == "KEY_APOSTROPHE":
			# Diaeresis
			if self.is_leftshift:
				self.acute = False
				self.is_leftshift = False
				self.diaeresis = True
			else:
				self.acute = True
			return ''

		elif keycode == "KEY_DOT":
			if self.is_leftshift:
				self.is_leftshift = False
				return ':'
			else:
				return '.'
		elif keycode == "KEY_COMMA":
			if self.is_leftshift:
				self.is_leftshift = False
				return ';'
			else:
				return ','
		else:
			# Cannot handle this
			return keycode



class KeyboardLibrary:
	
	logging.basicConfig(filename='multik.log',level=logging.INFO)

	total_keyboards = 0

	keypress = event.Event('A key has been pressed')

	keyboard_paths = []

	keyboard_local_global_id = {}

	def __init__(self):
		# Search eventXX that matches connected keyboards
		output = "grep -E 'Handlers|EV=' /proc/bus/input/devices | grep -B1 'EV=120013'"
		output_result = check_output(output, shell=True) # shell=True allows pipe usage
		keyboard_events = re.findall(r'event[0-9]+', output_result, re.MULTILINE) # using regex select 'eventXX'

		# Standard keyboard path
		INPUT_EVENT_PATH = "/dev/input/"

		# Create keyboard path

		for counter, ke in enumerate(keyboard_events):
			self.keyboard_paths.append(INPUT_EVENT_PATH + ke)
			self.keyboard_local_global_id[ke[ke.find("event")+5:]] = counter

		# Eliminamos teclado del sistema

		

		self.total_keyboards = len(self.keyboard_paths)-1
	
	def run(self):

		for i in self.keyboard_paths:
			# Automagically added to asyncore.loop map when creating this file_dispatcher
			InputDeviceDispatcher(InputDevice(i)).keypress += self.Keyboard_Event

		# Using asyncore
		loop()

	def Keyboard_Event(self,sender,eargs):
		values = {"id": self.keyboard_local_global_id[eargs['id']], "char": eargs['char'], "time_pressed": eargs['time_pressed']}
		self.keypress(values)
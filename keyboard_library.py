# coding=utf-8

import re
from subprocess import check_output

# Evdev library: http://python-evdev.readthedocs.org/en/latest/tutorial.html
from evdev import InputDevice, categorize, ecodes

from select import select
from threading import Thread
from asyncore import file_dispatcher, loop
import string

# Avoids while True for reading input
class InputDeviceDispatcher(file_dispatcher):
	
	diaeresis = False
	acute = False
	is_leftshift = False

	vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
	vowels_acute = ['á', 'é', 'í', 'ó', 'ú', 'Á', 'É', 'Í', 'Ó', 'Ú']
	vowels_diaeresis = ['ä', 'ë', 'ï', 'ö', 'ü', 'Ä', 'Ë', 'Ï', 'Ö', 'Ü']

	def __init__(self, device):
		self.device = device
		file_dispatcher.__init__(self, device)

	def recv(self, ign=None):
		return self.device.read()

	def handle_read(self):
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
					return([device_id,result])

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
		else:
			return ''

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



# Search eventXX that matches connected keyboards
output = "grep -E 'Handlers|EV=' /proc/bus/input/devices | grep -B1 'EV=120013'"
output_result = check_output(output, shell=True) # shell=True allows pipe usage
keyboard_events = re.findall(r'event[0-9]+', output_result, re.MULTILINE) # using regex select 'eventXX'

# Standard keyboard path
INPUT_EVENT_PATH = "/dev/input/"

# Create keyboard path
keyboard_paths = []

for ke in keyboard_events:
	keyboard_paths.append(INPUT_EVENT_PATH + ke)

for i in keyboard_paths:
	# Automagically added to asyncore.loop map when creating this file_dispatcher
	InputDeviceDispatcher(InputDevice(i))

# Using asyncore
loop()

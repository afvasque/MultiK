# coding=utf-8

import sys
import event
import time

import time
import logging

import InputDeviceDispatcher

import re
from subprocess import check_output



class KeyboardLibrary:
	
	logging.basicConfig(filename='multik.log',level=logging.INFO)

	total_keyboards = 0

	def __init__(self):
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

		self.total_keyboards = keyboard_paths.count()

	
	def run(self):
		for i in keyboard_paths:
			# Automagically added to asyncore.loop map when creating this file_dispatcher
			InputDeviceDispatcher(InputDevice(i))

			# Using asyncore
			loop()
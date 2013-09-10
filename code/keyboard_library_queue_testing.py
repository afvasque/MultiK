# coding=utf-8
import keyboard_library_queue
import sys


def print_event(sender, earg):
	print str(earg)
	

lib = keyboard_library_queue.KeyboardLibrary()
lib.keypress += print_event
lib.run([[0x0e8f,0x0022],[0x0e6a,0x6001]])


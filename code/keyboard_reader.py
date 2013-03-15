# coding=utf-8

import usb.core
import usb.util

# keycode mapping (for a latin american keyboard layout)
key_pages = [
'', '', '', '',
'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
'1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'Enter', '^]', '^H',
'^I', ' ', "'", '¡', '`', '+', 'ç', '>', 'ñ', '´', '°', ',', '.',
'-', 'CapsLock', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10', 'F11', 'F12',
'PS', 'SL', 'Pause', 'Ins', 'Home', 'PU', '^D', 'End', 'PD', '->', '<-', '-v', '-^', 'NL',
'KP/', 'KP*', 'KP-', 'KP+', 'KPE', 'KP1', 'KP2', 'KP3', 'KP4', 'KP5', 'KP6', 'KP7', 'KP8',
'KP9', 'KP0', '\\', '<', 'Pow', 'KP=', 'F13', 'F14' ]

key_pages_shift = [
'', '', '', '',
'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
'!', '"', '·', '$', '%', '&', '/', '(', ')', '=', 'Enter', '^]', '^H',
'^I', ' ', '?', '¿', '^', '*', 'Ç', '<', 'Ñ', '¨', 'ª', ';', ':',
'_', 'CapsLock', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10', 'F11', 'F12',
'PS', 'SL', 'Pause', 'Ins', 'Home', 'PU', '^D', 'End', 'PD', '->', '<-', '-v', '-^', 'NL',
'KP/', 'KP*', 'KP-', 'KP+', 'KPE', 'KP1', 'KP2', 'KP3', 'KP4', 'KP5', 'KP6', 'KP7', 'KP8',
'KP9', 'KP0', '|', '>', 'Pow', 'KP=', 'F13', 'F14' ]

def map_character(c):
	return key_pages[c]

def chunks(l, n):
	""" Yield successive n-sized chunks from l.
	"""
	for i in xrange(0, len(l), n):
		yield l[i:i+n]




class KeyboardReader:
	def __init__(self, vendor_id, product_id, keyboard_id, queue):
		# Save the queue as an attribute.
		self.queue = queue




		# Find all keyboards with the given vendor and product ids.
		keyboards = usb.core.find(find_all=True, idVendor=vendor_id, idProduct=product_id)

		# Get the one with the given index.
		self.keyboard = keyboards[keyboard_id]

		# Save the keyboard_id
		self.keyboard_id = keyboard_id

		# Remove the elements from the list (we don't want any other keyboard)
		del keyboards[:]




		# Detach kernel driver from the keyboard.
		self.detach_keyboard()

		# Set configuration.
		self.set_configuration()

		# Read the input.
		self.read_keyboard_input()






	def detach_keyboard(self):
		if self.keyboard.is_kernel_driver_active(0):
			try:
				self.keyboard.detach_kernel_driver(0)
			except usb.core.USBError as e:
				sys.exit("Could not detach kernel driver: %s" % str(e))




	def set_configuration(self):
		try:
			self.keyboard.set_configuration() # This gives us an error (Errno 16: Resource busy), we don't know why ...
			self.keyboard.reset()
		except usb.core.USBError as e:
			# # ... but we can ignore it and we get no problems.
			# print "Error on setting configuration: " + str(e) + ". Continuing anyway."
			pass

		# Define the endpoint.
		self.keyboard._endpoint = self.keyboard[0][(0,0)][0]




	def read_keyboard_input(self):
		while True:
			try:
				kb = self.keyboard
				data = kb._endpoint.read(kb._endpoint.wMaxPacketSize, 10) # timeout is the last argument

				# map the input to a character
				map_keys = lambda c: key_pages_shift[c[1]] if c[0] is 2 else key_pages[c[1]]
				data2 = "".join(map(map_keys, [(d[0], d[2]) for d in chunks(data, 8)]))

				# if input detected
				if data2:
					# define the event arguments
					values = {"id": str(self.keyboard_id), "char": data2}
					try:
						# put these values on the queue
						self.queue.put_nowait(values)
					except Queue.Full:
						print "Queue full. Lost values: %s", values
						pass

			except usb.core.USBError as e:
				pass
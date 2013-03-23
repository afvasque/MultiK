# coding=utf-8

import sys
import usb.core
import usb.util
import multiprocessing
import Queue
import keyboard_reader
import event



class KeyboardLibrary:

	keyboard_proc_array = []
	keypress = event.Event('A key has been pressed')


	def detect_all_keyboards(self, vendor_id, product_id):
		# find our keyboards
		print 'Detecting keyboards with vendor_id = ' + str(vendor_id) + ' and product_id = ' + str(product_id) + '...'
		keyboards = usb.core.find(find_all=True, idVendor=vendor_id, idProduct=product_id)

		print '\033[94m' + str(len(keyboards)) + ' keyboards of the specified type detected!' + '\033[0m'

		self.total_keyboards = len(keyboards)

		if self.total_keyboards == 0:
			print '\033[91m' + 'Make sure the keyboards are connected, or check that the vendor_id and product_id variables are correct.' + '\033[0m'
			raw_input('Press [Enter] to exit.')
			sys.exit()


	def get_total_keyboards(self):
		return self.total_keyboards

	def __init__(self):
		self.total_keyboards=0
		return

	
	def run(self, vendor_id, product_id):
		# Detect the keyboards
		# (id values can be found using 'lsusb --vv' command in ubuntu 12.04 and other linux versions)
		#self.detect_all_keyboards(vendor_id, product_id)

		# Create a queue (FIFO) for safely exchanging information
		queue = multiprocessing.Queue(False)

		# Create processes
		print "Starting %i processes..." % self.total_keyboards
		for i in range(self.total_keyboards):

			# The keyboard needs to be detected again.
			p = multiprocessing.Process(target=keyboard_reader.KeyboardReader, args=(vendor_id,product_id,i,queue))
			
			# Save the reference to the process just created.
			self.keyboard_proc_array.append(p)

			# Start it.
			p.start()
			print "%s" % str(p)


		# Read the queue forever.
		while(True):
			try:
				# Get the values for the event.
				val = queue.get()
				# Fire the event
				self.keypress(val) # Piuuu!
			except Queue.Empty as e:
				pass

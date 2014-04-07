# coding=utf-8

import sys
import usb.core
import usb.util
import multiprocessing
import Queue
import keyboard_reader
import event
import time



class KeyboardLibrary:

	keyboard_proc_array = []
	vendor_product_ids = []
	total_keyboards_by_vendor_product_ids = []
	keypress = event.Event('A key has been pressed')

	def detect_all_keyboards(self, vendor_product_ids):
		for i in range(len(vendor_product_ids)):
			vendor_id = vendor_product_ids[i][0]
			product_id = vendor_product_ids[i][1]

			# find our keyboards
			print 'Detecting keyboards with vendor_id = ' + str(vendor_id) + ' and product_id = ' + str(product_id) + '...'
			keyboards = usb.core.find(find_all=True, idVendor=vendor_id, idProduct=product_id)

			print '\033[94m' + str(len(keyboards)) + ' keyboards of the specified type detected!' + '\033[0m'

			self.total_keyboards_by_vendor_product_ids.append(len(keyboards))
			self.total_keyboards = self.total_keyboards + len(keyboards)

		if self.total_keyboards == 0:
			print '\033[91m' + 'Make sure the keyboards are connected, or check that the vendor_id and product_id variables are correct.' + '\033[0m'
			raw_input('Press [Enter] to exit.')
			sys.exit()


	def get_total_keyboards(self):
		return self.total_keyboards

	def __init__(self):
		self.total_keyboards = 0
		return

	
	def run(self, vendor_product_ids):
		self.vendor_product_ids = vendor_product_ids



		# Detect the keyboards
		# (id values can be found using 'lsusb --vv' command in ubuntu 12.04 and other linux versions)
		#self.detect_all_keyboards(self.vendor_product_ids)

		# Create a queue (FIFO) for safely exchanging information
		queue = multiprocessing.Queue(False)

		# Create processes
		print "Starting %i processes..." % self.total_keyboards
		for global_id in range(self.total_keyboards):
			local_id = -1
			vendor_id = -1
			product_id = -1

			cumulative = 0
			cumulative_prev = 0

			############DEBUG
			# print '---------:'
			# str1 = ''.join(str(e) + ',' for e in self.total_keyboards_by_vendor_product_ids)
			# print str1
			# print ':---------'

			for vp, val in enumerate(self.total_keyboards_by_vendor_product_ids):
				cumulative_prev = cumulative
				cumulative = cumulative + val
				if (global_id < cumulative):
					local_id = global_id - cumulative_prev
					vendor_id = self.vendor_product_ids[vp][0]
					product_id = self.vendor_product_ids[vp][1]
					break

			############DEBUG
			# print '++++++++:'
			# print 'local_id = %i' % local_id
			# print 'global_id = %i' % global_id
			# print ':++++++++'

			# The keyboard needs to be detected again.
			p = multiprocessing.Process(target=keyboard_reader.KeyboardReader, args=(vendor_id,product_id,global_id,local_id,queue))
			
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

import usb.core
import usb.util
import itertools
import os

class AudioLibrary:

	tarjetas1 = []
	tarjetas2 = []
	tarjetas3 = []
	tarjetas = []

	#Obtener VendorID y ProductID de una forma inteligente
	#Hardcodded por ahora

	tarjetas1 = usb.core.find(find_all = True, idVendor=0x0d8c)
	tarjetas2 = usb.core.find(find_all = True, idVendor=0x0c76)
	tarjetas3 = usb.core.find(find_all = True, idVendor=0x1130)

	def __init__(self):
		for counter, t in enumerate(itertools.chain(self.tarjetas1, self.tarjetas2, self.tarjetas3)):
			print "Tarjeta %s" % counter
			print str(t.bus)
			print str(t.address)
			self.tarjetas.append(t)
			if t.is_kernel_driver_active(0):
				t.detach_kernel_driver(0)
		os.system("aplay -l")

	#Llamar t.attach_kernel_driver(0) para retomar control

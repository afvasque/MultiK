import usb.core
import usb.util

class AudioLibrary:

	tarjetas = []

	#Obtener VendorID y ProductID de una forma inteligente
	#Hardcodded por ahora

	tarjetas.append(usb.core.find(idVendor=0x0d8c))
	tarjetas.append(usb.core.find(idVendor=0x0c76))
	tarjetas.append(usb.core.find(idVendor=0x1130))

	def __init__(self):
		for t in tarjetas:
			t.detach_kernel_driver(0)

	#Llamar t.attach_kernel_driver(0) para retomar control

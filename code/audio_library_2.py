import usb.core
import usb.util

class AudioLibrary:



	"""
	>>> import usb.core
	>>> import usb.util
	>>> tarjetas = []
	>>> tarjetas.append(usb.core.find(idVendor=0x0d8c))
	>>> tarjetas.append(usb.core.find(idVendor=0x0c76))
	>>> tarjetas.append(usb.core.find(idVendor=0x1130))
	>>> len(tarjetas)
	3
	>>> for t in tarjetas:
	...     t.detach_kernel_driver(0)
	... 
	>>> 
	>>> for t in tarjetas:
	...     t.attach_kernel_driver(0)
	"""
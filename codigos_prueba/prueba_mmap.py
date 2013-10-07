import alsaaudio
import wave
import mmap

class MMap_test:

	card = 'default'
	device = alsaaudio.PCM(card=card)
	
	f1 = open('bell.wav', 'rb')

	mmap = mmap.mmap(f1.fileno(),0, access=mmap.ACCESS_READ)
	
    # Set attributes
	device.setchannels(2)
	device.setrate(44100)

	device.setformat(alsaaudio.PCM_FORMAT_S16_LE)
	device.setperiodsize(320)

	data = mmap.read(320)
	while data:
	    # Read data from stdin
	    device.write(data)
	    data = mmap.read(320)

MMap_test()
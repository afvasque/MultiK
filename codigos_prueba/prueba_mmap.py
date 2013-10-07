import alsaaudio
import wave
import mmap

class MMap_test:

	card = 'default'
	device = alsaaudio.PCM(card=card)
	
	f = wave.open('bell.wav', 'rb')
	f1 = open('bell.wav', 'rb')

	mmap = mmap.mmap(f1.fileno(),0, access=mmap.ACCESS_READ)
	
	print '%d channels, %d sampling rate\n' % (f.getnchannels(), f.getframerate())
    # Set attributes
	device.setchannels(f.getnchannels())
	device.setrate(f.getframerate())

	# 8bit is unsigned in wav files
	if f.getsampwidth() == 1:
	    device.setformat(alsaaudio.PCM_FORMAT_U8)
	# Otherwise we assume signed data, little endian
	elif f.getsampwidth() == 2:
	    device.setformat(alsaaudio.PCM_FORMAT_S16_LE)
	elif f.getsampwidth() == 3:
	    device.setformat(alsaaudio.PCM_FORMAT_S24_LE)
	elif f.getsampwidth() == 4:
	    device.setformat(alsaaudio.PCM_FORMAT_S32_LE)
	else:
	    raise ValueError('Unsupported format')

	device.setperiodsize(320)

	data = mmap.read(320)
	while data:
	    # Read data from stdin
	    device.write(data)
	    data = mmap.read(320)

MMap_test()
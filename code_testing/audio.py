import sys
import pyaudio
import wave


CHUNK = 1024
RATE = 48000 # el que soportan las tarjetas


p = pyaudio.PyAudio()

count = p.get_device_count()

devices = []

for i in range(count):
    devices.append(p.get_device_info_by_index(i))

for i, dev in enumerate(devices):
    print "%d - %s" % (i, dev['name'])

output_device_index = int(raw_input('Choose dst: '))

wf = wave.open('/home/esteban/pyprojects/MultiK/audio_files/bell-ringing-04.wav', 'rb')

dst = p.open(format = p.get_format_from_width(wf.getsampwidth()),
                channels = wf.getnchannels(),
                #rate = wf.getframerate(),
                rate = RATE,
                output = True,
                output_device_index = output_device_index)




data = wf.readframes(CHUNK)

while data != '':
   dst.write(data, CHUNK)
   data = wf.readframes(CHUNK)

dst.stop_stream()
dst.close()



p.terminate()    
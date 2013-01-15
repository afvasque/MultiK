import sys
import os
import pyaudio
import wave


CHUNK = 1024

p = pyaudio.PyAudio()

count = p.get_device_count()

devices = []

for i in range(count):
    devices.append(p.get_device_info_by_index(i))

for i, dev in enumerate(devices):
    print "%d - %s" % (i, dev['name'])

output_device_index = int(raw_input('Choose dst: '))

audio_file_name = 'bell-ringing-04.wav' # importante: archivo de audio debe ser de 48000 Hz
audio_file_path = os.path.join( os.path.dirname(os.path.abspath(os.path.dirname(__file__))), 'audio_files', audio_file_name )
wf = wave.open(audio_file_path, 'rb')

dst = p.open(format = p.get_format_from_width(wf.getsampwidth()),
                channels = wf.getnchannels(),
                rate = wf.getframerate(),
                output = True,
                output_device_index = output_device_index)




data = wf.readframes(CHUNK)

while data != '':
   dst.write(data, CHUNK)
   data = wf.readframes(CHUNK)

dst.stop_stream()
dst.close()



p.terminate()    
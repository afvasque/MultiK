import sys
import os
import pyaudio
import wave

class AudioDevices:
	def __init__(self):
		# Number of frames to read per iteration
		self.CHUNK = 1024

	def play_wav_through(self, output_device_index, audio_file_path):
		p = pyaudio.PyAudio()
		chunk = self.CHUNK

		print 'Playing sound through device with device index ' + str(output_device_index) + "..."

		# Open the wave file
		wf = wave.open(audio_file_path, 'rb')

		# Get a pyaudio.Stream object
		dst = p.open(
				format = p.get_format_from_width(wf.getsampwidth()),
                channels = wf.getnchannels(),
                rate = wf.getframerate(),
                output = True,
                output_device_index = output_device_index)

		# Read and output
		data = wf.readframes(chunk)
		while data != '':
		   dst.write(data, chunk)
		   data = wf.readframes(chunk)

		# Close the wave file
		wf.close()
		# Stop and close the pyaudio.Stream
		dst.stop_stream()
		dst.close()

		# Terminate PortAudio. Be sure to call this method for every instance of this object to release PortAudio resources.
		p.terminate()

		print 'Done.'

	def play_wav_through_all(self, audio_file_path, device_index_array = None, simultaneous = False):
		p = pyaudio.PyAudio()
		chunk = self.CHUNK

		if device_index_array is None:
			count = p.get_device_count()
			device_index_array = range(count)
		else:
			count = len(device_index_array)

		# Open the wave file
		wf = wave.open(audio_file_path, 'rb')

		if not simultaneous:
			for i, output_device_index in enumerate(device_index_array):
				# Rewind the file pointer to the beginning of the audio stream
				wf.rewind()

				print 'Playing sound through device with device index ' + str(output_device_index) + " (device " + str(i) +" of " + str(count - 1) + ")... "
		
				# Get a pyaudio.Stream object
				dst = p.open(
						format = p.get_format_from_width(wf.getsampwidth()),
		                channels = wf.getnchannels(),
		                rate = wf.getframerate(),
		                output = True,
		                output_device_index = output_device_index)

				# Read and output
				data = wf.readframes(chunk)
				while data != '':
				   dst.write(data, chunk)
				   data = wf.readframes(chunk)

				# Stop and close the pyaudio.Stream
				dst.stop_stream()
				dst.close()

				print 'Done.'

		else:
			# Rewind the file pointer to the beginning of the audio stream
			wf.rewind()

			print 'Playing sound through devices with device indexes: ' + str(device_index_array) + "... "
			
			# Array for storing all the pyaudio.Stream objects through which we will be outputting audio
			destinations = []

			for output_device_index in device_index_array:
				# Get a pyaudio.Stream object
				dst = p.open(
						format = p.get_format_from_width(wf.getsampwidth()),
		                channels = wf.getnchannels(),
		                rate = wf.getframerate(),
		                output = True,
		                output_device_index = output_device_index)
				# Add it to the array
				destinations.append(dst)


			# Read and output
			data = wf.readframes(chunk)
			while data != '':
				# Write to every output stream
				for dst in destinations:
					dst.write(data, chunk)
				data = wf.readframes(chunk)

			for dst in destinations:
				# Stop and close the pyaudio.Stream
				dst.stop_stream()
				dst.close()

			print 'Done.'

		# Close the wave file
		wf.close()
		# Terminate PortAudio. Be sure to call this method for every instance of this object to release PortAudio resources.
		p.terminate()
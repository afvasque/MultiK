
import os
import audio_devices

# test wav file
# important: audio file must be 48000 Hz for our sound cards
audio_file_name = 'bell-ringing-04.wav'

# get the path to the file (relative to this file)
audio_file_path = os.path.join( os.path.dirname(os.path.abspath(os.path.dirname(__file__))), 'audio_files', audio_file_name )

# play the test sound on every device
audio_devices.AudioDevices().play_wav_through_all(audio_file_path, range(4, 18))


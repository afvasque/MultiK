# coding=utf-8

import sys
import wave
import os
import event
import time
import datetime
import alsaaudio

class AudioLibrary:
    card_array = []
    finished = event.Event('Audio has finished playing.')

    def __init__(self, total_internal_cards):
        total_cards = len(alsaaudio.cards())
        print "Detected " + str(total_cards) + " sound cards in total."
        total_external_cards = total_cards - total_internal_cards
        print "Assuming " + str(total_external_cards) + " external sound cards in total."

        for card in range(total_internal_cards,total_external_cards+1):
            dev = alsaaudio.PCM( card='hw:'+str(card) )
            
            # hard code the values because of the sound card capabilities,
            # audio files to be played have to match these values.
            dev.setchannels(2) # hard-coded 2 channels (stereo).
            dev.setrate(48000)  # hard-coded sample rate 48000 Hz.
            dev.setformat(alsaaudio.PCM_FORMAT_S16_LE)
            dev.setperiodsize(320)

            self.card_array.append(dev)

    def play(self, device_index, text_to_speech):
        timestamp = str(time.mktime(datetime.datetime.now().timetuple()))
        filename = str(device_index) + "_" + timestamp
        filename_final = filename+ "_final"

        # create the wav file
        # text2wave default voice can be changed in /etc/festival.scm. Add at the end, e.g.: (set! voice_default 'voice_JuntaDeAndalucia_es_sf_diphone)
        os.system("echo \""+ text_to_speech +"\" | text2wave -F 48000 -o " +filename+ ".wav")
        # convert to stereo, thus doubling the bitrate
        os.system("sox "+ filename +".wav -c 2 "+ filename_final +".wav")

        # play the wav file
        f = wave.open(filename_final + ".wav" , 'rb')
        data = f.readframes(320)
        while data:
            self.card_array[device_index].write(data)
            data = f.readframes(320)

        f.close()

        # fire finished event
        values = {"id": str(device_index)}
        self.finished(values)
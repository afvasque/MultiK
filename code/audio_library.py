# coding=utf-8

import sys
import wave
import os
import event
import time
import datetime
import alsaaudio
import subprocess

class AudioLibrary:
    card_array = []
    finished = event.Event('Audio has finished playing.')

    def __init__(self, total_internal_cards):
        cards = alsaaudio.cards() # running as sudo helps making it faster

        total_cards = len(cards)
        print "Detected " + str(total_cards) + " sound cards in total."
        total_external_cards = total_cards - total_internal_cards
        print "Assuming " + str(total_external_cards) + " external sound cards in total."

        # 
        for k in self.get_card_names()[total_internal_cards:]:
            print k
            dev = alsaaudio.PCM(card=k)
            
            # hard code the values because of the sound card capabilities,
            # audio files to be played have to match these values.
            dev.setchannels(2) # hard-coded 2 channels (stereo).
            dev.setrate(48000)  # hard-coded sample rate 48000 Hz.
            dev.setformat(alsaaudio.PCM_FORMAT_S16_LE)
            dev.setperiodsize(320)

            self.card_array.append(dev)

    def get_total_cards(self):
        return len(self.card_array)

    def play(self, device_index, text_to_speech):
        timestamp = str(time.mktime(datetime.datetime.now().timetuple()))
        filename = str(device_index) + "_" + timestamp

        # create the wav file
        # text2wave default voice can be changed in /etc/festival.scm. Add at the end, e.g.: (set! voice_default 'voice_JuntaDeAndalucia_es_sf_diphone)
        os.system("echo \""+ text_to_speech +"\" | text2wave -F 48000 -o " +filename+ ".tmp")
        # convert to stereo, thus doubling the bitrate
        os.system("sox "+ filename +".tmp -c 2 "+ filename +".wav")
        # remove the temporary file
        os.remove(filename + ".tmp")

        # play the wav file
        f = wave.open(filename + ".wav" , 'rb')
        data = f.readframes(320)
        while data:
            self.card_array[device_index].write(data)
            data = f.readframes(320)

        f.close()

        # fire finished event
        values = {"id": str(device_index)}
        self.finished(values)

    def get_card_names(self):
        command = "cat /proc/asound/cards | grep \"]\" | cut -d \"[\" -f 2 | cut -d \" \" -f 1"

        output = subprocess.check_output(command, shell=True) #Popen doesnt work :(

        l = output.split('\n')
        l.pop() # delete the last (empty) element

        return l


    def convert_intl_characters(self, text):
        # lower case
        text = text.replace("á", "'a")
        text = text.replace("é", "'e")
        text = text.replace("í", "'i")
        text = text.replace("ó", "'o")
        text = text.replace("ú", "'u")
        text = text.replace("ü", "''u")

        text = text.replace("ñ", "~n")

        # upper case
        text = text.replace("Á", "'A")
        text = text.replace("É", "'E")
        text = text.replace("Í", "'I")
        text = text.replace("Ó", "'O")
        text = text.replace("Ú", "'U")
        text = text.replace("Ü", "''U")

        text = text.replace("Ñ", "~N")

        return text


# coding=utf-8

import sys
import wave
import os
import event
import time
import datetime
import alsaaudio
import subprocess

import multiprocessing


class AudioLibrary:
    card_name_array = [] # array containing the names of the usb sound cards
    finished = event.Event('Audio has finished playing.')
    reproduciendo={}

    # semaphore with limit of 7 because of the hub bandwidth limit of 12Mbit/s
    # since our bitrate is 1.54Mbit/s,
    # 12 / 1.54 = 7.7922 gives us that the limit is 7
    semaphore = multiprocessing.Semaphore(7)

    def __init__(self):
        all_cards = self.get_card_names()
        usb_cards = self.get_usb_card_names()
        
        reload(sys)
        sys.setdefaultencoding('utf-8')

        total_cards = len(all_cards)
        print '\033[94m' + "Detected " + str(total_cards) + " sound cards in total." + '\033[0m'
        total_usb_cards = len(usb_cards)
        print "Assuming " + str(total_usb_cards) + " USB sound cards in total."

        self.card_name_array = usb_cards



    def get_total_usb_cards(self):
        return len(self.card_name_array)


    def play(self, device_index, text_to_speech_queue):
        timestamp = time.mktime(datetime.datetime.now().timetuple())
        filename = "%s_%d" % (device_index, timestamp)

        while True:
            text_to_speech = text_to_speech_queue.get()
            # create the wav file
            # text2wave default voice can be changed in /etc/festival.scm. Add at the end, e.g.: (set! voice_default 'voice_JuntaDeAndalucia_es_sf_diphone)
            os.system("echo \"%s\" | text2wave -F 48000 -o %s.tmp" % (self.convert_intl_characters(text_to_speech), filename))
            # convert to stereo, thus doubling the bitrate
            os.system("sox %s.tmp -c 2 %s.wav" % (filename, filename))
            # remove the temporary file
            os.remove("%s.tmp" % filename)


            self.semaphore.acquire()

            try:
                #open the audio card
                print "Opening card \"%s\" (device_index = %d)..." % (self.card_name_array[device_index], device_index)
                dev = alsaaudio.PCM(card="hw:CARD=" + self.card_name_array[device_index])
                
                # we hard code the values because of our sound card capabilities,
                # audio files to be played have to match these.
                dev.setchannels(2) # hard-coded 2 channels (stereo).
                dev.setrate(48000)  # hard-coded sample rate 48000 Hz.
                dev.setformat(alsaaudio.PCM_FORMAT_S16_LE) # sample encoding: 16-bit Signed Integer PCM
                dev.setperiodsize(320)
                
                # play the wav file
                f = wave.open(filename + ".wav" , 'rb')
                data = f.readframes(320)
                while data:
                    dev.write(data)
                    data = f.readframes(320)

                # close the wav file
                f.close()

                # close the audio card
                dev.close()

                # remove the played wav file
                os.remove(filename + ".wav")
            except Exception as e:
                print "Exception in card \"%s\" (device_index = %d): %s" % (self.card_name_array[device_index], device_index, str(e))
                pass

            self.semaphore.release()

            # fire 'finished' event
            values = {"id": str(device_index)}
            self.finished(values)

    def get_card_names(self):
        command = "cat /proc/asound/cards | grep \"]\" | cut -d \"[\" -f 2 | cut -d \" \" -f 1"

        output = subprocess.check_output(command, shell=True) #Popen doesnt work :(

        l = output.split('\n')
        l.pop() # delete the last (empty) element

        return l

    def get_usb_card_names(self):
        command = "cat /proc/asound/cards | grep \"USB-Audio\" | cut -d \"[\" -f 2 | cut -d \" \" -f 1"

        output = subprocess.check_output(command, shell=True) #Popen doesnt work :(

        l = output.split('\n')
        l.pop() # delete the last (empty) element

        return l

    def convert_intl_characters(self, text):
        #text = unicode(text,"utf8")
        # lower case
        text = text.replace(u"á", "'a")
        text = text.replace(u"é", "'e")
        text = text.replace(u"í", "'i")
        text = text.replace(u"ó", "'o")
        text = text.replace(u"ú", "'u")
        text = text.replace(u"ü", "''u")

        text = text.replace(u"ñ", "~n")

        # upper case
        text = text.replace(u"Á", "'A")
        text = text.replace(u"É", "'E")
        text = text.replace(u"Í", "'I")
        text = text.replace(u"Ó", "'O")
        text = text.replace(u"Ú", "'U")
        text = text.replace(u"Ü", "''U")

        text = text.replace(u"Ñ", "~N")

        return text
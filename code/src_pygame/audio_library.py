# coding=utf-8

import sys
import wave
import os
import event
import time
import alsaaudio
import subprocess
import multiprocessing
import sound_card
import logging
import mmap

logging.basicConfig(filename='multik.log',level=logging.INFO)




class AudioLibrary:
    card_array = [] # array containing the usb sound cards
    root_hubs_set = set('') # set containing the addresses of the root usb hubs
    semaphore = {}
    audio_mmap = {}

    all_q = []
    all_p = []

    finished = event.Event('Audio has finished playing.')




    def __init__(self):
        reload(sys)
        sys.setdefaultencoding('utf-8')

        for card_name in self.get_usb_card_names():
            card = sound_card.SoundCard(card_name)
            self.card_array.append(card)

        self.root_hubs_set = self.get_usb_root_hub_addrs()

        for hub in self.root_hubs_set:
            # semaphore with limit of 7 because of the hub bandwidth limit of 12Mbit/s
            # since our bitrate is 1.54Mbit/s,
            # 12 / 1.54 = 7.7922 gives us that the limit is 7
            self.semaphore[hub] = multiprocessing.Semaphore(7)

        print "\033[94mAssuming %d USB root hub(s) in total.\033[0m" % len(self.root_hubs_set)
        print "\033[94mAssuming %d USB sound card(s) in total.\033[0m" % len(self.card_array)

        # Create a process and a queue for every card
        for i in range(0,self.get_total_usb_cards()):
            # Create a queue
            text_to_speech_queue = multiprocessing.Queue()
            # Create a process
            p = multiprocessing.Process(target=self.read_queue, args=(i, text_to_speech_queue))
            # Set as daemon
            p.daemon = True
            # Append to the process array
            self.all_p.append(p)
            # Start it
            p.start()
            # Append the queue to the queue array
            self.all_q.append(text_to_speech_queue)




    def get_total_usb_cards(self):
        return len(self.card_array)



    def get_total_usb_root_hubs(self):
        return len(self.root_hubs_set)


    def get_usb_root_hub_addrs(self):
        hub_addrs = set('')

        for card in self.card_array:
            # Add the address to a set (with unique elements)
            hub_addrs.add(card.get_root_hub())
        
        return hub_addrs



    def play(self, id, text_to_speech):
        # Get the queue for the corresponding card
        queue = self.all_q[id]

        # Empty the queue
        while not queue.empty():
            queue.get()
        
        # Put the text_to_speech in the queue
        queue.put({
            'tts': text_to_speech
        })








    def read_queue(self, device_index, text_to_speech_queue):
        while True:
            # Get a queued text for turning into speech
            queued_item = text_to_speech_queue.get()
            text_to_speech = queued_item['tts']

            timestamp = time.time()
            filename = "%s_%f" % (device_index, timestamp)




            # check if tts is already generated
            if ( text_to_speech not in self.audio_mmap ):
                logging.info("[%f: [%d, %s, %s, %s] ], " % (time.time(), device_index, 'GENERATE_FILE_START', filename, text_to_speech))
                
                # generate the wav file
                self.generate_sound_file(text_to_speech, filename)

                # write audio file into memory
                filepath = "%s.wav" % (filename)

                # open the generated audio file
                f = open(filepath, "r+b")
                # memory-map the file, size 0 means whole file
                self.audio_mmap[text_to_speech] = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)

                logging.info("[%f: [%d, %s, %s, %s] ], " % (time.time(), device_index, 'GENERATE_FILE_COMPLETE', filename, text_to_speech))
            

            # mmap of the generated file
            file_mmap = self.audio_mmap[text_to_speech]

            # rewind the audio
            file_mmap.seek(0)

            semaphore_index = self.card_array[device_index].get_root_hub()

            logging.info("[%f: [%d, %s, %s, %s] ], " % (time.time(), device_index, 'SEMAPHORE_WAIT_START', filename, semaphore_index))
            self.semaphore[ semaphore_index ].acquire()
            logging.info("[%f: [%d, %s, %s, %s] ], " % (time.time(), device_index, 'SEMAPHORE_WAIT_COMPLETE', filename, semaphore_index))


            try:
                #open the audio card
                print "Opening card \"%s\" (device_index = %d)..." % (self.card_array[device_index].get_name(), device_index)
                dev = alsaaudio.PCM(card="hw:CARD=%s" % ( self.card_array[device_index].get_name() ))
                
                
                # play the wav file
                logging.info("[%f: [%d, %s, %s, %s] ], " % (time.time(), device_index, 'AUDIO_PLAY_START', filename, text_to_speech))


                # we hard code the values because of our sound card capabilities,
                # audio files to be played have to match these.
                dev.setchannels(2) # hard-coded 2 channels (stereo).
                dev.setrate(44100)  # hard-coded sample rate 48000 Hz.
                dev.setformat(alsaaudio.PCM_FORMAT_S16_LE) # sample encoding: 16-bit Signed Integer PCM
                dev.setperiodsize(320)

                data = file_mmap.read(320)
                while data:
                    dev.write(data)
                    data = file_mmap.read(320)
                

                logging.info("[%f: [%d, %s, %s, %s] ], " % (time.time(), device_index, 'AUDIO_PLAY_COMPLETE', filename, text_to_speech))


                # close the audio card
                dev.close()


            except alsaaudio.ALSAAudioError as e:
                print "Exception in card \"%s\" (device_index = %d): %s" % (self.card_array[device_index].get_name(), device_index, str(e))
                logging.exception("[%f: [%d, %s, %s, %s] ], " % (time.time(), device_index, 'AUDIO_PLAY_EXCEPTION', filename, text_to_speech))
                pass

            self.semaphore[ self.card_array[device_index].get_root_hub() ].release()

            # fire 'finished' event
            values = queued_item
            values['id'] = device_index
            self.finished(values)


    def generate_sound_file(self, text_to_speech, filename):
        # generate the wav file
        # text2wave default voice can be changed in /etc/festival.scm. Add at the end, e.g.: (set! voice_default 'voice_JuntaDeAndalucia_es_sf_diphone)
        os.system("echo \"%s\" | text2wave -F 48000 -o %s.tmp" % (self.convert_intl_characters(text_to_speech), filename))
        # convert to stereo, thus doubling the bitrate
        os.system("sox %s.tmp -c 2 %s.wav" % (filename, filename))
        # remove the temporary file
        os.remove("%s.tmp" % filename)


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
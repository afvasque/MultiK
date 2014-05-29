# coding=utf-8

import alsaaudio
import csv
from src_pygame.event import Event
import logging
import os
import mmap
import multiprocessing
import sound_card
import subprocess
import sys
import time
import wave

logging.basicConfig(filename='multik.log',level=logging.INFO)




class AudioLibrary:
    card_array = [] # array containing the usb sound cards
    root_hubs_set = set('') # set containing the addresses of the root usb hubs
    semaphore = {} # dictionary containing one semaphore for each root usb hub
    audio_mmap = {} # dictionary containing 'text_to_speech': corresponding_mmap

    all_q = [] # array containing all queues
    all_p = [] # array containing all processes

    finished = Event('Audio has finished playing.')




    def __init__(self):
        reload(sys)
        sys.setdefaultencoding('utf-8')

        # Create a representation for every usb sound card
        for card_name in self.get_usb_card_names():
            card = sound_card.SoundCard(card_name)
            self.card_array.append(card)

        # Populate the set containing the addresses of the root usb hubs
        self.root_hubs_set = self.get_usb_root_hub_addrs()

        # Create a semaphore for every root hub
        for hub in self.root_hubs_set:
            # semaphore with limit of 7 because of the hub bandwidth limit of 12Mbit/s
            # since our bitrate is 1.54Mbit/s,
            # 12 / 1.54 = 7.7922 gives us that the limit is 7
            self.semaphore[hub] = multiprocessing.Semaphore(7)

        # Print some info to console
        print "\033[94mAssuming %d USB root hub(s) in total.\033[0m" % len(self.root_hubs_set)
        print "\033[94mAssuming %d USB sound card(s) in total.\033[0m" % len(self.card_array)

        # Load the cached sound files into memory
        self.load_sound_files('archivos/Audio/audio_cache.csv','archivos/sounds')


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
        # Plays a single text as speech

        # Use the concatenated interface to avoid repeated code.
        text_to_speech_array = []
        text_to_speech_array.append( text_to_speech )

        self.play_concatenated(id, text_to_speech_array)


    def play_concatenated(self, id, text_to_speech_array):
        time_received = time.time()
        logging.info("[%f: [%d, %s, %s] ], " % (time_received, id, 'AUDIO_PLAY_INSTRUCTION_RECEIVED', text_to_speech_array))

        # Get the queue for the corresponding card
        queue = self.all_q[id]

        # Empty the queue
        while not queue.empty():
            queue.get()
        
        # Put the text_to_speech in the queue
        queue.put({
            'tts_concatenated': text_to_speech_array,
            'time_received': time_received
        })





    def load_sound_files(self, dictionary_filepath, sound_dir_path):
        print "Loading sound files... "
 

        with open(dictionary_filepath, 'rb') as csvfile:
            reader = csv.reader(csvfile, delimiter=';', quoting=csv.QUOTE_NONE)
            
            total_bytes = 0
            i = 0
            for line in reader:
                text_to_speech = line[0].lower()
                filename = line[1].decode('utf-8')
                
                filepath = "%s/%s" % (sound_dir_path, filename)

                # open the generated audio file
                f = open(filepath, "r+b")

                # memory-map the file, size 0 means whole file
                self.audio_mmap[text_to_speech] = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
                
                # update the total loaded size
                total_bytes = total_bytes + len(self.audio_mmap[text_to_speech])


                # print some output to show progress
                sys.stdout.write('.')
                sys.stdout.flush()
                
                i = i + 1

        print self.audio_mmap



    def read_queue(self, device_index, text_to_speech_queue):
        while True:
            # Get a queued text for turning into speech
            queued_item = text_to_speech_queue.get()
            tts_concatenated = queued_item['tts_concatenated']
            time_received = queued_item['time_received']
            

            for text_to_speech in tts_concatenated:
                timestamp = time.time()
                filename = "%s_%f" % (device_index, timestamp)

                # check if tts is not generated already
                if ( text_to_speech not in self.audio_mmap.keys() ):
                    logging.info("[%f: [%d, %f, %s, '%s'] ], " % (time.time(), device_index, time_received, 'AUDIO_MMAP_NOT_FOUND', text_to_speech))
                    # generate and mmap it
                    self.generate_and_mmap_file(text_to_speech, filename, device_index, time_received)

            # acquire semaphore
            semaphore_index = self.card_array[device_index].get_root_hub()
            logging.info("[%f: [%d, %f, %s, %s] ], " % (time.time(), device_index, time_received, 'SEMAPHORE_WAIT_START', semaphore_index))
            self.semaphore[ semaphore_index ].acquire()
            logging.info("[%f: [%d, %f, %s, %s] ], " % (time.time(), device_index, time_received, 'SEMAPHORE_WAIT_COMPLETE', semaphore_index))

            # write audios to the sound card
            try:
                #open the audio card
                print "Opening card \"%s\" (device_index = %d)..." % (self.card_array[device_index].get_name(), device_index)
                dev = alsaaudio.PCM(card="hw:CARD=%s" % ( self.card_array[device_index].get_name() ))
                
                # set it up
                # we hard code the values because of our sound card capabilities,
                # audio files to be played have to match these.
                dev.setchannels(2) # hard-coded 2 channels (stereo).
                dev.setrate(44100)  # hard-coded sample rate 48000 Hz.
                dev.setformat(alsaaudio.PCM_FORMAT_S16_LE) # sample encoding: 16-bit Signed Integer PCM
                dev.setperiodsize(320)

                for text_to_speech in tts_concatenated:
                    # get the mmap of the generated file
                    file_mmap = self.audio_mmap[text_to_speech]

                    # play the wav file
                    logging.info("[%f: [%d, %f, %s, '%s'] ], " % (time.time(), device_index, time_received, 'AUDIO_PLAY_START', text_to_speech))
                    # read and write
                    data = file_mmap.read(320)
                    while data:
                        dev.write(data)
                        data = file_mmap.read(320)
                    logging.info("[%f: [%d, %f, %s, '%s'] ], " % (time.time(), device_index, time_received, 'AUDIO_PLAY_COMPLETE', text_to_speech))
                    
                    # rewind the audio
                    file_mmap.seek(0)

                # close the audio card
                dev.close()

            except alsaaudio.ALSAAudioError as e:
                print "Exception in card \"%s\" (device_index = %d): %s" % (self.card_array[device_index].get_name(), device_index, str(e))
                logging.exception("[%f: [%d, %f, %s, '%s'] ], " % (time.time(), device_index, time_received, 'AUDIO_PLAY_EXCEPTION', text_to_speech))
                # close the audio card
                dev.close()
                pass

            # release semaphore
            self.semaphore[ self.card_array[device_index].get_root_hub() ].release()

            # fire 'finished' event
            values = queued_item
            values['id'] = device_index
            self.finished(values)


    def generate_sound_file(self, text_to_speech, filename):
        # generate the wav file
        # text2wave default voice can be changed in /etc/festival.scm. Add at the end, e.g.: (set! voice_default 'voice_JuntaDeAndalucia_es_sf_diphone)
        os.system("echo \"%s\" | text2wave -F 48000 -o archivos/sounds/%s.tmp" % (self.convert_intl_characters(text_to_speech), filename))
        # convert to stereo, thus doubling the bitrate
        os.system("sox archivos/sounds/%s.tmp -c 2 archivos/sounds/%s.wav" % (filename, filename))
        # remove the temporary file
        os.remove("archivos/sounds/%s.tmp" % filename)

    def generate_and_mmap_file(self, text_to_speech, filename, device_index, time_received):
        logging.info("[%f: [%d, %f, %s, '%s', '%s'] ], " % (time.time(), device_index, time_received, 'GENERATE_AND_MMAP_FILE_START', filename, text_to_speech))
                
        # generate the wav file
        self.generate_sound_file(text_to_speech, filename)

        # write audio file into memory
        filepath = "archivos/sounds/%s.wav" % (filename)

        # open the generated audio file
        f = open(filepath, "r+b")
        # memory-map the file, size 0 means whole file
        self.audio_mmap[text_to_speech] = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)

        logging.info("[%f: [%d, %f, %s, '%s', '%s'] ], " % (time.time(), device_index, time_received, 'GENERATE_AND_MMAP_FILE_COMPLETE', filename, text_to_speech))



            

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
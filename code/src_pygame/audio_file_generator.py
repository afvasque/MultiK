# coding=utf-8

import csv
import codecs
import os

class AudioFileGenerator:

    def __init__(self):
        fac = codecs.open('audio_cache.csv','w', 'utf-8')
        generated_audio = []

        with open('Ejercicios/EjerciciosLenguaje.csv', 'rb') as csvfile:
            reader = csv.reader(csvfile, delimiter=';', quoting=csv.QUOTE_NONE)
            i = 0
            for row in reader:
                question = row[6].decode('latin-1')
                question = question.replace(u"¿",'')
                question = question.replace(u"¡",'')
                
                if question not in generated_audio:
                    generated_audio.append(question)
                    print "i=%d; question=%s" %(i,question)
                    self.generate_sound_file(question, i)
                    fac.write(u"%s;%d.wav;\n" % (question, i)) # python will convert \n to os.linesep
                
                i = i + 1

        fac.close()




    def generate_sound_file(self, text_to_speech, filename):
        # generate the wav file
        # text2wave default voice can be changed in /etc/festival.scm. Add at the end, e.g.: (set! voice_default 'voice_JuntaDeAndalucia_es_sf_diphone)
        os.system("echo \"%s\" | text2wave -F 48000 -o %s.tmp" % (self.convert_intl_characters(text_to_speech), filename))
        # convert to stereo, thus doubling the bitrate
        os.system("sox %s.tmp -c 2 %s.wav" % (filename, filename))
        # remove the temporary file
        os.remove("%s.tmp" % filename)




    def convert_intl_characters(self, text):
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




AudioFileGenerator()
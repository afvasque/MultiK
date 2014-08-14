# -*- coding: utf-8 -*-

from librerias.keyboard_library_queue import KeyboardLibrary
from librerias import audio_library
import manejo_pantalla

# Creacion objetos librerias
lib_teclados = KeyboardLibrary()
lib_audio = audio_library.AudioLibrary()


manejo_pantalla.start(lib_teclados.total_keyboards)

frase = u"Escribe el número..."
for i in range(lib_teclados.total_keyboards):
	manejo_pantalla.write(i, frase, 0, 0)

# Recibe nro audifono y texto
print "Total de teclados: "+str(lib_teclados.total_keyboards)
while True:
	lib_audio.play(0, "hola")
	lib_audio.play(1, "audifono 1")
	lib_audio.play(2, "adios")



# Evento de teclado
def Keyboard_event(sender, earg):
    id_sent= int(earg['id'])
    text= str(earg['char']).decode('utf-8')
    time_pressed = earg['time_pressed']


# Subscripcion a evento teclado
lib_teclados.keypress += Keyboard_event




    

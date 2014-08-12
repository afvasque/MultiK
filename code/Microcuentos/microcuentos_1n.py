from librerias.keyboard_library_queue import KeyboardLibrary
import librerias.audio_library

# Creacion objetos librerias
lib_teclados = KeyboardLibrary()
lib_audio = audio_library.AudioLibrary()

# Subscripcion a evento teclado
lib.keypress += Keyboard_event

# Recibe nro audifono y texto
audio_lib.play(audifono, tts)


# Evento de teclado
def Keyboard_event(sender, earg):
    id_sent= int(earg['id'])
    text= str(earg['char']).decode('utf-8')
    time_pressed = earg['time_pressed']

    

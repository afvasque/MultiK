import audio_library

def hola(sender, earg):
	print "Termino audio en " + str(earg)



lib = audio_library.AudioLibrary(total_internal_cards=1)
lib.finished += hola

print "Audio tarjeta 1"
lib.play(0, "Hola tarjeta 1")
print "Audio tarjeta 2"
lib.play(1, "Hola tarjeta 2")
print "Audio tarjeta 3"
lib.play(2, "Hola tarjeta 3")
import audio_library

def hola(sender, earg):
	print "Termino audio en " + str(earg)



lib = audio_library.AudioLibrary(total_internal_cards=1)
lib.finished += hola

print "Audio tarjeta 1"
lib.play(0, "Hola tarjeta 1")

for i in range(0,32):
	print "Audio en tarjeta " + str(i) + "..."
	lib.play(i, "Hola Eustaquio en tarjeta " + str(i))

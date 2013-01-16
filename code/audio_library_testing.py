import audio_library

def hola(sender, earg):
	print "Termino audio en " + str(earg)



lib = audio_library.AudioLibrary(total_internal_cards=1)
lib.finished += hola

for i in range(0,lib.get_total_cards()):
	print "Audio en tarjeta " + str(i) + "..."
	lib.play(i, "Hola Eustaquio en tarjeta " + str(i))

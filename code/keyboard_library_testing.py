import keyboard_library

def hola(sender, earg):
	print str(earg)



lib = keyboard_library.KeyboardLibrary()
lib.keypress += hola
lib.start(0x0e8f,0x0022)
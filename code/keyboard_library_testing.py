import keyboard_library

def mostrar_algo_en_pantalla(sender, earg):
	print str(earg)



lib = keyboard_library.KeyboardLibrary()
lib.keypress += mostrar_algo_en_pantalla
lib.start(0x0e8f,0x0022)
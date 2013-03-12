# coding=utf-8
import keyboard_library

def mostrar_algo_en_pantalla(sender, earg):
	print str(earg)

def escribir_algo_en_archivo(sender, earg):
	f = open("%s.txt" % earg['id'], 'w+')
	f.write(earg['char'])
	f.close()


lib = keyboard_library.KeyboardLibrary()
lib.keypress += mostrar_algo_en_pantalla
lib.start(0x0e8f,0x0022)


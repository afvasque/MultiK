# coding=utf-8
#!/usr/bin/env python

import usb.core
import threading
import math
from keyboard_library_queue import *
import event

lib = KeyboardLibrary()
lib.detect_all_keyboards(0x0e8f,0x0022)

#@staticmethod
def Keyboard_event(sender, earg):
	#diccionario[int(earg['id'])].Keyboard_Pressed(sender,earg)
    print "#%s : %s" % (earg['id'], earg['char'])  # 0: id, 1: teclas

lib.keypress += Keyboard_event

lib.run(0x0e8f,0x0022)


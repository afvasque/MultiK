# coding=utf-8
#!/usr/bin/env python

import usb.core
import threading
import math
from keyboard_library_queue import *
import event

lib = KeyboardLibrary()
lib.detect_all_keyboards(0x0e8f,0x0022)

# coding=utf-8

import os
import datetime

def tts(text):
	return os.system("echo " +text+ " | festival --language spanish --tts")

tts("Muy bien, Eustaquio Gonzalez")
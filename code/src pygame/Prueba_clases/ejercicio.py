# coding=utf-8
import pygame
from clases import *
import os
import audio_library
from Reglas import *
from socket import *
import sys
import multiprocessing
from threading import Thread
from BasicOperacion import *

audio_lib = audio_library.AudioLibrary()

def scale_bitmap(bitmap, width, height):
	image = wx.ImageFromBitmap(bitmap)
	image = image.Scale(width, height, wx.IMAGE_QUALITY_HIGH)
	result = wx.BitmapFromImage(image)
	return result

def print_event(sender, earg):
	print "Terminó audio en " + str(earg)
	global audio_lib
	print str(audio_lib.reproduciendo[int(earg['id'])])
	audio_lib.reproduciendo[int(earg['id'])]=True
	print "audio_lib:"+str(audio_lib.reproduciendo[int(earg['id'])])

audio_lib.finished += print_event


class ejercicio:

	def __init__(self, pos_x, pos_y, width, height, numero_audifono, Alumno):
		print "ejercicio"
		self.pos_x = pos_x
		self.pos_y = pos_y
		self.whiteColor = pygame.Color(255,255,255)
		self.width = width
		self.height = height
		self.canvas = pygame.Surface((self.width,self.height))
		self.canvas.fill(self.whiteColor)
		self.blocked=False
		self.Objects=[]

		self.pareado= False
		self.nombre_ingresado=False

		self.mayus= False
		self.tilde=False

		self.numero_audifono= numero_audifono
		audio_lib.reproduciendo[int(self.numero_audifono)]=False
		self.Alumno_actual= Alumno
		self.reglas_main= Reglas()
		
		operacion= BasicOperacion()
		operacion.TipoOperacion= TipoOperacion.Reproduccion_letras_alfabeto
		operacion.nivelOperacion= 1
		operacion.feedback_correcto= "First"
		self.Operacion_actual= operacion

		"""
		HOST = 'localhost'
		PORT = 7388
		BUFSIZE = 1024
		ADDR = (HOST, PORT)

		tcpCliSock = socket()
		tcpCliSock.connect(ADDR)

		print 'conectando'
		data = "SustantivosFinal.multik"
		tcpCliSock.send(data)


		print 'recibiendo1'
		data = tcpCliSock.recv(BUFSIZE)
		if not data: sys.exit(0)
		print data


		print 'conectando'
		data = "30/1"
		tcpCliSock.send(data)

		print 'recibiendo2'
		data = tcpCliSock.recv(BUFSIZE)
		if not data: sys.exit(0)
		print data


		return

		#tcpCliSock.close()

		"""

		self.Operacion_actual= self.reglas_main.GetSiguienteOperacion(self.Operacion_actual, self.Alumno_actual)
			  
		self.CreateGrid(self.Operacion_actual)

		self.myfont = pygame.font.SysFont("monospace", 18)
		label = self.myfont.render("Escribe la letra...", 1, (0,0,0))
		self.canvas.blit(label,(0, 0))

		self.Objects.append(Textbox(self.canvas,0,20,300,40))
		self.canvas.blit(self.Objects[0].screen(),(self.width, self.height ))



	def CreateGrid(self, operacion):
		self.ResetLayout()

		if self.pareado == False:
			self.parear()
			return

		if operacion.TipoOperacion == TipoOperacion.Reproduccion_letras_alfabeto:
			#print operacion.nivelOperacion
			if operacion.nivelOperacion == 1:
				self.reproduccion_letras_alfabeto1(operacion)
			elif operacion.nivelOperacion ==2:
				self.reproduccion_letras_alfabeto2(operacion)
				
		elif operacion.TipoOperacion == TipoOperacion.sentido_vocales_silabas:
			
			if operacion.nivelOperacion ==1:
				self.sentido_vocales1(operacion)

		elif operacion.TipoOperacion == TipoOperacion.signos_int_excl:
			if operacion.nivelOperacion ==1:
				self.signos_int_excl1(operacion)
			elif operacion.nivelOperacion ==2:
				self.signos_int_excl2(operacion)
				
		elif operacion.TipoOperacion == TipoOperacion.mayus_nombres_propios:
			if operacion.nivelOperacion ==1:
				self.mayus_nombres_propios1(operacion)
			elif operacion.nivelOperacion ==2:
				self.mayus_nombres_propios2(operacion)
				
		elif operacion.TipoOperacion == TipoOperacion.patrones_ort_comunes:
			if operacion.nivelOperacion ==1:
				self.patrones_ort_comunes1(operacion)            
			elif operacion.nivelOperacion ==2:
				self.patrones_ort_comunes2(operacion)
			elif operacion.nivelOperacion ==3:
				self.patrones_ort_comunes3(operacion)
			elif operacion.nivelOperacion ==4:
				self.patrones_ort_comunes4(operacion)
			elif operacion.nivelOperacion ==5:
				self.patrones_ort_comunes5(operacion)

		self.Refresh()	

	def ResetLayout(self):
		self.canvas.fill(self.whiteColor)
		self.Objects= []

		
	def screen(self):
		return self.canvas

	def react(self,input):

		self.Objects[0].react(input)


	def arreglar_texto(self, texto):
			   
		return texto
	
		# Reconocimiento de signos de interrogacion y exclamación

		if self.mayus:
			if texto== "'":
				texto="?"
			elif texto== "¿":
				texto="¡"
			elif texto=="1":
				texto="!"
			self.mayus=False

		if self.tilde:
			if texto=="a":
				texto="á"
			elif texto=="e":
				texto="é"
			elif texto=="i":
				texto="í"
			elif texto=="o":
				texto="ó"
			elif texto=="u":
				texto="ú"
			self.mayus=False
			self.tilde=False
			
			
		# Reconocimiento de tildes

		if texto=="tilde":
			self.tilde=True

		if texto=="mayus":
			self.mayus=True
			texto=""
			
		return texto


	lib_play_proc = None
	def TexttoSpeech(self, text_to_speech):
		print "reproduciendo"
		#if audio_lib.reproduciendo[self.numero_audifono]==False:
		if self.lib_play_proc is None:
			self.text_to_speech_queue = multiprocessing.Queue()
			self.lib_play_proc = multiprocessing.Process(target=audio_lib.play, args=(self.numero_audifono, self.text_to_speech_queue))
			self.lib_play_proc.start()          
		
		if len(text_to_speech)>0:
			print "Reproduciendo en audÃ­fono #%s: \"%s\"" % (self.numero_audifono, text_to_speech)
			audio_lib.reproduciendo[int(self.numero_audifono)]=True
			print str(self.numero_audifono)+" "+str(audio_lib.reproduciendo[self.numero_audifono])
			self.text_to_speech_queue.put(text_to_speech)

	##########  PAREAMIENTO ##############
	

	def parear(self):

		self.ResetLayout()

		self.Operacion_actual.audio_pregunta= "Escribe el número"+str(self.numero_audifono)

		self.TexttoSpeech(self.Operacion_actual.audio_pregunta)

		self.Objects.append(Textbox(self.canvas,0,20,300,40))
		self.canvas.blit(self.Objects[0].screen(),(self.width, self.height ))



#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
from clases import *
import os
import audio_library
from Reglas import *
from socket import *
import sys
import multiprocessing
import time
from threading import Thread
from BasicOperacion import *

audio_lib = audio_library.AudioLibrary()

def scale_bitmap(bitmap, width, height):
	image = wx.ImageFromBitmap(bitmap)
	image = image.Scale(width, height, wx.IMAGE_QUALITY_HIGH)
	result = wx.BitmapFromImage(image)
	return result

def print_event(sender, earg):
	timestamp = time.time()
	print str(timestamp)+" Terminó audio en " + str(earg)
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

		self.Operacion_actual= self.reglas_main.GetSiguienteOperacion(self.Operacion_actual, self.Alumno_actual)
			  
		self.CreateGrid(self.Operacion_actual)


	def CreateGrid(self, operacion):
		self.ResetLayout()

		if self.pareado == False:
			print "parear"
			self.parear()
			return

		if operacion.TipoOperacion == TipoOperacion.Reproduccion_letras_alfabeto:
			if operacion.nivelOperacion == 1:
				self.reproduccion_letras_alfabeto1(operacion)
			elif operacion.nivelOperacion ==2:
				self.reproduccion_letras_alfabeto2(operacion)
				
		elif operacion.TipoOperacion == TipoOperacion.sentido_vocales_silabas:
			
			if operacion.nivelOperacion ==1:
				self.sentido_vocales1(operacion)
			elif operacion.nivelOperacion ==2:
				self.sentido_vocales2(operacion)
			elif operacion.nivelOperacion ==3:
				self.sentido_vocales3(operacion)

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


	def ResetLayout(self):
		self.canvas.fill(self.whiteColor)
		self.Objects= []

		
	def screen(self):
		return self.canvas

	def react(self,input):

		self.Objects[0].react(input)


	def reproduccion_letras_alfabeto1(self,operacion):

		self.TexttoSpeech(operacion.audio_pregunta)

		pygame.font.init()
		size= int(1.5 * self.width/len(operacion.pregunta))
		self.myfont = pygame.font.SysFont("monospace", size)
		label = self.myfont.render(operacion.pregunta, 1, (0,0,0))
		self.canvas.blit(label,(0, 0))
		
		self.Objects.append(Textbox(int(self.width*0.05),int(self.height/2),int(self.width*0.95),int(size*1.2)))
		self.canvas.blit(self.Objects[0].screen(),(self.Objects[0].pos_x, self.Objects[0].pos_y ))
		
		myimage = pygame.image.load("Imagenes/comida.jpg")

		self.new_width = ((self.height / 2) * myimage.get_width()) / myimage.get_height();

		self.canvas.blit(myimage, (self.width/2-self.height/5,self.height/8,self.new_width,self.height/2))
		pygame.display.flip()

	def reproduccion_letras_alfabeto2(self,operacion):

		self.TexttoSpeech(operacion.audio_pregunta)

		self.Objects.append(Listview(operacion.alternativas,int(self.width*0.05),int(self.height/4),int(self.width*0.95),int(self.height/2)))
		self.canvas.blit(self.Objects[0].screen(),(self.Objects[0].pos_x, self.Objects[0].pos_y))


	def sentido_vocales1(self, operacion):        
		
		self.TexttoSpeech(operacion.audio_pregunta)
		
		self.Objects.append(Listview(operacion.alternativas,int(self.width*0.05),int(self.height/4),int(self.width*0.95),int(self.height/2)))
		self.canvas.blit(self.Objects[0].screen(),(self.Objects[0].pos_x, self.Objects[0].pos_y))
		
	def sentido_vocales2(self, operacion):        
		
		self.TexttoSpeech(operacion.audio_pregunta)

		pygame.font.init()
		size= int(1.5 * self.width/len(operacion.pregunta))
		self.myfont = pygame.font.SysFont("monospace", size)
		label = self.myfont.render(operacion.pregunta, 1, (0,0,0))
		self.canvas.blit(label,(0, 0))
		
		self.Objects.append(Textbox(int(self.width*0.05),int(self.height/2),int(self.width*0.95),int(size*1.2)))
		self.canvas.blit(self.Objects[0].screen(),(self.Objects[0].pos_x, self.Objects[0].pos_y ))
				
	def sentido_vocales3(self, operacion):        
		
		self.TexttoSpeech(operacion.audio_pregunta)

		pygame.font.init()
		size= int(1.5 * self.width/len(operacion.pregunta))
		self.myfont = pygame.font.SysFont("monospace", size)
		label = self.myfont.render(operacion.pregunta, 1, (0,0,0))
		self.canvas.blit(label,(0, 0))
		
		self.Objects.append(Textbox(int(self.width*0.05),int(self.height/2),int(self.width*0.95),int(size*1.2)))
		self.canvas.blit(self.Objects[0].screen(),(self.Objects[0].pos_x, self.Objects[0].pos_y ))
	
	def signos_int_excl1(self, operacion):        
			
		self.TexttoSpeech(operacion.audio_pregunta)

		pygame.font.init()
		size= int(self.height/6)
		self.myfont = pygame.font.SysFont("monospace", size)
		label = self.myfont.render(operacion.pregunta, 1, (0,0,0))
		self.canvas.blit(label,(0, 0))

		self.Objects.append(Textbox(int(self.width*0.05),int(self.height/2),int(self.width*0.95),int(size*1.2)))
		self.canvas.blit(self.Objects[0].screen(),(self.Objects[0].pos_x, self.Objects[0].pos_y ))

	def signos_int_excl2(self, operacion):        
		
		self.TexttoSpeech(operacion.audio_pregunta)
		
		self.Objects.append(Textbox(0,20,300,40))
		self.canvas.blit(self.Objects[0].screen(),(self.Objects[0].pos_x, self.Objects[0].pos_y ))       
		
		pygame.font.init() 
		size= int(self.height/6)
		self.myfont = pygame.font.SysFont("monospace", size)
		label = self.myfont.render(operacion.pregunta, 1, (0,0,0))
		self.canvas.blit(label,(0, 0))
		
		self.Objects.append(Textbox(int(self.width*0.05),int(self.height/2),int(self.width*0.95),int(size*1.2)))
		self.canvas.blit(self.Objects[0].screen(),(self.Objects[0].pos_x, self.Objects[0].pos_y ))
		
	def mayus_nombres_propios1(self, operacion):        
				
		self.TexttoSpeech(operacion.audio_pregunta)
		
		self.Objects.append(Listview(operacion.alternativas,int(self.width*0.05),int(self.height/4),int(self.width*0.95),int(self.height/2)))
		self.canvas.blit(self.Objects[0].screen(),(self.Objects[0].pos_x, self.Objects[0].pos_y))

	# pendiente
	def mayus_nombres_propios2(self, operacion):        
		
		return

	def patrones_ort_comunes1(self, operacion):        
		
		pygame.font.init() 
		size= int(self.height/6)
		self.myfont = pygame.font.SysFont("monospace", size)
		label = self.myfont.render(operacion.pregunta, 1, (0,0,0))
		self.canvas.blit(label,(0, 0))
		
		self.TexttoSpeech(operacion.audio_pregunta)
		
		self.Objects.append(Listview(operacion.alternativas,int(self.width*0.05),int(self.height/4),int(self.width*0.95),int(self.height/2)))
		self.canvas.blit(self.Objects[0].screen(),(self.Objects[0].pos_x, self.Objects[0].pos_y))
		
	
	def patrones_ort_comunes2(self, operacion):        
		
		self.TexttoSpeech(operacion.audio_pregunta)

		pygame.font.init() 
		size= int(1.5 * self.width/len(operacion.pregunta))
		self.myfont = pygame.font.SysFont("monospace", size)
		label = self.myfont.render(operacion.pregunta, 1, (0,0,0))
		self.canvas.blit(label,(0, 0))
		
		self.Objects.append(Textbox(int(self.width*0.05),int(self.height/2),int(self.width*0.95),int(size*1.2)))
		self.canvas.blit(self.Objects[0].screen(),(self.Objects[0].pos_x, self.Objects[0].pos_y ))
		
	
	def patrones_ort_comunes3(self, operacion):        
		
		# Falta imagen!!
		
		self.TexttoSpeech(operacion.audio_pregunta)

		pygame.font.init() 
		self.myfont = pygame.font.SysFont("monospace", int(1.5 * self.width/len(operacion.pregunta)))
		label = self.myfont.render(operacion.pregunta, 1, (0,0,0))
		self.canvas.blit(label,(0, 0))
		
		
		
		self.Objects.append(Listview(operacion.alternativas,int(self.width*0.05),int(self.height/4),int(self.width*0.95),int(self.height/2)))
		self.canvas.blit(self.Objects[0].screen(),(self.Objects[0].pos_x, self.Objects[0].pos_y))
		
	
	def patrones_ort_comunes4(self, operacion):        
		
		pygame.font.init() 
		self.myfont = pygame.font.SysFont("monospace", size= int(self.height/6))
		label = self.myfont.render(operacion.pregunta, 1, (0,0,0))
		self.canvas.blit(label,(0, 0))
		
		self.TexttoSpeech(operacion.audio_pregunta)
		
		self.Objects.append(Listview(operacion.alternativas,int(self.width*0.05),int(self.height/4),int(self.width*0.95),int(self.height/2)))
		self.canvas.blit(self.Objects[0].screen(),(self.Objects[0].pos_x, self.Objects[0].pos_y))
	
	def patrones_ort_comunes5(self, operacion):        
		
		self.TexttoSpeech(operacion.audio_pregunta)

		pygame.font.init() 
		size= int(self.height/6)
		self.myfont = pygame.font.SysFont("monospace", size)
		label = self.myfont.render(operacion.pregunta, 1, (0,0,0))
		self.canvas.blit(label,(0, 0))
		
		self.Objects.append(Textbox(int(self.width*0.05),int(self.height/2),int(self.width*0.95),int(size*1.2)))
		self.canvas.blit(self.Objects[0].screen(),(self.Objects[0].pos_x, self.Objects[0].pos_y ))
		
		return



	def arreglar_texto(self, texto):
		
		#return texto
	
		print "tilde: "+str(self.tilde)
		if self.tilde:
			if texto=="a":
				texto=u"á"
			elif texto=="e":
				texto=u"é"
			elif texto=="i":
				texto=u"í"
			elif texto=="o":
				texto=u"ó"
			elif texto=="u":
				texto=u"ú"
			self.tilde=False
			
			
		# Reconocimiento de tildes

		if texto=="´":
			self.tilde=True
			texto=""

		return texto


	lib_play_proc = None
	def TexttoSpeech(self, text_to_speech):
		#if audio_lib.reproduciendo[self.numero_audifono]==False:
		if self.lib_play_proc is None:
			self.text_to_speech_queue = multiprocessing.Queue()
			self.lib_play_proc = multiprocessing.Process(target=audio_lib.play, args=(self.numero_audifono, self.text_to_speech_queue))
			self.lib_play_proc.start()          
		
		if len(text_to_speech)>0:
			print "Reproduciendo en audifono #%s: \"%s\"" % (self.numero_audifono, text_to_speech)
			audio_lib.reproduciendo[int(self.numero_audifono)]=True
			print str(self.numero_audifono)+" "+str(audio_lib.reproduciendo[self.numero_audifono])
			self.text_to_speech_queue.put(text_to_speech)

	##########  PAREAMIENTO ##############
	

	def parear(self):

		self.ResetLayout()

		self.Operacion_actual.audio_pregunta= "Escribe el número %d" % self.numero_audifono

		self.TexttoSpeech(self.Operacion_actual.audio_pregunta)

		pygame.font.init()
		frase = u"Escribe el número..."
		size= int(1.5 * self.width/(len(frase)))
		self.myfont = pygame.font.SysFont("monospace", size)
		label = self.myfont.render(frase, 1, (0,0,0))
		self.canvas.blit(label,(0, 0))
		
		self.Objects.append(Textbox(int(self.width*0.05),int(self.height/2),int(self.width*0.9),int(size*1.2)))
		self.canvas.blit(self.Objects[0].screen(),(self.Objects[0].pos_x, self.Objects[0].pos_y ))

	def ModificarPareamiento(self, diccionario, earg):
		
		text= str(earg['char']).decode('utf-8')
		text= self.arreglar_texto(text)
		
		if self.pareado== True and self.nombre_ingresado==False:
			textctrl= self.Objects[0]
			if text=="Enter" and len(textctrl.Value)>0:
				temp_nombre= textctrl.Value
				nombre_caps= temp_nombre.title()
				self.Alumno_actual.Nombre= nombre_caps
				self.nombre_ingresado=True
				self.Operacion_actual.feedback_correcto= "First"
				self.Operacion_actual.RespuestaCorrecta()
				self.Operacion_actual= self.reglas_main.GetSiguienteOperacion(self.Operacion_actual, self.Alumno_actual)
				self.CreateGrid(self.Operacion_actual)
		

		elif self.pareado== False and self.nombre_ingresado==False:
			textctrl= self.Objects[0]
			if text=="Enter" and len(textctrl.Value)>0:
				temp= int(textctrl.Value)
				if temp>=0 and temp< len(diccionario):
					self.numero_audifono=temp
					self.pareado=True
					self.lib_play_proc=None
					self.set_nombre()
					
		# reconocimiento de backspace para borrado
		

		self.Objects[0].react(text)
		self.canvas.blit(self.Objects[0].screen(),(self.Objects[0].pos_x, self.Objects[0].pos_y ))
		'''
		if self.pareado==False:
			if text=="0" or text=="1" or text=="2" or text=="3" or text=="4" or text=="5" or text=="6" or text=="7" or text=="8" or text=="9":
				self.Objects[0].react(text)
				self.canvas.blit(self.Objects[0].screen(),(self.Objects[0].pos_x, self.Objects[0].pos_y ))
		else:
			self.Objects[0].react(text)
			self.canvas.blit(self.Objects[0].screen(),(self.Objects[0].pos_x, self.Objects[0].pos_y ))
		'''
	



	def Keyboard_Pressed(self, sender, earg):

		text= str(earg['char']).decode('utf-8')
		text= self.arreglar_texto(text)
		
		if len(text)==0:
			return

		if text == "Enter":
			
			if ((self.Operacion_actual.TipoOperacion == TipoOperacion.Reproduccion_letras_alfabeto and self.Operacion_actual.nivelOperacion == 2) or
				(self.Operacion_actual.TipoOperacion == TipoOperacion.mayus_nombres_propios and self.Operacion_actual.nivelOperacion == 1) or
				(self.Operacion_actual.TipoOperacion == TipoOperacion.patrones_ort_comunes and self.Operacion_actual.nivelOperacion == 1) or
				(self.Operacion_actual.TipoOperacion == TipoOperacion.patrones_ort_comunes and self.Operacion_actual.nivelOperacion == 3) or
				(self.Operacion_actual.TipoOperacion == TipoOperacion.patrones_ort_comunes and self.Operacion_actual.nivelOperacion == 4) or
				(self.Operacion_actual.TipoOperacion == TipoOperacion.sentido_vocales_silabas and self.Operacion_actual.nivelOperacion == 1)):
				
				if isinstance(self.Objects[0],Listview):
					
					listview= self.Objects[0]
					print "Respuesta"
					print  listview.answer()
					print self.Operacion_actual.respuesta
					if listview.answer() == self.Operacion_actual.respuesta:
						self.TexttoSpeech(self.Operacion_actual.feedback_correcto.decode('utf8'))
						self.Operacion_actual.RespuestaCorrecta()
					else:
						self.TexttoSpeech(self.Operacion_actual.feedback_error.decode('utf8'))
						self.Operacion_actual.RespuestaIncorrecta()

					'''
					if len(list.GetSelections())>0:
						if list.Items[list.GetSelections()[0]] == self.Operacion_actual.respuesta:
							list.Clear()
							list.Append(self.Operacion_actual.feedback_correcto)
							self.TexttoSpeech(self.Operacion_actual.feedback_correcto)
							self.Operacion_actual.RespuestaCorrecta()

						else:
							list.Clear()
							list.Append(self.Operacion_actual.feedback_error)
							self.TexttoSpeech(self.Operacion_actual.feedback_error)
							self.Operacion_actual.RespuestaIncorrecta()
					'''
			elif ((self.Operacion_actual.TipoOperacion == TipoOperacion.Reproduccion_letras_alfabeto and self.Operacion_actual.nivelOperacion == 1) or
				(self.Operacion_actual.TipoOperacion == TipoOperacion.signos_int_excl and self.Operacion_actual.nivelOperacion == 1) or
				(self.Operacion_actual.TipoOperacion == TipoOperacion.patrones_ort_comunes and self.Operacion_actual.nivelOperacion == 2) or
				(self.Operacion_actual.TipoOperacion == TipoOperacion.patrones_ort_comunes and self.Operacion_actual.nivelOperacion == 5) or
				(self.Operacion_actual.TipoOperacion == TipoOperacion.sentido_vocales_silabas and self.Operacion_actual.nivelOperacion == 2) or
				(self.Operacion_actual.TipoOperacion == TipoOperacion.sentido_vocales_silabas and self.Operacion_actual.nivelOperacion == 3)):
				
				
				textctrl= self.Objects[0]
				
				if self.Operacion_actual.TipoOperacion == TipoOperacion.signos_int_excl:
					resp= self.Operacion_actual.respuesta.split(",")
					if ((resp[0] in textctrl.Value) and (resp[1] in textctrl.Value)):
						textctrl.Value= self.Operacion_actual.respuesta
						
				if textctrl.Value == self.Operacion_actual.respuesta:
					print u"feedback: "+self.Operacion_actual.feedback_correcto
					self.TexttoSpeech(self.Operacion_actual.feedback_correcto.decode('utf8'))
					self.Operacion_actual.RespuestaCorrecta()
					textctrl.Value=""
				else:
					self.TexttoSpeech(self.Operacion_actual.feedback_error.decode('utf8'))
					self.Operacion_actual.RespuestaIncorrecta()
					textctrl.Value=""
					
			self.Operacion_actual= self.reglas_main.GetSiguienteOperacion(self.Operacion_actual, self.Alumno_actual)
			self.CreateGrid(self.Operacion_actual)
		
		self.Objects[0].react(text)
		self.canvas.blit(self.Objects[0].screen(),(self.Objects[0].pos_x, self.Objects[0].pos_y ))


 	def RepetirPregunta(self):
		print "Repetir pregunta"
		print self.Operacion_actual.audio_pregunta
		self.TexttoSpeech(self.Operacion_actual.audio_pregunta)            
		
	

	def set_nombre(self):
		self.ResetLayout()
		self.Operacion_actual.audio_pregunta= "Ingresa tu nombre"
		self.TexttoSpeech(self.Operacion_actual.audio_pregunta)

		pygame.font.init()
		frase = u"Ingresa tu nombre"
		size= int(1.5 * self.width/len(frase))
		self.myfont = pygame.font.SysFont("monospace", size)
		label = self.myfont.render(frase, 1, (0,0,0))
		self.canvas.blit(label,(0, 0))
		
		self.Objects.append(Textbox(int(self.width*0.05),int(self.height/2),int(self.width*0.9),int(size*1.2)))
		self.canvas.blit(self.Objects[0].screen(),(self.Objects[0].pos_x, self.Objects[0].pos_y ))


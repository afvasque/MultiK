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
import math
import logging
from threading import Thread
from threading import Timer 
from BasicOperacion import *

logging.basicConfig(filename='multik.log',level=logging.INFO)

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
		self.backColor = pygame.Color(random.randint(100, 255),random.randint(100, 255),random.randint(100, 255))
		self.width = width
		self.height = height
		self.canvas = pygame.Surface((self.width,self.height))
		self.canvas.fill(self.backColor)
		self.blocked=False
		self.Objects=[]

		
		self.mayus= False
		self.tilde=False
		
		self.speaking = False

		self.numero_audifono= numero_audifono
		self.Alumno_actual= Alumno
		self.reglas_main= Reglas()

		self.resp_correct=False
		self.resp_incorrect=False
		
		operacion= BasicOperacion()
		operacion.TipoOperacion= TipoOperacion.primero
		operacion.nivelOperacion= 1
		operacion.feedback_correcto= "First"

		self.Operacion_actual= self.reglas_main.GetSiguienteOperacion(operacion, self.Alumno_actual)

			  
		self.CreateGrid(self.Operacion_actual)


	def CreateGrid(self, operacion):
		self.ResetLayout()

		print "audio_pregunta"+operacion.audio_pregunta
		

		tipo_op= operacion.GetControlType()
		print "Tipo:"+tipo_op

		if tipo_op=="Texto":
			self.SetLayoutText(operacion)
		elif tipo_op=="Lista":
			self.SetLayoutList(operacion)



	def ResetLayout(self):
		self.canvas.fill(self.backColor)
		self.Objects= []

		
	def screen(self):
		return self.canvas

	def react(self,input):

		self.Objects[0].react(input)


	def SetLayoutText(self,operacion):

		print"texto"
		print "audio: "+operacion.audio_pregunta
		self.TexttoSpeech(operacion.audio_pregunta)

		self.xtext= 0
		self.ytext= int(self.height*(1/16))

		if len(operacion.path_imagen)>1:

			textsize= self.height/8
			myimage = pygame.image.load("Imagenes/"+operacion.path_imagen)

			print "temp:"+str(temp)

			self.new_width = ((self.height / (temp*2)) * myimage.get_width()) / myimage.get_height();

			myimage= pygame.transform.scale(myimage, (self.new_width, self.height/(temp*2))) 
			self.canvas.blit(myimage, (self.width/2-self.height/5,0,self.new_width,self.height/(temp*2)))

			self.ytext= int(self.height/2)

			textsize= self.GetSizeTextImg(len(operacion.pregunta))

		
		if len(operacion.pregunta)>0:

			self.WriteLines(operacion)	


		textbox_x= int(self.width*0.05)
		textbox_y= self.ytext+self.height*0.02

		height_textbox= int(self.height-textbox_y)

		if height_textbox > int(self.height*0.3):
			height_textbox= int(self.height*0.3)

		self.Objects.append(Textbox(textbox_x,textbox_y,int(self.width*0.8),height_textbox))
		self.canvas.blit(self.Objects[0].screen(),(self.Objects[0].pos_x, self.Objects[0].pos_y ))

		pygame.display.flip()
		return

	def SetLayoutList(self,operacion):

		print"lista"
		self.TexttoSpeech(operacion.audio_pregunta)

		self.xtext= 0
		self.ytext= int(self.height*(1/8))

		# la variable temp dice cuantas lineas tiene cada frase.
		temp=1
		textsize= self.GetSizeHorizontal(len(operacion.pregunta))

		if len(operacion.pregunta)>0:
			temp= len(operacion.pregunta)/12


		if len(operacion.path_imagen)>1:

			myimage = pygame.image.load("Imagenes/"+operacion.path_imagen)

			self.new_width = ((self.height / 4) * myimage.get_width()) / myimage.get_height();
			myimage= pygame.transform.scale(myimage, (self.new_width, self.height/(temp*4))) 

			self.canvas.blit(myimage, (self.width/2-self.height/5,self.height/8,self.new_width,self.height/(temp*2)))

			self.ytext= int(self.height/2)

			textsize= self.GetSizeTextImg(len(operacion.pregunta))
		
		print "temp: "+str(temp)

		if len(operacion.pregunta)>0:

			self.WriteLines(operacion)
		
		listview_x= int(self.width*0.05)
		listview_y= self.ytext+self.height*0.02

		self.Objects.append(Listview(operacion.alternativas,listview_x,listview_y,int(self.width*0.8),int(self.height-listview_y)))
		self.canvas.blit(self.Objects[0].screen(),(self.Objects[0].pos_x, self.Objects[0].pos_y))

		return


	def WriteLines(self, operacion):

		sep=12 # caracteres para separar lineas
		temp= len(operacion.pregunta)/float(sep)
		print "temp"+str(temp)
		temp= math.ceil(temp)

		print "temp:"+str(temp)

		div_inicio=0
		div_fin=0
		global_textsize=500

		# se guardan en listas para escribir todo después de calcular el tamaño global de texto
		list_cleanpreguntas= list()
		
		for x in range(0,int(temp)):

			try:
				div_fin= operacion.pregunta.index(" ",div_fin+sep)
			except Exception, e:
				div_fin= len(operacion.pregunta)
			
			if div_inicio> div_fin:
				break;
			
			clean_pregunta=" "
			if div_fin< len(operacion.pregunta):
				clean_pregunta= operacion.pregunta[div_inicio:div_fin]
			else:
				clean_pregunta= operacion.pregunta[div_inicio:]

			textsize= self.GetSizeHorizontal(len(clean_pregunta))

			if global_textsize> textsize:
				global_textsize= textsize

			list_cleanpreguntas.append(clean_pregunta)
			print "clean:"+clean_pregunta

			div_inicio= div_fin+1

		for x in range(0,len(list_cleanpreguntas)):
			self.WriteColor(list_cleanpreguntas[x], self.xtext, self.ytext, global_textsize)
			self.ytext= self.ytext+ global_textsize
		return	

	def WriteColor(self, pregunta, xtext, ytext, textsize):

		print "ddd:"+ pregunta
		if "&" in pregunta:

			clean_pregunta= pregunta.replace("&","")
			self.myfont = pygame.font.SysFont("monospace", textsize)
			label = self.myfont.render(clean_pregunta, 1, (255,0,0))
			self.canvas.blit(label,(xtext, ytext))
			#self.canvas.blit(label,(0,0))

			masked_pregunta= pregunta

			while "&" in masked_pregunta:

				temp_start= masked_pregunta.index("&")
				temp_end= masked_pregunta.index("&",temp_start+1)

				for x in range(temp_start,temp_end):
					masked_pregunta= masked_pregunta[:x]+" "+masked_pregunta[(x+1):]
				masked_pregunta= masked_pregunta[:temp_start]+masked_pregunta[(temp_start+1):]
				masked_pregunta= masked_pregunta[:(temp_end-1)]+masked_pregunta[(temp_end):]
				print "eee:"+masked_pregunta

			self.myfont = pygame.font.SysFont("monospace", textsize+1)
			label = self.myfont.render(masked_pregunta, 1, (0,0,0))

			self.canvas.blit(label,(xtext, ytext))


		else:
			pygame.font.init()
			self.myfont = pygame.font.SysFont("monospace", textsize)
			label = self.myfont.render(pregunta, 1, (0,0,0))
			self.canvas.blit(label,(xtext, ytext))
			print "escribiendo: "+pregunta

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


	def TexttoSpeech(self, text_to_speech):
		
		if len(text_to_speech)>0:

			self.speaking = True
			# para concatenar los audios sin regenerarlos
			text_to_speech_conc = []

			if "¿" in text_to_speech:
				text_to_speech= text_to_speech.replace("¿","")
			

			if self.resp_correct:
				text_to_speech_conc.append(self.Operacion_actual.feedback_correcto.decode('utf8')+". ")
				self.resp_correct=False
			elif self.resp_incorrect:
				text_to_speech_conc.append(self.Operacion_actual.feedback_error.decode('utf8')+". ")
				self.resp_incorrect=False

			text_to_speech_conc.append(text_to_speech)

			print "Reproduciendo en audifono #%s: \"%s\"" % (self.numero_audifono, text_to_speech)
						
			audio_lib.play_concatenated(self.numero_audifono, text_to_speech_conc)

			def EnableAudio():
				self.speaking=False

			# son 0.15 segundos por caracter, para que sea medio segundo aprox por palabra
			t = Timer(1,EnableAudio)
			t.start()



	
	def Keyboard_Pressed(self, sender, earg):

		#try:
		text= str(earg['char']).decode('utf-8')
		text= self.arreglar_texto(text)
		
		if len(text)==0 or self.speaking==True:
			return

		if text == "Enter":

			
			if len(self.Operacion_actual.alternativas)>0:
				if isinstance(self.Objects[0],Listview):
					
					listview= self.Objects[0]
					
					if listview.answer() == self.Operacion_actual.respuesta:
						logging.info("[%f: [%d, %s, %s, %s, %s] ], " % (time.time(), self.numero_audifono, 'CORRECT_ANSWER', self.Operacion_actual.pregunta,self.Operacion_actual.audio_pregunta , self.Operacion_actual.respuesta))
						#self.TexttoSpeech(self.Operacion_actual.feedback_correcto.decode('utf8'))
						self.resp_correct=True
						self.Operacion_actual.RespuestaCorrecta()
					else:
						# WRONG_ANSWER, pregunta, audio_pregunta, respuesta alumno, respuesta
						logging.info("[%f: [%d, %s, %s, %s, %s, %s] ], " % (time.time(), self.numero_audifono, 'WRONG_ANSWER', self.Operacion_actual.pregunta,self.Operacion_actual.audio_pregunta , listview.answer() ,self.Operacion_actual.respuesta))
						#self.TexttoSpeech(self.Operacion_actual.feedback_error.decode('utf8'))
						self.resp_incorrect=True
						self.Operacion_actual.RespuestaIncorrecta()

					
			else:

				textctrl= self.Objects[0]
						
				if textctrl.Value.strip() == self.Operacion_actual.respuesta:
					# CORRECT_ANSWER, pregunta, audio_pregunta, respuesta
					logging.info("[%f: [%d, %s, %s, %s, %s] ], " % (time.time(), self.numero_audifono, 'CORRECT_ANSWER', self.Operacion_actual.pregunta,self.Operacion_actual.audio_pregunta ,self.Operacion_actual.respuesta))
					#self.TexttoSpeech(self.Operacion_actual.feedback_correcto.decode('utf8'))
					self.resp_correct=True
					self.Operacion_actual.RespuestaCorrecta()
					textctrl.Value=""
				else:
					# WRONG_ANSWER, pregunta, audio_pregunta, respuesta alumno, respuesta
					logging.info("[%f: [%d, %s, %s, %s, %s, %s] ], " % (time.time(), self.numero_audifono, 'WRONG_ANSWER', self.Operacion_actual.pregunta,self.Operacion_actual.audio_pregunta , textctrl.Value ,self.Operacion_actual.respuesta))
					#self.TexttoSpeech(self.Operacion_actual.feedback_error.decode('utf8'))
					self.resp_incorrect=True
					self.Operacion_actual.RespuestaIncorrecta()
					textctrl.Value=""
			
			cambia_nivel= Reglas_Fijas.CambioNivel(self.Operacion_actual)

			self.Operacion_actual= self.reglas_main.GetSiguienteOperacion(self.Operacion_actual, self.Alumno_actual)

			if cambia_nivel == CambioNivel.Sube:
				logging.info("[%f: [%d, %s, %d] ], " % (time.time(), self.numero_audifono, 'LEVEL_UP', self.Operacion_actual.nivelOperacion))
			self.CreateGrid(self.Operacion_actual)
		
		self.Objects[0].react(text)
		self.canvas.blit(self.Objects[0].screen(),(self.Objects[0].pos_x, self.Objects[0].pos_y ))
		# Tiempo respuesta desde decision de Pucca
		logging.info("[%f: [%d, %s, %s, %s, %s] ], " % (time.time(), self.numero_audifono, 'CORRECT_ANSWER', self.Operacion_actual.pregunta,self.Operacion_actual.audio_pregunta ,self.Operacion_actual.respuesta))




	def RepetirPregunta(self):
		#print "Repetir pregunta"
		#print self.Operacion_actual.audio_pregunta
		logging.info("[%f: [%d, %s, %s] ], " % (time.time(), self.numero_audifono, 'REPEAT_QUESTION',self.Operacion_actual.audio_pregunta))
		self.TexttoSpeech(self.Operacion_actual.audio_pregunta)            
		
	
	##### Utilidades ######
	#### funciones que obtienen el tamaño para los ejercicios

	def GetSizeVertical(self, x):

		if x==0:
			return int(2.3 * self.width)
		if x>15:
			return int(1.5 * self.width/x)
		elif x>10:
			return int(1.8*self.width/x)
		elif x>6:
			return int(2 * self.width/x)
		else:
			return int(2.3 * self.width/x)

	def GetSizeHorizontal(self, x):

		if x<6:
			x=8

		if x==0:
			return int(1.5 * self.width)
		
		return int(1.5 * self.width/x)


	def GetSizeTextImg(self, x):
		if x==0:
			return int(1.5 * self.width)
		if x>40:
			return int(0.8 * self.width/x)
		elif x>30:
			return int(self.width/x)
		elif x>25:
			return int(1.2 * self.width/x)
		else:
			return int(1.5 * self.width/x)





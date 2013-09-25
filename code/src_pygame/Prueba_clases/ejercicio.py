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
		self.recien_pareado= False
		self.speaking = False

		self.numero_audifono= numero_audifono
		audio_lib.reproduciendo[int(self.numero_audifono)]=False
		self.Alumno_actual= Alumno
		self.reglas_main= Reglas()
		
		operacion= BasicOperacion()
		operacion.TipoOperacion= TipoOperacion.primero
		operacion.nivelOperacion= 1
		operacion.feedback_correcto= "First"
		self.Operacion_actual= operacion

			  
		self.CreateGrid(self.Operacion_actual)


	def CreateGrid(self, operacion):
		self.ResetLayout()

		print "audio_pregunta"+operacion.audio_pregunta
		if self.pareado == False:
			print "parear"
			self.parear()
			return

		tipo_op= operacion.GetControlType()
		print "Tipo:"+tipo_op

		if tipo_op=="Texto":
			self.SetLayoutText(operacion)
		elif tipo_op=="Lista":
			self.SetLayoutList(operacion)



	def ResetLayout(self):
		self.canvas.fill(self.whiteColor)
		self.Objects= []

		
	def screen(self):
		return self.canvas

	def react(self,input):

		self.Objects[0].react(input)


	def SetLayoutText(self,operacion):

		print"texto"
		self.TexttoSpeech(operacion.audio_pregunta)

		xtext= 0
		ytext= int(self.height*(1/8))

		temp=1
		textsize= self.height/8

		if len(operacion.pregunta)>0:
			temp= len(operacion.pregunta)/15
			textsize= self.GetSizeHorizontal(len(operacion.pregunta))
		
		if temp==0:
			temp=1

		print "temp:"+str(temp)
		if len(operacion.path_imagen)>1:

			myimage = pygame.image.load("Imagenes/"+operacion.path_imagen)

			print "temp:"+str(temp)

			self.new_width = ((self.height / (temp*2)) * myimage.get_width()) / myimage.get_height();

			myimage= pygame.transform.scale(myimage, (self.new_width, self.height/(temp*2))) 
			self.canvas.blit(myimage, (self.width/2-self.height/5,0,self.new_width,self.height/(temp*2)))

			ytext= int(self.height/2)

			textsize= self.GetSizeTextImg(len(operacion.pregunta))

		
		if len(operacion.pregunta)>0:
			if temp<=1:
				self.WriteColor(operacion.pregunta, xtext, ytext, textsize)	
				ytext= ytext+textsize

			elif temp<=2:
				div= operacion.pregunta.index(" ",15)

				if div ==-1:
					div=operacion.pregunta.index(" ")

				start=0
				end= div

				clean_pregunta= operacion.pregunta[:div]
				self.WriteColor(clean_pregunta, xtext, ytext, textsize)	
				clean_pregunta= operacion.pregunta[(div+1):]
				self.WriteColor(clean_pregunta, xtext, ytext+textsize, textsize)
				ytext= ytext+textsize

			elif temp<=4:
				ytext= ytext*0.6
				div1= operacion.pregunta.index(" ",15)
				div2= operacion.pregunta.index(" ",30)

				if div2 ==-1:
					div2= operacion.pregunta.index(" ",20)

				clean_pregunta= operacion.pregunta[:div1]
				self.WriteColor(clean_pregunta, xtext, ytext, textsize)	

				clean_pregunta= operacion.pregunta[(div1+1):div2]
				self.WriteColor(clean_pregunta, xtext, ytext+textsize, textsize)

				clean_pregunta= operacion.pregunta[(div2+1):]
				self.WriteColor(clean_pregunta, xtext, ytext+2*textsize, textsize)
				ytext= ytext+2*textsize


		textbox_x= int(self.width*0.05)
		textbox_y= ytext+self.height*0.02
		self.Objects.append(Textbox(textbox_x,textbox_y,int(self.width*0.8),int(self.height-textbox_y)))
		self.canvas.blit(self.Objects[0].screen(),(self.Objects[0].pos_x, self.Objects[0].pos_y ))

		pygame.display.flip()
		return

	def SetLayoutList(self,operacion):

		print"lista"
		self.TexttoSpeech(operacion.audio_pregunta)

		xtext= 0
		ytext= int(self.height*(1/8))

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

			ytext= int(self.height/2)

			textsize= self.GetSizeTextImg(len(operacion.pregunta))
		
		print "temp: "+str(temp)

		# Aquí se construyen las distintas lineas de la pregunta
		if len(operacion.pregunta)>0:

			# Si es que hay más de 2 lineas, entonces hay que escribir las oraciones más arriba
			if temp>=2:
				ytext= ytext*0.8
			
			# 1 sola linea
			if temp<=1:
				self.WriteColor(operacion.pregunta, xtext, ytext, textsize)	
				ytext= ytext+textsize

			# 2 lineas
			elif temp<=2:
				# define el divisor por espacio de caracter
				div= operacion.pregunta.index(" ",12)

				if div ==-1:
					div=operacion.pregunta.index(" ")

				start=0
				end= div

				clean_pregunta= operacion.pregunta[:div]
				textsize= self.GetSizeHorizontal(len(clean_pregunta))
				
				clean_pregunta2= operacion.pregunta[(div+1):]
				textsize2= self.GetSizeHorizontal(len(clean_pregunta2))

				textsize= min(textsize, textsize2)

				self.WriteColor(clean_pregunta, xtext, ytext, textsize)	
				self.WriteColor(clean_pregunta2, xtext, ytext+textsize, textsize)
				ytext= ytext+2*textsize

			# si tiene 3 lineas
			elif temp<=4:
				ytext= ytext*0.6
				# 12 es el numero adecuado de caracteres que se ve bien con 50 teclados
				div1= operacion.pregunta.index(" ",12)
				div2= operacion.pregunta.index(" ",div1+12)

				if div2 ==-1:
					div2= operacion.pregunta.index(" ",18)

				clean_pregunta= operacion.pregunta[:div1]
				textsize= self.GetSizeHorizontal(len(clean_pregunta))
				
				clean_pregunta2= operacion.pregunta[(div1+1):div2]
				textsize2= self.GetSizeHorizontal(len(clean_pregunta2))
				
				clean_pregunta3= operacion.pregunta[(div2+1):]
				textsize3= self.GetSizeHorizontal(len(clean_pregunta3))
				
				textsize = min(textsize, textsize2, textsize3)

				self.WriteColor(clean_pregunta, xtext, ytext, textsize)
				self.WriteColor(clean_pregunta2, xtext, ytext+textsize, textsize)
				self.WriteColor(clean_pregunta3, xtext, ytext+2*textsize, textsize)
				ytext= ytext+3*textsize

		

		listview_x= int(self.width*0.05)
		listview_y= ytext+self.height*0.02

		self.Objects.append(Listview(operacion.alternativas,listview_x,listview_y,int(self.width*0.8),int(self.height-listview_y)))
		self.canvas.blit(self.Objects[0].screen(),(self.Objects[0].pos_x, self.Objects[0].pos_y))



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

		if self.recien_pareado==True:
			print "matando primer audio"
			self.text_to_speech_queue.put({'tts': text_to_speech, 'terminate': True, 'tts_id': time.time()})
			#self.lib_play_proc.join()

		if self.lib_play_proc is None or self.recien_pareado==True:
			self.recien_pareado=False
			self.text_to_speech_queue = multiprocessing.Queue()
			self.lib_play_proc = multiprocessing.Process(target=audio_lib.play, args=(self.numero_audifono, self.text_to_speech_queue))
			self.lib_play_proc.start()          
		


		if len(text_to_speech)>0:

			self.speaking = True

			if "¿" in text_to_speech:
				text_to_speech= text_to_speech.replace("¿","")

			print "Reproduciendo en audifono #%s: \"%s\"" % (self.numero_audifono, text_to_speech)
			audio_lib.reproduciendo[int(self.numero_audifono)]=True
			print str(self.numero_audifono)+" "+str(audio_lib.reproduciendo[self.numero_audifono])
			self.text_to_speech_queue.put({'tts': text_to_speech, 'terminate': False, 'tts_id': time.time()})

			def EnableAudio():
				self.speaking=False

			# son 0.1 segundos por caracter, para que sea medio segundo aprox por palabra
			t = Timer(len(text_to_speech)*0.2,EnableAudio)
			t.start()


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

				logging.info("[%f: [%d, %s, %s] ], " % (time.time(), self.numero_audifono, 'Pareamiento', 'nombre: ' +nombre_caps))

				self.Operacion_actual= self.reglas_main.GetSiguienteOperacion(self.Operacion_actual, self.Alumno_actual)
				print "siguiente op"
				self.CreateGrid(self.Operacion_actual)
		

		elif self.pareado== False and self.nombre_ingresado==False:
			textctrl= self.Objects[0]
			print "largo: "+str(len(textctrl.Value))
			if text=="Enter" and len(textctrl.Value)>0:
				temp= int(textctrl.Value)
				print "temp:"+str(temp)
				if temp>=0 and temp< len(diccionario):

					for a in range(0,len(diccionario)):
						if(diccionario[a].numero_audifono== temp):
							num_aud= str(self.numero_audifono)
							diccionario[a].numero_audifono= int(num_aud)
							self.recien_pareado=True
							print "cambiado:"+str(temp)+" por:"+str(self.numero_audifono)
							print "diccionario:"+str(diccionario[a])
							print "teclado 1:"+str(diccionario[1].numero_audifono)
							print "teclado 1 preg:"+str(diccionario[1].Operacion_actual.audio_pregunta)
							diccionario[a].recien_pareado=True
							#diccionario[a].TexttoSpeech("apagando")

					self.numero_audifono=temp
					self.pareado=True
					self.recien_pareado=True
					self.lib_play_proc=None
					self.set_nombre()
					
		# reconocimiento de backspace para borrado
		
		if self.pareado==False:
			if text=="0" or text=="1" or text=="2" or text=="3" or text=="4" or text=="5" or text=="6" or text=="7" or text=="8" or text=="9" or text=="Back":
				self.Objects[0].react(text)
				self.canvas.blit(self.Objects[0].screen(),(self.Objects[0].pos_x, self.Objects[0].pos_y ))
		else:
			self.Objects[0].react(text)
			self.canvas.blit(self.Objects[0].screen(),(self.Objects[0].pos_x, self.Objects[0].pos_y ))
		
	



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
					#print "Respuesta"
					#print  listview.answer()
					#print self.Operacion_actual.respuesta
					if listview.answer() == self.Operacion_actual.respuesta:
						logging.info("[%f: [%d, %s, %s, %s, %s] ], " % (time.time(), self.numero_audifono, 'Respuesta Correcta', 'pregunta: '+self.Operacion_actual.pregunta,'audio_preg: '	+self.Operacion_actual.audio_pregunta , 'respuesta: '+self.Operacion_actual.respuesta))
						self.TexttoSpeech(self.Operacion_actual.feedback_correcto.decode('utf8'))
						self.Operacion_actual.RespuestaCorrecta()
					else:
						logging.info("[%f: [%d, %s, %s, %s, %s, %s] ], " % (time.time(), self.numero_audifono, 'Respuesta Incorrecta', 'pregunta: '+self.Operacion_actual.pregunta,'audio_preg: '	+self.Operacion_actual.audio_pregunta , 'resp_alum: '+listview.answer() ,'respuesta: '+self.Operacion_actual.respuesta))
						self.TexttoSpeech(self.Operacion_actual.feedback_error.decode('utf8'))
						self.Operacion_actual.RespuestaIncorrecta()

					
			else:

				textctrl= self.Objects[0]
						
				if textctrl.Value == self.Operacion_actual.respuesta:
					#print u"feedback: "+self.Operacion_actual.feedback_correcto
					logging.info("[%f: [%d, %s, %s, %s, %s] ], " % (time.time(), self.numero_audifono, 'Respuesta Correcta', 'pregunta: '+self.Operacion_actual.pregunta,'audio_preg: '	+self.Operacion_actual.audio_pregunta , 'respuesta: '+self.Operacion_actual.respuesta))
					self.TexttoSpeech(self.Operacion_actual.feedback_correcto.decode('utf8'))
					self.Operacion_actual.RespuestaCorrecta()
					textctrl.Value=""
				else:
					logging.info("[%f: [%d, %s, %s, %s, %s, %s] ], " % (time.time(), self.numero_audifono, 'Respuesta Incorrecta', 'pregunta: '+self.Operacion_actual.pregunta,'audio_preg: '	+self.Operacion_actual.audio_pregunta , 'resp_alum: '+textctrl.Value ,'respuesta: '+self.Operacion_actual.respuesta))
					self.TexttoSpeech(self.Operacion_actual.feedback_error.decode('utf8'))
					self.Operacion_actual.RespuestaIncorrecta()
					textctrl.Value=""
			
			self.Operacion_actual= self.reglas_main.GetSiguienteOperacion(self.Operacion_actual, self.Alumno_actual)
			self.CreateGrid(self.Operacion_actual)
		
		self.Objects[0].react(text)
		self.canvas.blit(self.Objects[0].screen(),(self.Objects[0].pos_x, self.Objects[0].pos_y ))
		#except Exception, e:
		#	print "result is:"+ str(e)



	def RepetirPregunta(self):
		#print "Repetir pregunta"
		#print self.Operacion_actual.audio_pregunta
		logging.info("[%f: [%d, %s, %s] ], " % (time.time(), self.numero_audifono, 'Repetir pregunta', 'audio_preg: '	+self.Operacion_actual.audio_pregunta))
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

		return int(1.5 * self.width/x)

		if x<6:
			x=8

		if x==0:
			return int(1.5 * self.width)
		if x>30:
			return int(2.8*self.width/x)
		elif x>20:
			return int(2.5*self.width/x)
		elif x>15:
			return int(2 * self.width/x)
		else:
			return int(1.8 * self.width/x)

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





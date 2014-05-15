#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
from Prueba_clases.clases import *
from Prueba_clases.ejercicio import *
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
import lector_csv

logging.basicConfig(filename='multik.log',level=logging.INFO)

class Pareamiento:

	def __init__(self, pos_x, pos_y, width, height):

		print "pareamiento"
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
		self.recien_pareado= False

		#TO-DO Cambiar nombre curso mas user-friendly
		#self.numero_alumno = lector_csv.obtener_lista("3A")
		#self.numero_alumno = lector_csv.obtener_lista("3B")
		#self.numero_alumno = lector_csv.obtener_lista("3C")
		self.numero_alumno = lector_csv.obtener_lista("3B")
		self.parear()

	def react(self,input):

		self.Objects[0].react(input)

	def screen(self):
		return self.canvas

	def ResetLayout(self):
		self.canvas.fill(self.whiteColor)
		self.Objects= []

	def Write(self, pregunta, xtext, ytext, textsize):

		pygame.font.init()
		self.myfont = pygame.font.SysFont("monospace", textsize)
		label = self.myfont.render(pregunta, 1, (0,0,0))
		self.canvas.blit(label,(xtext, ytext))

		return



		##########  PAREAMIENTO ##############
	

	def parear(self):

		self.ResetLayout()
		
		frase = u"Escribe el número..."
		size= int(1.5 * self.width/len(frase))		
		self.Write(frase, 0, 0, size)

		textbox_x= int(self.width*0.05)
		textbox_y= size+self.height*0.2

		height_textbox= int(self.height-textbox_y)

		if height_textbox > int(self.height*0.3):
			height_textbox= int(self.height*0.3)

		self.Objects.append(Textbox(textbox_x,textbox_y,int(self.width*0.8),height_textbox))
		self.canvas.blit(self.Objects[0].screen(),(self.Objects[0].pos_x, self.Objects[0].pos_y ))


	def ModificarPareamiento(self, Alumno ,Audio, earg):
		
		text= str(earg['char']).decode('utf-8')
		id_teclado = earg['id']
		
		if self.pareado== True and self.nombre_ingresado==False:
			textctrl= self.Objects[0]
			if text=="Enter" and len(textctrl.Value)>0:
				# Buscamos el numero de lista en el CSV del curso
				temp_numero= textctrl.Value
				#Variable nombre_caps por legacy
				if temp_numero in self.numero_alumno:
					nombre_caps = self.numero_alumno[temp_numero]
					Alumno.Nombre= self.numero_alumno[temp_numero]
					# Identificamos al alumno asi para manejar persistencia y evitar choques de nombre
					Alumno.nro_lista = temp_numero
					self.nombre_ingresado=True

					logging.info("[%f: [%d, %d, %s, %s] ], " % (time.time(), self.numero_audifono, id_teclado, 'PAREAMIENTO', temp_numero))
				else:
					self.set_nombre()

		elif self.pareado== False and self.nombre_ingresado==False:
			textctrl= self.Objects[0]
			print "largo: "+str(len(textctrl.Value))
			if text=="Enter" and len(textctrl.Value)>0:
				value= int(textctrl.Value)
				print "value:"+str(value)
				if value>=0 and value< len(Audio):
					print "dentro de márgenes"
					if Audio[Alumno.Id] is None:
						if value not in Audio:
							Audio[Alumno.Id]= value					
							self.numero_audifono=value
							self.pareado=True
							self.recien_pareado=True
							self.set_nombre()
				else:
					textctrl.value=""
					
		# reconocimiento de backspace para borrado
		print "pareado:"+str(self.pareado)
		if self.pareado==False:
			if text=="0" or text=="1" or text=="2" or text=="3" or text=="4" or text=="5" or text=="6" or text=="7" or text=="8" or text=="9" or text=="Back":
				self.Objects[0].react(text)
				self.canvas.blit(self.Objects[0].screen(),(self.Objects[0].pos_x, self.Objects[0].pos_y ))
		else:
			self.Objects[0].react(text)
			self.canvas.blit(self.Objects[0].screen(),(self.Objects[0].pos_x, self.Objects[0].pos_y ))

	
	#def set_mensaje

	def set_nombre(self):
		
		self.ResetLayout()
		
		frase = u"Ingresa tu número de lista"
		size= int(1.5 * self.width/len(frase))		
		self.Write(frase, 0, 0, size)

		# Textbox que pregunta nombre
		self.Objects.append(Textbox(int(self.width*0.05),int(self.height/4),int(self.width*0.9),int(size*6)))
		self.canvas.blit(self.Objects[0].screen(),(self.Objects[0].pos_x, self.Objects[0].pos_y))

	

# coding: utf-8
import pygame
import random
from Alumno import *
from clases import *

class ejercicio:
	def __init__(self, alumnos, pos_x, pos_y, width, height):
		self.teclados = []
		for i in range(len(alumnos)):
			self.teclados.append(alumnos[i].id)
		self.pos_x = pos_x
		self.pos_y = pos_y
		self.redColor = pygame.Color(255,0,0)
		self.greenColor = pygame.Color(0,255,0)
		self.blueColor = pygame.Color(0,0,255)
		self.whiteColor = pygame.Color(255,255,255)
		self.blackColor = pygame.Color(0,0,0)
		self.width = width
		self.height = height
		self.canvas = pygame.Surface((self.width,self.height))
		self.canvas.fill(self.blackColor)
		pygame.draw.rect(self.canvas,self.whiteColor,(1, 1, self.width - 2,  self.height - 2))
		
		self.inputs = []
		
		#self.finished = False
		
	def screen(self):
		return self.canvas

	def react(self,id,input):
		return
	
	def get_audio_text(self):
		return ""
	
	def get_color(self, id):
		if id == 0:
			return self.redColor
		elif id == 1:
			return self.greenColor
		elif id == 2:
			return self.blueColor
		return self.blackColor
		
	def next(self):
		return ejercicio0(self.alumnos, self.pos_x, self.pos_y, self.width, self.height)
	
	def finished(self):
		return True

	def correct(self):
		return True

class ejercicio0(ejercicio):
	def __init__(self, alumnos, pos_x, pos_y, width, height):
		self.teclados = []
		for i in range(len(alumnos)):
			self.teclados.append(alumnos[i].id)
		self.alumnos = alumnos
		self.pos_x = pos_x
		self.pos_y = pos_y
		self.redColor = pygame.Color(255,0,0)
		self.greenColor = pygame.Color(0,255,0)
		self.blueColor = pygame.Color(0,0,255)
		self.whiteColor = pygame.Color(255,255,255)
		self.blackColor = pygame.Color(0,0,0)
		self.width = width
		self.height = height
		self.canvas = pygame.Surface((self.width,self.height))
		self.canvas.fill(self.blackColor)
		pygame.draw.rect(self.canvas,self.whiteColor,(1, self.height / 4, self.width - 2,  3 * self.height / 4 - 2))
		
		self.inputs = []
		
		#self.finished = False

		self.blocked = [False, False, False]

		pygame.font.init()
		self.myfont = pygame.font.SysFont("monospace", self.height / 4)
		labels = []
		labels.append(self.myfont.render("Grupo %d" % alumnos[0].grupo, 1, self.whiteColor))
		labels.append(self.myfont.render(alumnos[0].name, 1, self.redColor))
		labels.append(self.myfont.render(alumnos[1].name, 1, self.greenColor))
		labels.append(self.myfont.render(alumnos[2].name, 1, self.blueColor))

		for i in range(len(labels)):
			self.canvas.blit(labels[i], (2, self.height / len(labels) * i))
		
	def react(self,id,input):
		if input == "Enter":#El alumno indica que ya encontro su nombre y grupo
			index_teclado = self.teclados.index(id)
			self.blocked[index_teclado] = not self.blocked[index_teclado]
			#if False not in self.blocked:
				#self.finished = True
			if self.blocked[index_teclado]:
				print "Bloqueado alumno"
				pygame.draw.rect(self.canvas,self.get_color(index_teclado),(1, self.height / 4 * (1 + index_teclado), self.width - 2,  self.height / 4 - 2))
				label = self.myfont.render(self.alumnos[index_teclado].name, 1, self.whiteColor)
				self.canvas.blit(label, (2, self.height / 4 * (1 + index_teclado)))
			else:
				pygame.draw.rect(self.canvas,self.whiteColor,(1, self.height / 4 * (1 + index_teclado), self.width - 2,  self.height / 4 - 2))
				label = self.myfont.render(self.alumnos[index_teclado].name, 1, self.get_color(index_teclado))
				self.canvas.blit(label, (2, self.height / 4 * (1 + index_teclado)))
		return
		
	def get_audio_text(self):
		return "Busca tu grupo y nombre y presiona enter"

	def finished(self):
		if self.blocked[0] and self.blocked[1] and self.blocked[2]:
			print "Finished"
			return True
		else:
			print "Not Finished"
			return False

	def next(self):
		return ejercicio1(self.alumnos, self.pos_x,self.pos_y, self.width, self.height)

class ejercicioAlternativas(ejercicio):
	def __init__(self, alumnos, pos_x, pos_y, width, height, preguntaC):
		self.teclados = []
		for i in range(len(alumnos)):
			self.teclados.append(alumnos[i].id)
		self.pos_x = pos_x
		self.pos_y = pos_y
		self.whiteColor = pygame.Color(255,255,255)
		self.blackColor = pygame.Color(0,0,0)
		self.width = width
		self.height = height
		self.canvas = pygame.Surface((self.width,self.height))
		self.canvas.fill(self.blackColor)
		pygame.draw.rect(self.canvas,self.whiteColor,(1, 1, self.width - 2,  self.height - 2))
		
		pygame.font.init()
		
		self.pregunta = preguntaC
		
		self.inputs = []
		#self.xs = []
		self.ys = []
		self.blocked = []
		
		for i in range(len(alumnos)):
			self.ys[i] = random.randint(0, len(preguntaC.alternativas)-1)
			self.inputs[i] = self.pregunta.alternativas[self.ys[i]]
			self.blocked[i] = False
			
		self.top_limit = 0
		if len(self.preguntaC.preguntas) > 0:
			self.top_limit = self.height / (len(preguntaC.alternativas) + 1)
			texto_pregunta = self.preguntaC.preguntas[0]
			myfont = pygame.font.SysFont("monospace", self.top_limit - 4)
			label_pregunta = self.myfont.render(texto_pregunta, 1, self.blackColor)
			size_multiplier = 100
			while label_pregunta.width > (self.width - 4) or label_pregunta.height > (self.top_limit - 4):
				size_multiplier -= 10
				myfont = pygame.font.SysFont("monospace", ((self.top_limit - 4) * 100) / size_multiplier)
				label_pregunta = self.myfont.render(texto_pregunta, 1, self.blackColor)
			self.canvas.blit(label_pregunta, (self.width / 2 - label_pregunta.width / 2, self.height / 2 - label_pregunta.height / 2))
		
		self.draw_rectangles()
		self.finished = False
		
	def draw_rectangles(self):
		rect_height = (self.height - self.top_limit) / len(self.preguntaC.alternativas)
		for i in range(len(alumnos)):
			delta = 2 * (i + 1)
			pygame.draw.rect(self.canvas,self.get_color(i),(delta, self.top_limit + delta + rect_height * self.ys[i], self.width - 2 * delta,  rect_height - 2 * delta))
			if not self.blocked[i]:
				pygame.draw.rect(self.canvas,self.whiteColor,(delta + 2, self.top_limit + delta + rect_height * self.ys[i] + 2, self.width - 2 * delta - 4,  rect_height - 2 * delta - 4))
			else:
				pygame.draw.rect(self.canvas,self.whiteColor,(delta + 4, self.top_limit + delta + rect_height * self.ys[i] + 4, self.width - 2 * delta - 8,  rect_height - 2 * delta - 8))
		word_width = self.width - 14
		word_height = rect_height - 14
		for i in range(len(self.preguntaC.alternativas)):
			myfont = pygame.font.SysFont("monospace", word_height)
			label_alternativa = self.myfont.render(self.preguntaC.alternativas[i], 1, self.blackColor)
			size_multiplier = 100
			while label_alternativa.width > word_width or label_alternativa.height > word_height:
				size_multiplier -= 10
				myfont = pygame.font.SysFont("monospace", (100 * word_height) / size_multiplier)
	
	def erase_rectangles(self):
		pygame.draw.rect(self.canvas,self.whiteColor,(2, self.top_limit + 1, self.width - 4,  self.height -  self.top_limit - 4))
		
	def react(self, id, input):
		index_teclado = self.teclados.index(id)
		if input == "Enter":
			self.blocked[index_teclado] = not self.blocked[index_teclado]
			self.finished = False not in self.blocked
			self.erase_rectangles()
			self.draw_rectangles()
		elif not self.blocked[index_teclado]:
			self.erase_rectangles()
			if input == "-^":
				if self.ys[index_teclado] == 0:
					self.ys[index_teclado] = len(self.preguntaC.alternativas) - 1
				else:
					self.ys[index_teclado] -= 1
			elif input == "-v":
				self.ys[index_teclado] = (self.ys[index_teclado] + 1)%len(self.preguntaC.alternativas)
			self.draw_rectangles()
			
		self.inputs[index_teclado] = self.preguntaC.alternativas[self.ys[index_teclado]]
	
class ejercicioTexto(ejercicio):	
	def __init__(self, alumnos, pos_x, pos_y, width, height, preguntaC):
		self.teclados = []
		for i in range(len(alumnos)):
			self.teclados.append(alumnos[i].id)
		self.pos_x = pos_x
		self.pos_y = pos_y
		self.whiteColor = pygame.Color(255,255,255)
		self.blackColor = pygame.Color(0,0,0)
		self.width = width
		self.height = height
		self.canvas = pygame.Surface((self.width,self.height))
		self.canvas.fill(self.blackColor)
		pygame.draw.rect(self.canvas,self.whiteColor,(1, 1, self.width - 2,  self.height - 2))
		
		pygame.font.init()
		
		self.pregunta = preguntaC
		self.inputs = []
		self.blocked = []
		
		for i in range(len(alumnos)):
			self.inputs[i] = ""
			self.blocked[i] = False
			
		self.top_limit = 0
		if len(self.preguntaC.preguntas) > 0:
			self.top_limit = self.height / (len(self.teclados))
			texto_pregunta = self.preguntaC.preguntas[0]
			myfont = pygame.font.SysFont("monospace", self.top_limit - 4)
			label_pregunta = self.myfont.render(texto_pregunta, 1, self.blackColor)
			size_multiplier = 100
			while label_pregunta.width > (self.width - 4) or label_pregunta.height > (self.top_limit - 4):
				size_multiplier -= 10
				myfont = pygame.font.SysFont("monospace", ((self.top_limit - 4) * 100) / size_multiplier)
				label_pregunta = self.myfont.render(texto_pregunta, 1, self.blackColor)
			self.canvas.blit(label_pregunta, (self.width / 2 - label_pregunta.width / 2, self.height / 2 - label_pregunta.height / 2))
		
		self.textBoxs = []
		
		textHeight = ((self.height - 2) - self.top_limit) / len(self.alumnos)
		textWidth = self.width - 6
		
		for i in range(len(self.alumnos)):
			pos_y = self.top_limit + 2 + i * textHeight
			self.textBoxs[i] = Textbox(3, pos_y, textWidth, textHeight - 2, self.self.get_color(i))
			self.canvas.blit(self.textBoxs[i],(pos_y, 3))
		self.finished = False
		
	def react(self, id, input):
		index_teclado = self.teclados.index(id)
		self.textBoxs[index_teclado].react(input)
		self.blocked[index_teclado] = self.textBoxs[index_teclado].blocked
		
		self.inputs[index_teclado] = self.textBoxs[index_teclado].Value
		
		self.finished = False not in self.blocked
		
		self.canvas.blit(self.textBoxs[index_teclado],(self.textBoxs[index_teclado].pos_y, 3))
		
	
	
class ejercicio1(ejercicio):
	def __init__(self, alumnos, pos_x, pos_y, width, height):
		self.alumnos = alumnos
		self.teclados = []
		for i in range(len(alumnos)):
			self.teclados.append(alumnos[i].id)
		self.pos_x = pos_x
		self.pos_y = pos_y
		self.redColor = pygame.Color(255,0,0)
		self.greenColor = pygame.Color(0,255,0)
		self.blueColor = pygame.Color(0,0,255)
		self.whiteColor = pygame.Color(255,255,255)
		self.blackColor = pygame.Color(0,0,0)
		self.width = width
		self.height = height
		self.canvas = pygame.Surface((self.width,self.height))
		self.canvas.fill(self.blackColor)
		pygame.draw.rect(self.canvas,self.whiteColor,(1, 1, self.width - 2,  self.height - 2))
		
		#self.finished = False
		
		#Sector especifico para el inicio
		
		self.inputs = ['', '', '']

		self.blocked = [False, False, False]
		
		pygame.draw.rect(self.canvas,self.redColor,(self.width / 5, self.height / 7, 3 * self.width / 5,  self.height / 7))
		pygame.draw.rect(self.canvas,self.greenColor,(self.width / 5, 3 * self.height / 7, 3 * self.width / 5,  self.height / 7))
		pygame.draw.rect(self.canvas,self.blueColor,(self.width / 5, 5 * self.height / 7, 3 * self.width / 5,  self.height / 7))
		
		pygame.font.init()
		
		self.myfont = pygame.font.SysFont("monospace", self.height / 7)
		label1 = self.myfont.render(self.inputs[0], 1, (255,255,255))
		self.canvas.blit(label1,(self.width / 5, self.height / 7))
		label2 = self.myfont.render(self.inputs[1], 1, (255,255,255))
		self.canvas.blit(label2,(self.width / 5, 3 * self.height / 7))
		label3 = self.myfont.render(self.inputs[2], 1, (255,255,255))
		self.canvas.blit(label3,(self.width / 5, 5 * self.height / 7))
		return

	def react(self,id,input):
		index_teclado = self.teclados.index(id)
		if input == "Enter":
			self.blocked[index_teclado] = not self.blocked[index_teclado]
			#if self.blocked[0] and self.blocked[1] and self.blocked[2]:
				#self.finished = True
			#else:
			if self.blocked[index_teclado]:
				pygame.draw.rect(self.canvas,self.whiteColor,(self.width / 5 + 3, (2 * index_teclado + 1) * self.height / 7 + 3, 3 * self.width / 5 - 6,  self.height / 7 - 6))
				self.myfont = pygame.font.SysFont("monospace", self.height / 7)
				label = self.myfont.render(self.inputs[index_teclado], 1, (0,0,0))
				self.canvas.blit(label,(self.width / 5, (2 * index_teclado + 1) * self.height / 7))
			else:
				if index_teclado == 0:
					pygame.draw.rect(self.canvas,self.redColor,(self.width / 5, self.height / 7, 3 * self.width / 5,  self.height / 7))
				elif index_teclado == 1:
					pygame.draw.rect(self.canvas,self.greenColor,(self.width / 5, 3 * self.height / 7, 3 * self.width / 5,  self.height / 7))
				else:
					pygame.draw.rect(self.canvas,self.blueColor,(self.width / 5, 5 * self.height / 7, 3 * self.width / 5,  self.height / 7))
				self.myfont = pygame.font.SysFont("monospace", self.height / 7)
				label = self.myfont.render(self.inputs[index_teclado], 1, (255,255,255))
				self.canvas.blit(label,(self.width / 5, (2 * index_teclado + 1) * self.height / 7))
		elif not self.blocked[index_teclado]:
			if len(input) == 1:
				self.inputs[index_teclado] = self.inputs[index_teclado] + input
				self.myfont = pygame.font.SysFont("monospace", self.height / 7)
				label = self.myfont.render(self.inputs[index_teclado], 1, (255,255,255))
				self.canvas.blit(label,(self.width / 5, (2 * index_teclado + 1) * self.height / 7))
			elif input == "Back":
				if len(self.inputs[index_teclado]) > 0:
					if index_teclado == 0:
						pygame.draw.rect(self.canvas,self.redColor,(self.width / 5, self.height / 7, 3 * self.width / 5,  self.height / 7))
					elif index_teclado == 1:
						pygame.draw.rect(self.canvas,self.greenColor,(self.width / 5, 3 * self.height / 7, 3 * self.width / 5,  self.height / 7))
					else:
						pygame.draw.rect(self.canvas,self.blueColor,(self.width / 5, 5 * self.height / 7, 3 * self.width / 5,  self.height / 7))
					self.inputs[index_teclado] = self.inputs[index_teclado][:-1]
					self.myfont = pygame.font.SysFont("monospace", self.height / 7)
					label = self.myfont.render(self.inputs[index_teclado], 1, (255,255,255))
					self.canvas.blit(label,(self.width / 5, (2 * index_teclado + 1) * self.height / 7))
		return

	def finished(self):
		if self.blocked[0] and self.blocked[1] and self.blocked[2]:
			return True
		return False

class ejercicio2(ejercicio):
	def __init__(self, alumnos, pos_x, pos_y, width, height):
		self.alumnos = alumnos
		self.teclados = []
		for i in range(len(alumnos)):
			self.teclados.append(alumnos[i].id)
		self.pos_x = pos_x
		self.pos_y = pos_y
		self.redColor = pygame.Color(255,0,0)
		self.greenColor = pygame.Color(0,255,0)
		self.blueColor = pygame.Color(0,0,255)
		self.whiteColor = pygame.Color(255,255,255)
		self.blackColor = pygame.Color(0,0,0)
		self.width = width
		self.height = height
		self.canvas = pygame.Surface((self.width,self.height))
		self.canvas.fill(self.blackColor)
		pygame.draw.rect(self.canvas,self.whiteColor,(1, 1, self.width - 2,  self.height - 2))
		
		self.inputs = []
		
		self.finished = False
		
		#Sector especifico para el inicio
		
		self.xs = [0, 0, 0]
		self.ys = [0, 0, 0]

		self.blocked = [False, False, False]
		
		image_1 = pygame.image.load("Images/pato.png")
		image_1 = pygame.transform.scale(image_1,(self.width  / 5,self.height / 5))
		self.canvas.blit(image_1,(self.width/5,self.height/5))
		
		image_2 = pygame.image.load("Images/pelota.png")
		image_2 = pygame.transform.scale(image_2,(self.width/5,self.height/5))
		self.canvas.blit(image_2,(3*self.width/5,self.height/5))
		
		image_3 = pygame.image.load("Images/perro.png")
		image_3 = pygame.transform.scale(image_3,(self.width/5,self.height/5))
		self.canvas.blit(image_3,(self.width/5,3*self.height/5))
		
		image_4 = pygame.image.load("Images/casa.png")
		image_4 = pygame.transform.scale(image_4,(self.width/5,self.height/5))
		self.canvas.blit(image_4,(3*self.width/5,3*self.height/5))
		
		myfont = pygame.font.SysFont("monospace", self.height / 10)
		
		label_1 = myfont.render("pato",1,(0,0,0))
		label_2 = myfont.render("pelota",1,(0,0,0))
		label_3 = myfont.render("perro",1,(0,0,0))
		label_4 = myfont.render("casa",1,(0,0,0))
		
		self.canvas.blit(label_1,(self.width/5, 2*self.height/5))
		self.canvas.blit(label_2,(3*self.width/5,2*self.height/5))
		self.canvas.blit(label_3,(self.width/5,4*self.height/5))
		self.canvas.blit(label_4,(3*self.width/5,4*self.height/5))
		
		self.radio = min(self.width / 40, self.height / 40) / 2
		
		self.paint_circles(0)
		self.paint_circles(1)
		self.paint_circles(2)
		

		return
		
	def paint_circles(self, id):
		if id == 0: #Patron :  :
			pygame.draw.circle(self.canvas, self.redColor,((self.xs[0] * 2 + 1) * self.width / 5 - self.radio, (self.ys[0] * 2 + 1) * self.height / 5 - self.radio), 2 * self.radio, 0)
			pygame.draw.circle(self.canvas, self.redColor,((self.xs[0] * 2 + 2) * self.width / 5 - self.radio, (self.ys[0] * 2 + 1) * self.height / 5 - self.radio), 2 * self.radio, 0)
			pygame.draw.circle(self.canvas, self.redColor,((self.xs[0] * 2 + 2) * self.width / 5 - self.radio, (self.ys[0] * 2 + 2) * self.height / 5 - self.radio), 2 * self.radio, 0)
			pygame.draw.circle(self.canvas, self.redColor,((self.xs[0] * 2 + 1) * self.width / 5 - self.radio, (self.ys[0] * 2 + 2) * self.height / 5 - self.radio), 2 * self.radio, 0)
			
		elif id == 1: # patron ' : '
			pygame.draw.circle(self.canvas, self.greenColor,((self.xs[1] * 4 + 3) * self.width / 10 - self.radio, (self.ys[1] * 2 + 1) * self.height / 5 - self.radio), 2 * self.radio, 0)
			pygame.draw.circle(self.canvas, self.greenColor,((self.xs[1] * 4 + 3) * self.width / 10 - self.radio, (self.ys[1] * 2 + 2) * self.height / 5 - self.radio), 2 * self.radio, 0)
			pygame.draw.circle(self.canvas, self.greenColor,((self.xs[1] * 2 + 1) * self.width / 5 - self.radio, (self.ys[1] * 4 + 3) * self.height / 10 - self.radio), 2 * self.radio, 0)
			pygame.draw.circle(self.canvas, self.greenColor,((self.xs[1] * 2 + 2) * self.width / 5 - self.radio, (self.ys[1] * 4 + 3) * self.height / 10 - self.radio), 2 * self.radio, 0)
		
		elif id == 2: #patron  :: 
			pygame.draw.circle(self.canvas, self.blueColor,(((self.xs[2] * 8 + 5) * self.width) / 20 - self.radio, (self.ys[2] * 2 + 1) * self.height / 5 - self.radio), 2 * self.radio, 0)
			pygame.draw.circle(self.canvas, self.blueColor,((self.xs[2] * 8 + 7) * self.width / 20 - self.radio, (self.ys[2] * 2 + 1) * self.height / 5 - self.radio), 2 * self.radio, 0)
			pygame.draw.circle(self.canvas, self.blueColor,((self.xs[2] * 8 + 5) * self.width / 20 - self.radio, (self.ys[2] * 2 + 2) * self.height / 5 - self.radio), 2 * self.radio, 0)
			pygame.draw.circle(self.canvas, self.blueColor,((self.xs[2] * 8 + 7) * self.width / 20 - self.radio, (self.ys[2] * 2 + 2) * self.height / 5 - self.radio), 2 * self.radio, 0)
		
		return

	def paint_blocked_circles(self, id):
	
		if id == 0: #Patron :  :
			pygame.draw.circle(self.canvas, self.redColor,((self.xs[0] * 2 + 1) * self.width / 5 - self.radio, (self.ys[0] * 2 + 1) * self.height / 5 - self.radio), 2 * self.radio, 2)
			pygame.draw.circle(self.canvas, self.redColor,((self.xs[0] * 2 + 2) * self.width / 5 - self.radio, (self.ys[0] * 2 + 1) * self.height / 5 - self.radio), 2 * self.radio, 2)
			pygame.draw.circle(self.canvas, self.redColor,((self.xs[0] * 2 + 2) * self.width / 5 - self.radio, (self.ys[0] * 2 + 2) * self.height / 5 - self.radio), 2 * self.radio, 2)
			pygame.draw.circle(self.canvas, self.redColor,((self.xs[0] * 2 + 1) * self.width / 5 - self.radio, (self.ys[0] * 2 + 2) * self.height / 5 - self.radio), 2 * self.radio, 2)
			
		elif id == 1: # patron ' : '
			pygame.draw.circle(self.canvas, self.greenColor,((self.xs[1] * 4 + 3) * self.width / 10 - self.radio, (self.ys[1] * 2 + 1) * self.height / 5 - self.radio), 2 * self.radio, 2)
			pygame.draw.circle(self.canvas, self.greenColor,((self.xs[1] * 4 + 3) * self.width / 10 - self.radio, (self.ys[1] * 2 + 2) * self.height / 5 - self.radio), 2 * self.radio, 2)
			pygame.draw.circle(self.canvas, self.greenColor,((self.xs[1] * 2 + 1) * self.width / 5 - self.radio, (self.ys[1] * 4 + 3) * self.height / 10 - self.radio), 2 * self.radio, 2)
			pygame.draw.circle(self.canvas, self.greenColor,((self.xs[1] * 2 + 2) * self.width / 5 - self.radio, (self.ys[1] * 4 + 3) * self.height / 10 - self.radio), 2 * self.radio, 2)
		
		elif id == 2: #patron  :: 
			pygame.draw.circle(self.canvas, self.blueColor,(((self.xs[2] * 8 + 5) * self.width) / 20 - self.radio, (self.ys[2] * 2 + 1) * self.height / 5 - self.radio), 2 * self.radio, 2)
			pygame.draw.circle(self.canvas, self.blueColor,((self.xs[2] * 8 + 7) * self.width / 20 - self.radio, (self.ys[2] * 2 + 1) * self.height / 5 - self.radio), 2 * self.radio, 2)
			pygame.draw.circle(self.canvas, self.blueColor,((self.xs[2] * 8 + 5) * self.width / 20 - self.radio, (self.ys[2] * 2 + 2) * self.height / 5 - self.radio), 2 * self.radio, 2)
			pygame.draw.circle(self.canvas, self.blueColor,((self.xs[2] * 8 + 7) * self.width / 20 - self.radio, (self.ys[2] * 2 + 2) * self.height / 5 - self.radio), 2 * self.radio, 2)
			
		return
		
	def erase_circles(self, id):
		if id == 0: #Patron :  :
			pygame.draw.circle(self.canvas, self.whiteColor,((self.xs[0] * 2 + 1) * self.width / 5 - self.radio, (self.ys[0] * 2 + 1) * self.height / 5 - self.radio), 2 * self.radio, 0)
			pygame.draw.circle(self.canvas, self.whiteColor,((self.xs[0] * 2 + 2) * self.width / 5 - self.radio, (self.ys[0] * 2 + 1) * self.height / 5 - self.radio), 2 * self.radio, 0)
			pygame.draw.circle(self.canvas, self.whiteColor,((self.xs[0] * 2 + 2) * self.width / 5 - self.radio, (self.ys[0] * 2 + 2) * self.height / 5 - self.radio), 2 * self.radio, 0)
			pygame.draw.circle(self.canvas, self.whiteColor,((self.xs[0] * 2 + 1) * self.width / 5 - self.radio, (self.ys[0] * 2 + 2) * self.height / 5 - self.radio), 2 * self.radio, 0)
			
		elif id == 1: # patron ' : '
			pygame.draw.circle(self.canvas, self.whiteColor,((self.xs[1] * 4 + 3) * self.width / 10 - self.radio, (self.ys[1] * 2 + 1) * self.height / 5 - self.radio), 2 * self.radio, 0)
			pygame.draw.circle(self.canvas, self.whiteColor,((self.xs[1] * 4 + 3) * self.width / 10 - self.radio, (self.ys[1] * 2 + 2) * self.height / 5 - self.radio), 2 * self.radio, 0)
			pygame.draw.circle(self.canvas, self.whiteColor,((self.xs[1] * 2 + 1) * self.width / 5 - self.radio, (self.ys[1] * 4 + 3) * self.height / 10 - self.radio), 2 * self.radio, 0)
			pygame.draw.circle(self.canvas, self.whiteColor,((self.xs[1] * 2 + 2) * self.width / 5 - self.radio, (self.ys[1] * 4 + 3) * self.height / 10 - self.radio), 2 * self.radio, 0)
		
		elif id == 2: #patron  :: 
			pygame.draw.circle(self.canvas, self.whiteColor,(((self.xs[2] * 8 + 5) * self.width) / 20 - self.radio, (self.ys[2] * 2 + 1) * self.height / 5 - self.radio), 2 * self.radio, 0)
			pygame.draw.circle(self.canvas, self.whiteColor,((self.xs[2] * 8 + 7) * self.width / 20 - self.radio, (self.ys[2] * 2 + 1) * self.height / 5 - self.radio), 2 * self.radio, 0)
			pygame.draw.circle(self.canvas, self.whiteColor,((self.xs[2] * 8 + 5) * self.width / 20 - self.radio, (self.ys[2] * 2 + 2) * self.height / 5 - self.radio), 2 * self.radio, 0)
			pygame.draw.circle(self.canvas, self.whiteColor,((self.xs[2] * 8 + 7) * self.width / 20 - self.radio, (self.ys[2] * 2 + 2) * self.height / 5 - self.radio), 2 * self.radio, 0)
		
		return
	
	def react(self, id, input):
		index_teclado = self.teclados.index(id)
		if input == "Enter":
			self.blocked[index_teclado] = not self.blocked[index_teclado]
			if self.blocked[0] and self.blocked[1] and self.blocked[2]:
				self.finished = True
			else:
				if self.blocked[index_teclado]:
					self.erase_circles(index_teclado)
					self.paint_blocked_circles(index_teclado)
				else:
					self.paint_circles(index_teclado)
		elif not self.blocked[index_teclado]:
			self.erase_circles(index_teclado)
			if input == "-^":
				if self.ys[index_teclado] == 0:
					self.ys[index_teclado] = 1
				else:
					self.ys[index_teclado] = 0
			elif input == "-v":
				self.ys[index_teclado] = (self.ys[index_teclado] + 1)%2
			elif input == "<-":
				if self.xs[index_teclado] == 0:
					self.xs[index_teclado] = 1
				else:
					self.xs[index_teclado] = 0
			elif input == "->":
				self.xs[index_teclado] = (self.xs[index_teclado] + 1)%2
			self.paint_circles(index_teclado)
		return

class ejercicio3(ejercicio):
	def __init__(self, alumnos, pos_x, pos_y, width, height):
		self.alumnos = alumnos
		self.teclados = []
		for i in range(len(alumnos)):
			self.teclados.append(alumnos[i].id)
		self.pos_x = pos_x
		self.pos_y = pos_y
		self.redColor = pygame.Color(255,0,0)
		self.greenColor = pygame.Color(0,255,0)
		self.blueColor = pygame.Color(0,0,255)
		self.whiteColor = pygame.Color(255,255,255)
		self.blackColor = pygame.Color(0,0,0)
		self.width = width
		self.height = height
		self.canvas = pygame.Surface((self.width,self.height))
		self.canvas.fill(self.blackColor)
		pygame.draw.rect(self.canvas,self.whiteColor,(1, 1, self.width - 2,  self.height - 2))
		
		self.inputs = []
		
		self.finished = False
		
		#Sector especifico para el inicio
		
		self.xs = [0, 0 , 0]
		self.blocked = [False, False, False]
		self.radio = min(self.width / 40, self.height / 40) / 2
		
		pygame.draw.rect(self.canvas,self.blackColor,(self.width / 5, self.height / 3, self.width / 5,  self.height / 3))
		pygame.draw.rect(self.canvas,self.whiteColor,(self.width / 5 + 2, self.height / 3 + 2, self.width / 5 - 4,  self.height / 3 - 4))
		pygame.draw.rect(self.canvas,self.blackColor,(3 * self.width / 5, self.height / 3, self.width / 5,  self.height / 3))
		pygame.draw.rect(self.canvas,self.whiteColor,(3 * self.width / 5 + 2, self.height / 3 + 2, self.width / 5 - 4,  self.height / 3 - 4))
		
		myfont = pygame.font.SysFont("monospace", self.height / 5)
		label_1 = myfont.render(u"¿?",1,(0,0,0))
		label_2 = myfont.render(u"¡!",1,(0,0,0))
		
		self.canvas.blit(label_1,(self.width/5 + 3, self.height/3 + 3))
		self.canvas.blit(label_2,(3 * self.width/5 + 3, self.height/3 + 3))
		
		self.paint_circles(0)
		self.paint_circles(1)
		self.paint_circles(2)
		
	def paint_circles(self, id):
		if id == 0: #Patron :  :
			pygame.draw.circle(self.canvas, self.redColor,((self.xs[0] * 2 + 1) * self.width / 5 - 2 * self.radio, self.height / 3 - 2 * self.radio), 2 * self.radio, 0)
			pygame.draw.circle(self.canvas, self.redColor,((self.xs[0] * 2 + 2) * self.width / 5 + 2 * self.radio, self.height / 3 - 2 * self.radio), 2 * self.radio, 0)
			pygame.draw.circle(self.canvas, self.redColor,((self.xs[0] * 2 + 2) * self.width / 5 + 2 * self.radio, 2 * self.height / 3 + 2 * self.radio), 2 * self.radio, 0)
			pygame.draw.circle(self.canvas, self.redColor,((self.xs[0] * 2 + 1) * self.width / 5 - 2 * self.radio, 2 * self.height / 3 + 2 * self.radio), 2 * self.radio, 0)
			
		elif id == 1: # patron ' : '
			pygame.draw.circle(self.canvas, self.greenColor,((self.xs[1] * 4 + 3) * self.width / 10 - self.radio, self.height / 3 - 2 * self.radio), 2 * self.radio, 0)
			pygame.draw.circle(self.canvas, self.greenColor,((self.xs[1] * 4 + 3) * self.width / 10 - self.radio, 2 * self.height / 3 + 2 * self.radio), 2 * self.radio, 0)
			pygame.draw.circle(self.canvas, self.greenColor,((self.xs[1] * 2 + 1) * self.width / 5 - 2 * self.radio, self.height / 2 - self.radio), 2 * self.radio, 0)
			pygame.draw.circle(self.canvas, self.greenColor,((self.xs[1] * 2 + 2) * self.width / 5 + 2 * self.radio, self.height / 2 - self.radio), 2 * self.radio, 0)
		
		elif id == 2: #patron  :: 
			pygame.draw.circle(self.canvas, self.blueColor,(((self.xs[2] * 8 + 5) * self.width) / 20 - self.radio, self.height / 3 - 2 * self.radio), 2 * self.radio, 0)
			pygame.draw.circle(self.canvas, self.blueColor,((self.xs[2] * 8 + 7) * self.width / 20 - self.radio, self.height / 3 - 2 * self.radio), 2 * self.radio, 0)
			pygame.draw.circle(self.canvas, self.blueColor,((self.xs[2] * 8 + 5) * self.width / 20 - self.radio, 2 * self.height / 3 + 2 * self.radio), 2 * self.radio, 0)
			pygame.draw.circle(self.canvas, self.blueColor,((self.xs[2] * 8 + 7) * self.width / 20 - self.radio, 2 * self.height / 3 + 2 * self.radio), 2 * self.radio, 0)
		return
		
	def erase_circles(self, id):
		if id == 0: #Patron :  :
			pygame.draw.circle(self.canvas, self.whiteColor,((self.xs[0] * 2 + 1) * self.width / 5 - 2 * self.radio, self.height / 3 - 2 * self.radio), 2 * self.radio, 0)
			pygame.draw.circle(self.canvas, self.whiteColor,((self.xs[0] * 2 + 2) * self.width / 5 + 2 * self.radio, self.height / 3 - 2 * self.radio), 2 * self.radio, 0)
			pygame.draw.circle(self.canvas, self.whiteColor,((self.xs[0] * 2 + 2) * self.width / 5 + 2 * self.radio, 2 * self.height / 3 + 2 * self.radio), 2 * self.radio, 0)
			pygame.draw.circle(self.canvas, self.whiteColor,((self.xs[0] * 2 + 1) * self.width / 5 - 2 * self.radio, 2 * self.height / 3 + 2 * self.radio), 2 * self.radio, 0)
			
		elif id == 1: # patron ' : '
			pygame.draw.circle(self.canvas, self.whiteColor,((self.xs[1] * 4 + 3) * self.width / 10 - self.radio, self.height / 3 - 2 * self.radio), 2 * self.radio, 0)
			pygame.draw.circle(self.canvas, self.whiteColor,((self.xs[1] * 4 + 3) * self.width / 10 - self.radio, 2 * self.height / 3 + 2 * self.radio), 2 * self.radio, 0)
			pygame.draw.circle(self.canvas, self.whiteColor,((self.xs[1] * 2 + 1) * self.width / 5 - 2 * self.radio, self.height / 2 - self.radio), 2 * self.radio, 0)
			pygame.draw.circle(self.canvas, self.whiteColor,((self.xs[1] * 2 + 2) * self.width / 5 + 2 * self.radio, self.height / 2 - self.radio), 2 * self.radio, 0)
		
		elif id == 2: #patron  :: 
			pygame.draw.circle(self.canvas, self.whiteColor,(((self.xs[2] * 8 + 5) * self.width) / 20 - self.radio, self.height / 3 - 2 * self.radio), 2 * self.radio, 0)
			pygame.draw.circle(self.canvas, self.whiteColor,((self.xs[2] * 8 + 7) * self.width / 20 - self.radio, self.height / 3 - 2 * self.radio), 2 * self.radio, 0)
			pygame.draw.circle(self.canvas, self.whiteColor,((self.xs[2] * 8 + 5) * self.width / 20 - self.radio, 2 * self.height / 3 + 2 * self.radio), 2 * self.radio, 0)
			pygame.draw.circle(self.canvas, self.whiteColor,((self.xs[2] * 8 + 7) * self.width / 20 - self.radio, 2 * self.height / 3 + 2 * self.radio), 2 * self.radio, 0)
		return
		
	def paint_blocked_circles(self, id):
		if id == 0: #Patron :  :
			pygame.draw.circle(self.canvas, self.redColor,((self.xs[0] * 2 + 1) * self.width / 5 - 2 * self.radio, self.height / 3 - 2 * self.radio), 2 * self.radio, 2)
			pygame.draw.circle(self.canvas, self.redColor,((self.xs[0] * 2 + 2) * self.width / 5 + 2 * self.radio, self.height / 3 - 2 * self.radio), 2 * self.radio, 2)
			pygame.draw.circle(self.canvas, self.redColor,((self.xs[0] * 2 + 2) * self.width / 5 + 2 * self.radio, 2 * self.height / 3 + 2 * self.radio), 2 * self.radio, 2)
			pygame.draw.circle(self.canvas, self.redColor,((self.xs[0] * 2 + 1) * self.width / 5 - 2 * self.radio, 2 * self.height / 3 + 2 * self.radio), 2 * self.radio, 2)
			
		elif id == 1: # patron ' : '
			pygame.draw.circle(self.canvas, self.greenColor,((self.xs[1] * 4 + 3) * self.width / 10 - self.radio, self.height / 3 - 2 * self.radio), 2 * self.radio, 2)
			pygame.draw.circle(self.canvas, self.greenColor,((self.xs[1] * 4 + 3) * self.width / 10 - self.radio, 2 * self.height / 3 + 2 * self.radio), 2 * self.radio, 2)
			pygame.draw.circle(self.canvas, self.greenColor,((self.xs[1] * 2 + 1) * self.width / 5 - 2 * self.radio, self.height / 2 - self.radio), 2 * self.radio, 2)
			pygame.draw.circle(self.canvas, self.greenColor,((self.xs[1] * 2 + 2) * self.width / 5 + 2 * self.radio, self.height / 2 - self.radio), 2 * self.radio, 2)
		
		elif id == 2: #patron  :: 
			pygame.draw.circle(self.canvas, self.blueColor,(((self.xs[2] * 8 + 5) * self.width) / 20 - self.radio, self.height / 3 - 2 * self.radio), 2 * self.radio, 2)
			pygame.draw.circle(self.canvas, self.blueColor,((self.xs[2] * 8 + 7) * self.width / 20 - self.radio, self.height / 3 - 2 * self.radio), 2 * self.radio, 2)
			pygame.draw.circle(self.canvas, self.blueColor,((self.xs[2] * 8 + 5) * self.width / 20 - self.radio, 2 * self.height / 3 + 2 * self.radio), 2 * self.radio, 2)
			pygame.draw.circle(self.canvas, self.blueColor,((self.xs[2] * 8 + 7) * self.width / 20 - self.radio, 2 * self.height / 3 + 2 * self.radio), 2 * self.radio, 2)
		return
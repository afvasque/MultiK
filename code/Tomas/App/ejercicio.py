# coding: utf-8
import pygame

class ejercicio:
	def __init__(self, teclados, pos_x, pos_y, width, height):
		self.teclados = teclados
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
		self.finished = False
		
	def screen(self):
		return self.canvas

	def react(self,id,input):
		return
	
class ejercicio1(ejercicio):
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
		
		self.finished = False
		
		#Sector especifico para el inicio
		
		self.inputs = ['', '', '']

		self.blocked = [False, False, False]
		
		pygame.draw.rect(self.canvas,self.blueColor,(self.width / 5, self.height / 7, 3 * self.width / 5,  self.height / 7))
		pygame.draw.rect(self.canvas,self.greenColor,(self.width / 5, 3 * self.height / 7, 3 * self.width / 5,  self.height / 7))
		pygame.draw.rect(self.canvas,self.redColor,(self.width / 5, 5 * self.height / 7, 3 * self.width / 5,  self.height / 7))
		
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
			if self.blocked[0] and self.blocked[1] and self.blocked[2]:
				self.finished = True
			else:
				if self.blocked[index_teclado]:
					pygame.draw.rect(self.canvas,self.whiteColor,(self.width / 5 + 3, (2 * index_teclado + 1) * self.height / 7 + 3, 3 * self.width / 5 - 6,  self.height / 7 - 6))
					self.myfont = pygame.font.SysFont("monospace", self.height / 7)
					label = self.myfont.render(self.inputs[index_teclado], 1, (0,0,0))
					self.canvas.blit(label,(self.width / 5, (2 * index_teclado + 1) * self.height / 7))
				else:
					if index_teclado == 0:
						pygame.draw.rect(self.canvas,self.blueColor,(self.width / 5, self.height / 7, 3 * self.width / 5,  self.height / 7))
					elif index_teclado == 1:
						pygame.draw.rect(self.canvas,self.greenColor,(self.width / 5, 3 * self.height / 7, 3 * self.width / 5,  self.height / 7))
					else:
						pygame.draw.rect(self.canvas,self.redColor,(self.width / 5, 5 * self.height / 7, 3 * self.width / 5,  self.height / 7))
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
						pygame.draw.rect(self.canvas,self.blueColor,(self.width / 5, self.height / 7, 3 * self.width / 5,  self.height / 7))
					elif index_teclado == 1:
						pygame.draw.rect(self.canvas,self.greenColor,(self.width / 5, 3 * self.height / 7, 3 * self.width / 5,  self.height / 7))
					else:
						pygame.draw.rect(self.canvas,self.redColor,(self.width / 5, 5 * self.height / 7, 3 * self.width / 5,  self.height / 7))
					self.inputs[index_teclado] = self.inputs[index_teclado][:-1]
					self.myfont = pygame.font.SysFont("monospace", self.height / 7)
					label = self.myfont.render(self.inputs[index_teclado], 1, (255,255,255))
					self.canvas.blit(label,(self.width / 5, (2 * index_teclado + 1) * self.height / 7))
		return

class ejercicio2(ejercicio):
	def __init__(self, teclados, pos_x, pos_y, width, height):
		self.teclados = teclados
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
	def __init__(self, teclados, pos_x, pos_y, width, height):
		self.teclados = teclados
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
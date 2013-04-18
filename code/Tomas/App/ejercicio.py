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
		self.canvas.fill(self.whiteColor)
		self.finished = False
		
	def screen(self):
		return self.canvas

	def react(self,id,char):
		return
		
class ejercicio1(ejercicio):
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
		self.canvas.fill(self.whiteColor)
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


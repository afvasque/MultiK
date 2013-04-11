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
		
	def screen(self):
		return self.canvas
		
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
		
		#Sector especifico para el inicio
		
		self.inputs = ['input 1', 'input 2', 'input 3']
		#self.inputs.append("input 1")
		#self.inputs.append("input 2")
		#self.inputs.append("input 3")
		
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

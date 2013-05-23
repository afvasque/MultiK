import pygame


class Textbox:
	def __init__(self, pos_x, pos_y, width, height):
		self.pos_x = pos_x
		self.pos_y = pos_y
		self.Color = pygame.Color(0,255,0)
		self.whiteColor = pygame.Color(255,255,255)
		self.blackColor = pygame.Color(0,0,0)
		self.width = width
		self.height = height
		self.canvas = pygame.Surface((self.width,self.height))
		self.canvas.fill(self.blackColor)
		pygame.draw.rect(self.canvas,self.whiteColor,(1, 1, self.width - 2, self.height - 2))
		#Sector especifico para el inicio
		
		self.Value = ""
		
		pygame.font.init()
		
		self.myfont = pygame.font.SysFont("monospace", self.height - 2)

	def screen(self):
		return self.canvas

	def react(self,input):
		if len(input)==1:
			self.Value = self.Value + input
			print "valor: " + self.Value

			self.myfont = pygame.font.SysFont("monospace", self.height - 2)
			label = self.myfont.render(self.Value, 1, self.blackColor)
			self.canvas.blit(label,(1, 1))


		elif input == "Back":
			if len(self.Value) > 0:
				pygame.draw.rect(self.canvas,self.whiteColor,(1, 1, self.width - 2, self.height - 2))
				self.Value = self.Value[:-1]
				self.myfont = pygame.font.SysFont("monospace", self.height - 2)
				label = self.myfont.render(self.Value, 1, self.blackColor)
				self.canvas.blit(label,(1, 1))
		return

class Listview:

	def __init__(self, pos_x, pos_y, width, height):
		self.pos_x = pos_x
		self.pos_y = pos_y
		self.Color = pygame.Color(0,255,0)
		self.whiteColor = pygame.Color(255,255,255)
		self.blackColor = pygame.Color(0,0,0)
		self.width = width
		self.height = height
		self.canvas = pygame.Surface((self.width,self.height))
		self.canvas.fill(self.blackColor)
		pygame.draw.rect(self.canvas,self.whiteColor,(1, 1, self.width - 2, self.height - 2))


				
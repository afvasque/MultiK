import pygame


class Textbox:
	def __init__(self,canvas, pos_x, pos_y, width, height):
		self.pos_x = pos_x
		self.pos_y = pos_y
		self.Color = pygame.Color(0,255,0)
		self.whiteColor= pygame.Color(255,255,255)
		self.width = width
		self.height = height
		self.canvas=canvas
		#Sector especifico para el inicio
		
		self.Value = ""
		
		pygame.draw.rect(self.canvas,self.Color,(self.pos_x, self.pos_y, self.width, self.height))
		
		pygame.font.init()
		
		self.myfont = pygame.font.SysFont("monospace", self.height)

	def screen(self):
		return self.canvas

	def react(self,input):
		if len(input)==1:
			self.Value = self.Value + input
			print "valor: "+self.Value

			self.myfont = pygame.font.SysFont("monospace", self.height)
			label = self.myfont.render(self.Value, 1, (0,0,0))
			self.canvas.blit(label,(self.pos_x, self.pos_y))


		elif input == "Back":
			if len(self.Value) > 0:
				pygame.draw.rect(self.canvas,self.Color,(self.pos_x, self.pos_y, self.width, self.height))
				self.Value = self.Value[:-1]
				self.myfont = pygame.font.SysFont("monospace", self.height)
				label = self.myfont.render(self.Value, 1, (0,0,0))
				self.canvas.blit(label,(self.pos_x, self.pos_y))
		return
				
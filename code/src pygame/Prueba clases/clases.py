import pygame

class Textbox:
	def __init__(self,canvas, pos_x, pos_y, width, height):
		print "dib textbox"
		self.pos_x = pos_x
		self.pos_y = pos_y
		self.Color = pygame.Color(0,255,0)
		self.whiteColor= pygame.Color(255,255,255)
		self.width = width
		self.height = height
		self.canvas=canvas
		#Sector especifico para el inicio
		
		self.input = ""
		
		pygame.draw.rect(self.canvas,self.Color,(self.pos_x, self.pos_y, self.width, self.height))
		
		pygame.font.init()
		
		self.myfont = pygame.font.SysFont("monospace", self.height)
		#label1 = self.myfont.render(self.input, 1, (0,0,0))
		#self.canvas.blit(label1,(self.width, self.height))

	def screen(self):
		return self.canvas

	def react(self,input):
		
		if len(input)==1:
			self.input = self.input + input
			print self.input
			#self.myfont = pygame.font.SysFont("monospace", self.height)
			#label = self.myfont.render(self.input, 1, (255,255,255))
			#self.canvas.blit(label,(self.width, self.height))

			self.myfont = pygame.font.SysFont("monospace", self.height)
			label = self.myfont.render(self.input, 1, (0,0,0))
			self.canvas.blit(label,(0, 0))


		elif input == "Back":
			if len(self.input) > 0:
				pygame.draw.rect(self.canvas,self.Color,(self.pos_x, self.pos_y, self.width, self.height))
				self.input = self.input[:-1]
				self.myfont = pygame.font.SysFont("monospace", self.height)
				label = self.myfont.render(self.input, 1, (0,0,0))
				self.canvas.blit(label,(0, 0))
		return
				


class ejercicio:

	def __init__(self, pos_x, pos_y, width, height):
		self.pos_x = pos_x
		self.pos_y = pos_y
		self.whiteColor = pygame.Color(255,255,255)
		self.width = width
		self.height = height
		self.canvas = pygame.Surface((self.width,self.height))
		self.canvas.fill(self.whiteColor)
		self.blocked=False
		self.Objects=[]

		self.Objects.append(Textbox(self.canvas,0,0,300,40))
		self.canvas.blit(self.Objects[0].screen(),(self.width, self.height ))
		
	def screen(self):
		return self.canvas

	def react(self,input):

		self.Objects[0].react(input)


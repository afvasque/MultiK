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
		self.myfont = pygame.font.SysFont("monospace", self.height - 2)
		label = self.myfont.render(self.Value, 1, self.blackColor)
		if len(input)==1:
			self.Value = self.Value + input
			print "valor: " + self.Value
			self.myfont = pygame.font.SysFont("monospace", self.height - 2)
			label = self.myfont.render(self.Value, 1, self.blackColor)
			#self.canvas.blit(label,(1, 1))


		elif input == "Back":
			if len(self.Value) > 0:
				#pygame.draw.rect(self.canvas,self.whiteColor,(1, 1, self.width - 2, self.height - 2))
				self.Value = self.Value[:-1]
				self.myfont = pygame.font.SysFont("monospace", self.height - 2)
				label = self.myfont.render(self.Value, 1, self.blackColor)
				#self.canvas.blit(label,(1, 1))
		pygame.draw.rect(self.canvas,self.whiteColor,(1, 1, self.width - 2, self.height - 2))
		if self.width > label.get_width():
			self.canvas.blit(label,(1, 1))
		else:
			self.canvas.blit(label,(self.width - label.get_width() - 1, 1))		
		return

class Listview:
	def __init__(self, texts, pos_x, pos_y, width, height):
		self.pos_x = pos_x
		self.pos_y = pos_y
		self.Color = pygame.Color(0,255,0)
		self.whiteColor = pygame.Color(255,255,255)
		self.blackColor = pygame.Color(0,0,0)
		self.focusColor = pygame.Color(210,210,210)
		self.width = width
		self.height = height
		self.canvas = pygame.Surface((self.width,self.height))
		self.canvas.fill(self.blackColor)
		pygame.draw.rect(self.canvas,self.whiteColor,(1, 1, self.width - 2, self.height - 2))
		self.texts = texts
		self.focus = 0
		self.count = len(texts)
		self.font_len=0
		for i in range(self.count):
			temp_font= len(texts[i])
			if temp_font>self.font_len:
				self.font_len=temp_font

		self.font_final= int(1.5 * self.width/self.font_len)
		font2= ((self.height - self.count) / self.count)

		if self.font_final>font2:
			self.font_final=font2
		
		pygame.font.init()
		
		self.myfont = pygame.font.SysFont("monospace", self.font_final)
		#self.myfont = pygame.font.SysFont("monospace", (self.height - self.count) / self.count)
		
		self.labels = [self.myfont.render(self.texts[0], 1, self.blackColor)] * self.count
		for i in range(self.count):
			self.labels[i] = self.myfont.render(self.texts[i], 1, self.blackColor)
			self.canvas.blit(self.labels[i],(1, (self.height / self.count) * i + 1))
			pygame.draw.rect(self.canvas,self.blackColor,( 1, (self.height / self.count) * (i + 1) + 1, self.width - 2, 2))
		
		pygame.draw.rect(self.canvas,self.focusColor,( 1, (self.height / self.count) * (self.focus) + 1, self.width - 2, self.height / self.count))
		self.canvas.blit(self.labels[self.focus],(1, (self.height / self.count) * self.focus + 1))
		
	def react(self,input):
		if (input == "-v" or input == "-^"):
			pygame.draw.rect(self.canvas,self.whiteColor,( 1, (self.height / self.count) * (self.focus) + 1, self.width - 2, self.height / self.count))
			self.canvas.blit(self.labels[self.focus],(1, (self.height / self.count) * self.focus + 1))
			if input == "-v":
				self.focus = self.focus + 1
				self.focus = self.focus % self.count
			else:
				if self.focus == 0:
					self.focus = self.count - 1
				else:
					self.focus = self.focus - 1
			pygame.draw.rect(self.canvas,self.focusColor,( 1, (self.height / self.count) * (self.focus) + 1, self.width - 2, self.height / self.count))
			self.canvas.blit(self.labels[self.focus],(1, (self.height / self.count) * self.focus + 1))
			for i in range(self.count):
				pygame.draw.rect(self.canvas,self.blackColor,( 1, (self.height / self.count) * (i + 1) + 1, self.width - 2, 2))
			
	def screen(self):
		return self.canvas

	def answer(self):
		return self.texts[self.focus]
			

# coding=utf-8
import pygame
from clases import *

class Pareamiento:
	def __init__(self, id, pos_x, pos_y, width, height):
		self.id = id
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
		
		pygame.draw.rect(self.canvas,self.blackColor,(self.width / 7, 10,  5 * self.width / 7,  self.height - 20))
		pygame.draw.rect(self.canvas,self.whiteColor,(self.width / 7 + 1, 11,  5 * self.width / 7 - 2,  self.height - 22))
		
		pygame.font.init()

		self.value = 0
	
	def screen(self):
		return self.canvas
		
	def react(self,input):
		if input == "0":
			self.value = self.value * 10
		elif input == "1":
			self.value = self.value * 10 + 1
		elif input == "2":
			self.value = self.value * 10 + 2
		elif input == "3":
			self.value = self.value * 10 + 3
		elif input == "4":
			self.value = self.value * 10 + 4
		elif input == "5":
			self.value = self.value * 10 + 5
		elif input == "6":
			self.value = self.value * 10 + 6
		elif input == "7":
			self.value = self.value * 10 + 7
		elif input == "8":
			self.value = self.value * 10 + 8
		elif input == "9":
			self.value = self.value * 10 + 9
		elif input == "Back":
			self.value = int(self.value / 10)
		pygame.draw.rect(self.canvas,self.blackColor,(self.width / 7, 10,  5 * self.width / 7,  self.height - 20))
		pygame.draw.rect(self.canvas,self.whiteColor,(self.width / 7 + 1, 11,  5 * self.width / 7 - 2,  self.height - 22))
		self.myfont = pygame.font.SysFont("monospace", self.height - 24)
		label = self.myfont.render("%i" % self.value, 1, self.blackColor)
		self.canvas.blit(label,(self.width / 7 + 1, 12))
		
	def waiting(self):
		return False
		
class setup_nombre:
	def __init__(self,pareamiento):
		self.id = pareamiento.id
		self.pos_x = pareamiento.pos_x
		self.pos_y = pareamiento.pos_y
		self.redColor = pygame.Color(255,0,0)
		self.greenColor = pygame.Color(0,255,0)
		self.blueColor = pygame.Color(0,0,255)
		self.whiteColor = pygame.Color(255,255,255)
		self.blackColor = pygame.Color(0,0,0)
		self.width = pareamiento.width
		self.height = pareamiento.height
		self.canvas = pygame.Surface((self.width,self.height))
		self.canvas.fill(self.blackColor)
		pygame.draw.rect(self.canvas,self.whiteColor,(1, 1, self.width - 2,  self.height - 2))
		
		self.text_box = Numbox(int(self.width / 7), 10,  int(5 * self.width / 7),  int(self.height - 20))
		self.canvas.blit(self.text_box.screen(), (self.text_box.pos_x, self.text_box.pos_y))
		
	def screen(self):
		return self.canvas
		
	def get_audio_text(self):
		return "Ingresa tu numero de lista"
		
	def react(self, input):
		self.text_box.react(input)
		self.canvas.blit(self.text_box.screen(), (self.text_box.pos_x, self.text_box.pos_y))
	
	def value(self):
		return self.text_box.value
	
	def waiting(self):
		return False
		
class setup_grupo:
	def __init__(self,setup_nombre):
		self.id = setup_nombre.id
		self.pos_x = setup_nombre.pos_x
		self.pos_y = setup_nombre.pos_y
		self.redColor = pygame.Color(255,0,0)
		self.greenColor = pygame.Color(0,255,0)
		self.blueColor = pygame.Color(0,0,255)
		self.whiteColor = pygame.Color(255,255,255)
		self.blackColor = pygame.Color(0,0,0)
		self.width = setup_nombre.width
		self.height = setup_nombre.height
		self.canvas = pygame.Surface((self.width,self.height))
		self.canvas.fill(self.blackColor)
		pygame.draw.rect(self.canvas,self.whiteColor,(1, 1, self.width - 2,  self.height - 2))
		
		self.text_box = Numbox(self.width / 7, 10,  5 * self.width / 7,  self.height - 20)
		self.canvas.blit(self.text_box.screen(), (self.text_box.pos_x, self.text_box.pos_y))
		
	def screen(self):
		return self.canvas
		
	def get_audio_text(self):
		return "Ingresa tu grupo"
		
	def react(self, input):
		self.text_box.react(input)
		self.canvas.blit(self.text_box.screen(), (self.text_box.pos_x, self.text_box.pos_y))
	
	def value(self):
		return self.text_box.value
	
	def waiting(self):
		return False
		
class setup_wait:
	def __init__(self,setup_grupo):
		self.id = setup_grupo.id
		self.pos_x = setup_grupo.pos_x
		self.pos_y = setup_grupo.pos_y
		self.redColor = pygame.Color(255,0,0)
		self.greenColor = pygame.Color(0,255,0)
		self.blueColor = pygame.Color(0,0,255)
		self.whiteColor = pygame.Color(255,255,255)
		self.blackColor = pygame.Color(0,0,0)
		self.width = setup_grupo.width
		self.height = setup_grupo.height
		self.canvas = pygame.Surface((self.width,self.height))
		self.canvas.fill(self.blackColor)
		
		pygame.font.init()
		self.myfont = pygame.font.SysFont("monospace", self.height / 3)
		label = self.myfont.render("Espera", 1, self.whiteColor)
		self.canvas.blit(label,(1, self.height / 3))
		
	def screen(self):
		return self.canvas
		
	def get_audio_text(self):
		return "Porfavor espera"
		
	def react(self, input):
		return
	
	def waiting(self):
		return True
	
# coding: utf-8
import pygame

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
		label = self.myfont.render(self.value, 1, self.blackColor)
		self.canvas.blit(label,(self.width / 7 + 1, 12)
		
from PreguntaColaborativa import *
from Alumno import *
from ejercicio import *
from Transformador import *

class Manager:
	def __init__(self, alumnos, pos_x, pos_y, width, height):
		self.alumnos = alumnos
		self.pos_x = pos_x
		self.pos_y = pos_y
		self.width = width
		self.height = height
		
		self.nivel = 0
		self.correctas_current = 0 #Las correctas que lleva en este nivel
		self.malas_current = 0 #Las veces que ha respondido mal la pregunta actual
		self.pregunta = None
		self.ejercicio = ejercicio0(self.alumnos, self.pos_x, self.pos_y, self.width, self.height)
		
		self.correctas_nivel = 5 #La cantidad de correctas que necesitan para pasar de nivel
		self.nivel_max = 1
		
		self.transformador = Transformador()
		
		return
		
	def correct(self):
		if self.nivel == 0:
			return True
		print "Nivel de comprobacion mayor a 0"
		if not self.pregunta.orden:
			print "El orden no importa"
			self.pregunta.respuestas.sort()
			self.ejercicio.inputs.sort()
		
		for i in range(3):
			if not self.pregunta.respuestas[i] == self.ejercicio.inputs[i]:
				print "Encontrado inconsistencia"
				return False
		print "No encontrado inconsistencias"
		return True
	
	def advance(self):
		if self.correctas_current >= self.correctas_nivel or self.nivel == 0:
			self.nivel+=1
			self.correctas_current = 0
			if self.nivel > self.nivel_max:
				self.nivel = 1
		self.malas_current = 0
		self.getPregunta()
		
	def getPregunta(self):
		if self.nivel == 1:
			self.pregunta = self.transformador.threeToOne(1, True)
			self.ejercicio = ejercicio1(self.alumnos, self.pos_x, self.pos_y, self.width, self.height)
			
	def getAudio(self):
		audio = ""
		if self.nivel == 0:
			return "Busca tu grupo y nombre y presiona enter"
		if self.pregunta.individualCount == 3 and self.pregunta.orden:
			for i in range(3):
				audio += self.alumnos[i].name + " " + self.pregunta.audios[i] + "."
		return audio
	

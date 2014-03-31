from PreguntaIndividual import *
from PreguntaColaborativa import *
from LectorCSV import *
import random

class Transformador:
	def __init__(self):
		self.lector = LectorCSV.getInstance()
		self.niveles = [1,2,3,4,5,6,7,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43]
		#18 ver que cresta hacer
		#27 es raro
		self.tresparalelas = [1,18]
		self.unaunica = [5,6,7,11,12,13,14,15,16,17,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43]
		self.unacombinable = [2,3,4]
		return
		
	def autoTransform(self, nivel, group_size = 3):
		nivelReal = self.niveles[nivel - 1]
		preguntasI = self.lector.preguntas[nivelReal]
		rand = random.randint(0, len(preguntasI)-1)
		preguntaI = preguntasI[rand]
		
		preguntaC = PreguntaColaborativa()
		preguntaC.nivel = preguntaI.nivel
		preguntaC.individualCount = 1
		preguntaC.preguntas.append(preguntaI.pregunta)
		preguntaC.alternativas.extend(preguntaI.alternativas)
		preguntaC.respuestas.append(preguntaI.respuesta)
		preguntaC.audios.append(preguntaI.audio)
		preguntaC.imagenes.append(preguntaI.imagen)	
		
		return preguntaC
		
	def oneToOne(self, nivel):
		preguntasI = filter(lambda x: x.nivel == nivel, self.lector.preguntas)
		rand = random.randint(0, len(preguntasI)-1)
		preguntaI = preguntasI[rand]
		
		preguntaC = PreguntaColaborativa()
		preguntaC.nivel = preguntaI.nivel
		preguntaC.individualCount = 1
		preguntaC.preguntas.append(preguntaI.pregunta)
		preguntaC.alternativas.append(preguntaI.alternativas)
		preguntaC.respuestas.append(preguntaI.respuesta)
		preguntaC.audios.append(preguntaI.audio)
		preguntaC.imagenes.append(preguntaI.imagen)
		
		return preguntaC
		
	def twoToOne(self, nivel, orden):
		preguntasI = filter(lambda x: x.nivel == nivel, self.lector.preguntas)
		rand = random.randint(0, len(preguntasI)-1)
		pregunta1 = preguntasI[rand]
		if not orden:
			preguntasI = filter(lambda x: x.audio == pregunta1.audio, preguntasI)
		rand = random.randint(0, len(preguntasI)-1)
		pregunta2 = preguntasI[rand]
		
		preguntaC = PreguntaColaborativa()
		preguntaC.nivel = nivel
		preguntaC.individualCount = 2
		preguntaC.preguntas.append(pregunta1.pregunta)
		preguntaC.preguntas.append(pregunta2.pregunta)
		preguntaC.alternativas.append(pregunta1.alternativas)
		preguntaC.alternativas.append(pregunta2.alternativas)
		preguntaC.respuestas.append(pregunta1.respuesta)
		preguntaC.respuestas.append(pregunta2.respuesta)
		preguntaC.audios.append(pregunta1.audio)
		preguntaC.audios.append(pregunta2.audio)
		preguntaC.imagenes.append(pregunta1.imagen)
		preguntaC.imagenes.append(pregunta2.imagen)
		preguntaC.orden = orden
		
		return preguntaC
	
	def threeToOne(self, nivel, orden):
		preguntasI = filter(lambda x: x.nivel == nivel, self.lector.preguntas)
		rand = random.randint(0, len(preguntasI)-1)
		preguntas = [None,None,None]
		preguntas[0] = preguntasI[rand]
		if not orden:
			preguntasI = filter(lambda x: x.audio == preguntas[0].audio, preguntasI)
		rand = random.randint(0, len(preguntasI)-1)
		preguntas[1] = preguntasI[rand]
		rand = random.randint(0, len(preguntasI)-1)
		preguntas[2] = preguntasI[rand]
		
		preguntaC = PreguntaColaborativa()
		preguntaC.nivel = nivel
		preguntaC.individualCount = 3
		preguntaC.orden = orden
		
		for i in range(3):
			preguntaC.preguntas.append(preguntas[i].pregunta)
			preguntaC.alternativas.append(preguntas[i].alternativas)
			preguntaC.respuestas.append(preguntas[i].respuesta)
			preguntaC.audios.append(preguntas[i].audio)
			preguntaC.imagenes.append(preguntas[i].imagen)
		
		return preguntaC
		

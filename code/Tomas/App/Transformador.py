from PreguntaIndividual import *
from PreguntaColaborativa import *
from LectorCSV import *
import random

class Transformador:
	def __init__(self):
		self.lector = LectorCSV.getInstance()
		return
		
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
		preguntas = []
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
		
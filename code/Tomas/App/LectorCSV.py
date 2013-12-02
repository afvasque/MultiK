from PreguntaIndividual import *
import csv

class LectorCSV:
	_instance = None
	
	def __init__(self):
		self.preguntas = list()
		with open('Ejercicios/EjerciciosLenguaje.csv', 'rb') as csvfile:
			lenguajereader = csv.reader(csvfile, delimiter=';', quoting=csv.QUOTE_NONE)
			rownum=0
			for row in lenguajereader:
				if rownum > 0:
					pregunta = PreguntaIndividual()
					pregunta.nivel = row[0]
					pregunta.pregunta = row[1].decode('latin-1')
					for x in range(2,5):
						if len(row[x])>0:
							pregunta.alternativas.append(row[x].decode('latin-1').strip())	
					pregunta.respuesta = row[5].decode('latin-1').strip()
					pregunta.audio = row[6].decode('latin-1')
					pregunta.imagen= row[7].decode('latin-1')
					
					self.preguntas.append(pregunta)
				rownum += 1

		return
	
	@staticmethod
	def getInstance():
		if _instance is None:
			_instace = LectorCSV()
		return _instance
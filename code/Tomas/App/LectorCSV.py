from PreguntaIndividual import *
import csv

CSVinstance = None
class LectorCSV:
	def __init__(self):
		curso = "3D"
		#Leer los ejercicios
		self.preguntas = {}
		nivel_anterior = -1
		with open('archivos/Ejercicios/EjerciciosLenguaje.csv', 'rb') as csvfile:
			lenguajereader = csv.reader(csvfile, delimiter=';', quoting=csv.QUOTE_NONE)
			rownum=0
			for row in lenguajereader:
				if rownum > 0:
					pregunta = PreguntaIndividual()
					pregunta.nivel = int(row[0])
					if pregunta.nivel != nivel_anterior:
						self.preguntas[pregunta.nivel] = list()
						nivel_anterior = pregunta.nivel
					pregunta.pregunta = row[1].decode('latin-1')
					for x in range(2,5):
						if len(row[x])>0:
							pregunta.alternativas.append(row[x].decode('latin-1').strip())	
					pregunta.respuesta = row[5].decode('latin-1').strip()
					pregunta.audio = row[6].decode('latin-1')
					pregunta.imagen= row[7].decode('latin-1')
					
					self.preguntas[pregunta.nivel].append(pregunta)
				rownum += 1
		#Leer los alumnos
		self.alumnos = {}
		filepath = "archivos/ListasCSV/"+ curso + ".csv"
		with open(filepath, 'rb') as csvfile:
			lenguajereader = csv.reader(csvfile, delimiter=',', quoting=csv.QUOTE_NONE)
			for row in lenguajereader:
				self.alumnos[int(row[0])] = row[1].decode('latin-1')
		
		return
	
	@staticmethod
	def getInstance():
		global CSVinstance
		if CSVinstance is None:
			CSVinstance = LectorCSV()
		return CSVinstance

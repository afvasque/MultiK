from Generador import *
from BasicOperacion import *
from TipoOperacionNivel import *
from Alumno import *
import random
import csv


class GeneradorPreguntas(object):
	
	_instance = None
	preguntas= None

	#def __init__(self, alumno):
	#	
	#	self.alumno= alumno
	#	self.interpal= Generador_pal("clase de prueba")
	#	self.interor= Generador_or("clase de prueba")
	#	return

	def __new__(cls, *args, **kwargs):
			if not cls._instance:
				cls._instance = super(GeneradorPreguntas, cls).__new__(
									cls, *args, **kwargs)
			return cls._instance

	def SetAlumno(self,alumno):

		self.alumno=alumno

		if self.preguntas is None:

			self.preguntas= list();


			with open('Ejercicios/EjerciciosLenguaje.csv', 'rb') as csvfile:
				lenguajereader = csv.reader(csvfile, delimiter=';', quoting=csv.QUOTE_NONE)
				rownum=0
				for row in lenguajereader:

					if rownum == 0:
						header = row
					else:
						operacion= BasicOperacion()
						operacion.nivelOperacion= int(row[0])
						operacion.pregunta= row[1].decode('latin-1')
						for x in range(2,5):
							if len(row[x])>0:
								operacion.alternativas.append(row[x].decode('latin-1').strip())

						operacion.respuesta= row[5].decode('latin-1').strip()
						operacion.audio_pregunta= row[6].decode('latin-1')
						operacion.path_imagen= row[7].decode('latin-1')

						self.preguntas.append(operacion)					
							 
					rownum += 1

		return
	
	#TO-DO: que no se repitan al tiro las preguntas
	def Getsiguiente(self, niveloperacion, tipo_operacion):
		
		operaciones= filter(lambda x: x.nivelOperacion == niveloperacion, self.preguntas)

		rand= random.randint(0, len(operaciones)-1)

		operacion= operaciones[rand]

		operacion.TipoOperacion = tipo_operacion
		operacion.feedback_correcto = "Bien, " + self.alumno.Nombre
		operacion.feedback_error = "Inténtalo de nuevo"
		print "op: "+operacion.audio_pregunta
		return operacion

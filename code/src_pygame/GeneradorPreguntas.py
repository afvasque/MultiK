from BasicOperacion import *
from TipoOperacionNivel import *
from Alumno import *
import random
import csv


class GeneradorPreguntas(object):
	
	_instance = None
	preguntas= None

	# Para que no se repitan las preguntas inmediatamente
	preguntas_seleccionadas = []

	path_ejercicios = "./archivos/Ejercicios/EjerciciosLenguaje.csv"

	def __new__(cls, *args, **kwargs):
			if not cls._instance:
				cls._instance = super(GeneradorPreguntas, cls).__new__(
									cls, *args, **kwargs)
			return cls._instance

	def SetAlumno(self,alumno):

		self.alumno=alumno

		if self.preguntas is None:

			self.preguntas= list();


			with open(self.path_ejercicios, 'rb') as csvfile:
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
						random.shuffle(operacion.alternativas)

						operacion.respuesta= row[5].decode('latin-1').strip()
						operacion.audio_pregunta= row[6].decode('latin-1')
						operacion.path_imagen= row[7].decode('latin-1')

						if len(row) > 7:
							operacion.feedback_error_custom = row[8].decode('latin-1')

						self.preguntas.append(operacion)					
							 
					rownum += 1

		return

	def Getsiguiente(self, niveloperacion, tipo_operacion, operacion_actual):
		
		operaciones= filter(lambda x: x.nivelOperacion == niveloperacion, self.preguntas)

		rand = random.randint(0, len(operaciones)-1)
		operacion = operaciones[rand]


		if len(self.preguntas_seleccionadas) < len(operaciones):
			while operacion in self.preguntas_seleccionadas:
				rand= random.randint(0, len(operaciones)-1)
				operacion = operaciones[rand]
		else:
			self.preguntas_seleccionadas = []

		self.preguntas_seleccionadas.append(operacion)


		operacion.TipoOperacion = tipo_operacion
		operacion.feedback_correcto = "Bien, " + self.alumno.Nombre
		if operacion_actual.feedback_error_custom == "":
			operacion_actual.feedback_error_custom = "Pasemos a la siguiente pregunta..."
		operacion.feedback_error = operacion_actual.feedback_error_custom #"Inténtalo de nuevo"

		return operacion

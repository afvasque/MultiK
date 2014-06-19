	
from TipoOperacionNivel import *
from ModuloNivel import ModuloNivel
from BasicOperacion import *
from Reglas_Fijas import *
from GeneradorPreguntas import *
import time

class Reglas:

	
	def __init__(self):
		
		lista = list()
		self.nivel_tipoOperacion = {}	
		self.path_TipoOperacionNivel = './archivos/Ejercicios/TipoOperacionNivel.csv'	
		
		with open(self.path_TipoOperacionNivel, 'rb') as csvfile:
			lenguajereader = csv.reader(csvfile, delimiter=';', quoting=csv.QUOTE_NONE)
			rownum=0
			for row in lenguajereader:

				if rownum == 0:
					header = row
				else:
					lista.append(TipoOperacionNivel(int(row[0]),TipoOperacionNivel.InttoTipoOperacion(int(row[1]))))
					self.nivel_tipoOperacion[int(row[0])] = TipoOperacionNivel.InttoTipoOperacion(int(row[1]))
					print "agregado nivel"+row[0]						 
				rownum += 1
		
		self.modulosNivel = list()
		self.modulosNivel.append(ModuloNivel(lista, "principal"))
		return		
	
	# Metodo publico que entrega la siguiente operacion en funcion
	# de las reglas pedagogicas. Es lo unico que se puede acceder de
	# la clase Reglas
	def GetSiguienteOperacion(self, operacion, alumno):
		
		if (not operacion.respuesta_correcta)  and (operacion.CantidadVecesIncorrectaSoloEsta <= 2) and (operacion.feedback_correcto != "First") :
			operacion.feedback_error = "Inténtalo de nuevo"
			return operacion		
		
		operacion.cantidadMaximaNivel= max(Reglas_Fijas.MaximoNivel, operacion.cantidadMaximaNivel)
		
		siguiente_nivel = operacion.nivelOperacion
		cantidad_nivel = operacion.cantidadNivel
		cantidad_maxima_nivel = operacion.cantidadMaximaNivel
		borrarCorrectas = False
		tipoActual = self.nivel_tipoOperacion[operacion.nivelOperacion]

		cambia_nivel= Reglas_Fijas.CambioNivel(operacion)
		
		if cambia_nivel == CambioNivel.Sube:
			#Cambio nivel
			borrarCorrectas = True
			siguiente_nivel+=1
			if siguiente_nivel == 8:
				siguiente_nivel = 11
			if siguiente_nivel == 36:
				siguiente_nivel = 37
			if siguiente_nivel == 38:
				siguiente_nivel = 39
			if siguiente_nivel ==41:
				siguiente_nivel = 42
			cantidad_nivel = 1
			op= self.AlterarFlujo(operacion, siguiente_nivel)
			tipoActual = op.TipoOperacion
			siguiente_nivel = op.nivelOperacion + 1
		
		elif cambia_nivel == CambioNivel.Mantiene:
			cantidad_maxima_nivel += self.SubidaMaximoNivel(operacion)
			cantidad_nivel+=1
		
		siguiente_operacion= None
		
		generador= GeneradorPreguntas()
		generador.SetAlumno(alumno)

		#Obtenemos el siguiente nivel a partir del nivel actual
		tipop = self.modulosNivel[0].GetSiguiente(siguiente_nivel)

		siguiente_operacion = generador.Getsiguiente(siguiente_nivel, tipop, operacion)

		if borrarCorrectas:
			siguiente_operacion.cambio_reciente_nivel= True
			siguiente_operacion.correctasTotales = 0

		if siguiente_nivel == operacion.nivelOperacion:
			siguiente_operacion.cantidadMaximaNivel= cantidad_maxima_nivel
			siguiente_operacion.AgregarPuntajesNivel(operacion.puntajesNivel, operacion.puntaje)
			siguiente_operacion.cantidadNivel= cantidad_nivel
			siguiente_operacion.puntajesNivel= operacion.puntajesNivel
			siguiente_operacion.correctas_seguidas += operacion.correctas_seguidas

		else:
			siguiente_operacion.cantidadNivel=1
			siguiente_operacion.correctas_seguidas = 0

		if not borrarCorrectas:
			siguiente_operacion.correctasTotales = operacion.correctasTotales
		
		siguiente_operacion.vecesIncorrecta = operacion.vecesIncorrecta
		
		return siguiente_operacion
		
	
	def AlterarFlujo(self, operacion, siguienteNivel):
		nivelActual = siguienteNivel - 1

		for mn in self.modulosNivel:
			ind= mn.ContieneTipoOperacionNivel(nivelActual, operacion.TipoOperacion)
			if ind != -1:
				on= mn.GetSiguiente(ind)
				
				if on == None:
					indexMO= self.modulosNivel.index(mn)
					indexMO+=1
					
					if indexMO== len(self.modulosNivel):
						op= BasicOperacion()
						op.TipoOperacion= operacion.TipoOperacion
						op.nivelOperacion= nivelActual
						return op
					else:
						on= self.modulosNivel[indexMO].GetPrimerOpNivel()
				
				op= BasicOperacion()
				op.TipoOperacion= on.tipo_op
				op.nivelOperacion= on.nivel
				return op
				
		op= BasicOperacion()
		op.TipoOperacion= operacion.TipoOperacion
		op.nivelOperacion= nivelActual
		return op		
		
		
	def SubidaMaximoNivel(self,op):

		if op.correctasTotales < Reglas_Fijas.MinimoPasoNivel and op.cantidadNivel>= Reglas_Fijas.CantidadPreguntasNivelError:
			return 1
		
		return 0
		
	
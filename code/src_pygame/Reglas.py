
from TipoOperacionNivel import *
from ModuloNivel import ModuloNivel
from BasicOperacion import *
from Reglas_Fijas import *
from GeneradorPreguntas import *

class Reglas:


	# pendiente 2 mayus
	# pendiente 2 otr (no hay palabras terminadas en aba en la base de datos)
	#pendiente 2 int
	#lista = list()
	
	
	def __init__(self):
		lista=list()

		with open('Ejercicios/TipoOperacionNivel.csv', 'rb') as csvfile:
			lenguajereader = csv.reader(csvfile, delimiter=';', quoting=csv.QUOTE_NONE)
			rownum=0
			for row in lenguajereader:

				if rownum == 0:
					header = row
				else:
					lista.append(TipoOperacionNivel(int(row[0]),TipoOperacionNivel.InttoTipoOperacion(int(row[1]))))

					print "agregado nivel"+row[0]						 
				rownum += 1
		'''
		lista.append(TipoOperacionNivel(1,TipoOperacion.primero))
		lista.append(TipoOperacionNivel(2,TipoOperacion.primero))
		lista.append(TipoOperacionNivel(1, TipoOperacion.primero))
		lista.append(TipoOperacionNivel(2, TipoOperacion.primero))
		lista.append(TipoOperacionNivel(3, TipoOperacion.primero))
		lista.append(TipoOperacionNivel(1, TipoOperacion.primero))
		lista.append(TipoOperacionNivel(1, TipoOperacion.primero))		
		lista.append(TipoOperacionNivel(1, TipoOperacion.primero)) # falta temporizador		
		lista.append(TipoOperacionNivel(3, TipoOperacion.primero)) # falta imagen en las palabras
		lista.append(TipoOperacionNivel(4, TipoOperacion.primero)) # pendiente 4, no hay diferencias entre palabras con r y rr
		lista.append(TipoOperacionNivel(5, TipoOperacion.primero))
		'''
		self.modulosNivel = list()
		self.modulosNivel.append(ModuloNivel(lista, "principal"))
		return		
	
	# Metodo publico que entrega la siguiente operacion en funcion
	# de las reglas pedagogicas. Es lo unico que se puede acceder de
	# la clase Reglas
	def GetSiguienteOperacion(self, operacion, alumno):
		
		print "correcta:"+str(operacion.respuesta_correcta)	
		if (not operacion.respuesta_correcta)  and (operacion.CantidadVecesIncorrectaSoloEsta <= 2) and (operacion.feedback_correcto != "First") :
			print "misma operacion"
			return operacion
		
		
		operacion.cantidadMaximaNivel= max(Reglas_Fijas.MaximoNivel, operacion.cantidadMaximaNivel)
		
		siguiente_nivel = operacion.nivelOperacion
		cantidad_nivel = operacion.cantidadNivel
		cantidad_maxima_nivel = operacion.cantidadMaximaNivel
		borrarCorrectas = False
		tipoActual = operacion.TipoOperacion;
		
		cambia_nivel= Reglas_Fijas.CambioNivel(operacion)
		
		if cambia_nivel == CambioNivel.Sube:
			borrarCorrectas = True
			siguiente_nivel+=1
			cantidad_nivel = 1
			op= self.AlterarFlujo(operacion, siguiente_nivel)
			tipoActual = op.TipoOperacion
			siguiente_nivel = op.nivelOperacion
		
		elif cambia_nivel == CambioNivel.Mantiene:
			cantidad_maxima_nivel += self.SubidaMaximoNivel(operacion)
			cantidad_nivel+=1
		
		siguiente_operacion= None
		generador= GeneradorPreguntas()
		generador.SetAlumno(alumno)
		siguiente_operacion = generador.Getsiguiente(siguiente_nivel)

		if borrarCorrectas:
			siguiente_operacion.cambio_reciente_nivel= True

		print "zzoperacion generada"
		'''
		if tipoActual == TipoOperacion.primero:
			if siguiente_nivel==1:
				siguiente_operacion = generador.generador_mayus_nombres_propios1()
			elif siguiente_nivel==2:
				siguiente_operacion = generador.generador_mayus_nombres_propios2()
				
		if tipoActual == TipoOperacion.segundo:
			if siguiente_nivel==1:
				siguiente_operacion = generador.generador_patrones_ort_comunes1()
			elif siguiente_nivel==2:
				siguiente_operacion = generador.generador_patrones_ort_comunes2()
			elif siguiente_nivel==3:
				siguiente_operacion = generador.generador_patrones_ort_comunes3()
			elif siguiente_nivel==4:
				siguiente_operacion = generador.generador_patrones_ort_comunes4()
			elif siguiente_nivel==5:
				siguiente_operacion = generador.generador_patrones_ort_comunes5()
				
		if tipoActual == TipoOperacion.tercero:
			if siguiente_nivel==1:
				siguiente_operacion = generador.generador_reproduccion_letras_alfabeto1()
			elif siguiente_nivel==2:
				siguiente_operacion = generador.generador_reproduccion_letras_alfabeto2()
				
		if tipoActual == TipoOperacion.cuarto:
			if siguiente_nivel==1:
				next_num= random.randrange(1,3)
				siguiente_operacion = generador.generador_sentido_vocales1(next_num)
				
			elif siguiente_nivel==2:
				next_num= random.randrange(1,10)
				siguiente_operacion = generador.generador_sentido_vocales2(next_num)
			
			elif siguiente_nivel==3:
				next_num= random.randrange(1,4)
				siguiente_operacion = generador.generador_sentido_vocales3(next_num)
			
		if tipoActual == TipoOperacion.quinto:
			if siguiente_nivel==1:
				if operacion.TipoOperacion == TipoOperacion.sentido_vocales_silabas:
					siguiente_operacion = generador.generador_signos_int_excl1(False)
				else:
					siguiente_operacion = generador.generador_signos_int_excl1(True)
			elif siguiente_nivel==2:
				siguiente_operacion = generador.generador_signos_int_excl2()
		'''

		print "siguiente nivel: "+str(siguiente_nivel)
		print "nivel operacion: "+ str(operacion.nivelOperacion)

		if siguiente_nivel == operacion.nivelOperacion:
			print "zz adentro"
			siguiente_operacion.cantidadMaximaNivel= cantidad_maxima_nivel
			print "zz adentro mas"
			siguiente_operacion.puntajesNivel= operacion.puntajesNivel
			siguiente_operacion.AgregarPuntajesNivel(operacion.puntajesNivel, operacion.puntaje)

			siguiente_operacion.cantidadNivel= cantidad_nivel
		else:
			siguiente_operacion.cantidadNivel=1
		
		print "zz otra pos"

		if not borrarCorrectas:
			siguiente_operacion.correctasTotales = operacion.correctasTotales
		
		siguiente_operacion.vecesIncorrecta = operacion.vecesIncorrecta
		
		print "zzotro marker"

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
		
	
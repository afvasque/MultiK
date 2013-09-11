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
		#self.interpal= Generador_pal("clase de prueba")
		#self.interor= Generador_or("clase de prueba")

		if self.preguntas is None:

			print "entro"
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
								print "agregada"
								operacion.alternativas.append(row[x].decode('latin-1'))
								print row[x].decode('latin-1')

						operacion.respuesta= row[5].decode('latin-1')
						operacion.audio_pregunta= row[6].decode('latin-1')
						operacion.path_imagen= row[7].decode('latin-1')

						self.preguntas.append(operacion)
						print "agregada "+operacion.pregunta						
							 
					rownum += 1

		return
	
	def Getsiguiente(self, niveloperacion):
		operaciones= filter(lambda x: x.nivelOperacion== niveloperacion,self.preguntas)

		rand= random.randint(0, len(operaciones)-1)
		print "random"+str(rand)
		print "operaciones"+str(len(operaciones))
		operacion= operaciones[rand]

		for x in operaciones:
			print "lista: "+x.audio_pregunta

		operacion.TipoOperacion = TipoOperacion.primero
		operacion.feedback_correcto = "Bien, " + self.alumno.Nombre
		operacion.feedback_error = "Inténtalo de nuevo"
		print "op: "+operacion.audio_pregunta
		return operacion

'''
	def generador_reproduccion_letras_alfabeto1(self):
		
		letra= self.interpal.generador_letra_alfabeto()
		print "generando operacion letra"
		operacion= BasicOperacion()
		operacion.respuesta= letra
		
		letra= self.ReemplazoLetras(letra)
		
		operacion.TipoOperacion = TipoOperacion.primero
		operacion.nivelOperacion = 1
		operacion.audio_pregunta = "Presiona la letra. %s" % letra
		operacion.pregunta = "Presiona la letra... "
		operacion.feedback_correcto = "Bien, " + self.alumno.Nombre
		operacion.feedback_error = "Inténtalo de nuevo"
					
		return operacion


	def ReemplazoLetras(self, letra):
		if letra == "w":
			letra = "doble b"
		if letra == "v":
			letra = "b corta"
		if letra == "y":
			letra = "y griega"
		return letra
	
	def generador_reproduccion_letras_alfabeto2(self):
		
		letra= self.interpal.generador_letra_alfabeto()
		
		operacion= BasicOperacion()
		operacion.TipoOperacion = TipoOperacion.Reproduccion_letras_alfabeto
		operacion.nivelOperacion = 2
		operacion.audio_pregunta = "Busca la letra. "+self.ReemplazoLetras(letra)
		operacion.feedback_correcto = "Bien \n" + self.alumno.Nombre
		operacion.feedback_error = "Inténtalo \nde nuevo"
		
		resp= self.interpal.generador_palabra_contiene(letra)
		alt1= self.interpal.generador_palabra_no_contine(letra)
		alt2= self.interpal.generador_palabra_no_contine(letra)
		
		operacion.alternativas.append(resp)
		operacion.alternativas.append(alt1)
		operacion.alternativas.append(alt2)
		operacion.respuesta= operacion.alternativas[0]
		
		random.shuffle(operacion.alternativas)
		
		return operacion
		
		
	def generador_sentido_vocales1(self, silabas):
		
		temp= silabas-1
		
		if temp<1:
			temp=2
			
		operacion= BasicOperacion()
		operacion.TipoOperacion= TipoOperacion.sentido_vocales_silabas
		operacion.nivelOperacion=1
		#operacion.audio_pregunta= "Selecciona la palabra con " + str(silabas) + " sílaba"
		
		if silabas==1:
			operacion.audio_pregunta= "Selecciona la palabra con una sílaba"
		elif silabas==2:
			operacion.audio_pregunta= "Selecciona la palabra con dos sílabas" 
		elif silabas==3:
			operacion.audio_pregunta= "Selecciona la palabra con tres sílabas" 
		elif silabas==4:
			operacion.audio_pregunta= "Selecciona la palabra con cuatro sílabas" 
		
		
		operacion.feedback_correcto= "Bien \n" + self.alumno.Nombre
		operacion.feedback_error= "Inténtalo \nde nuevo"
		operacion.alternativas.append(self.interpal.generador_palabra_silaba(silabas))
		operacion.alternativas.append(self.interpal.generador_palabra_silaba(temp))
		operacion.alternativas.append(self.interpal.generador_palabra_silaba(temp))
		operacion.respuesta= operacion.alternativas[0]
		
		random.shuffle(operacion.alternativas)
		
		return operacion
		
		
	def generador_sentido_vocales2(self, num_palabras):
		
		# las opciones son ce, ci, que, qui, ge, gi, gue, gui, güe, güi
		
		operacion= BasicOperacion()
		operacion.TipoOperacion= TipoOperacion.sentido_vocales_silabas
		operacion.nivelOperacion=2
		
		
		
		if num_palabras==1:
			self.silaba="ce"
		elif num_palabras==2:
			self.silaba="ci"
		elif num_palabras==3:
			self.silaba="que"
		elif num_palabras==4:
			self.silaba="qui"
		elif num_palabras==5:
			self.silaba="ge"
		elif num_palabras==6:
			self.silaba="gi"
		elif num_palabras==7:
			self.silaba="gue"
		elif num_palabras==8:
			self.silaba="gui"
		elif num_palabras==9:
			self.silaba="güe"
		elif num_palabras==10:
			self.silaba="güi"
		
		palabra= self.interpal.generador_palabra_contiene(self.silaba)
		operacion.audio_pregunta= "Escribe la sílaba faltante de."+palabra
		operacion.pregunta = palabra.replace(self.silaba,"___")
		operacion.respuesta= self.silaba
		
		operacion.feedback_correcto= "Bien \n" + self.alumno.Nombre
		operacion.feedback_error= "Inténtalo \nde nuevo"
		
		return operacion
		
	def generador_sentido_vocales3(self, num_palabras):
		
		# las opciones son ge, gi, je, ji
		
		operacion= BasicOperacion()
		operacion.TipoOperacion= TipoOperacion.sentido_vocales_silabas
		operacion.nivelOperacion=3
		
		
		
		if num_palabras==1:
			self.silaba="ge"
		elif num_palabras==2:
			self.silaba="gi"
		elif num_palabras==3:
			self.silaba="je"
		elif num_palabras==4:
			self.silaba="ji"
		
		
		palabra= self.interpal.generador_palabra_contiene(self.silaba)
		operacion.audio_pregunta= "Escribe la sílaba faltante de."+palabra
		operacion.pregunta = palabra.replace(self.silaba,"___")
		operacion.respuesta= self.silaba
		
		operacion.feedback_correcto= "Bien \n" + self.alumno.Nombre
		operacion.feedback_error= "Inténtalo \nde nuevo"
		
		return operacion
		
	def generador_signos_int_excl1(self, tipo_op):
		
		operacion= BasicOperacion()
		operacion.TipoOperacion= TipoOperacion.signos_int_excl
		operacion.nivelOperacion=1
		
		if tipo_op:
			operacion.audio_pregunta= "¿Cuáles son los signos de interrogación?  Recuerda que nos sirven para hacer preguntas"
			operacion.feedback_correcto = "Bien \n" + self.alumno.Nombre
			operacion.feedback_error = "Inténtalo \nde nuevo"
			operacion.respuesta = "¿,?"
			
		else:
			operacion.audio_pregunta = "¿Cuáles son los signos de exclamación?  Recuerda que nos sirven para expresar sentimientos y emociones"
			operacion.feedback_correcto = "Bien \n" + self.alumno.Nombre
			operacion.feedback_error = "Inténtalo de nuevo"
			operacion.respuesta = "¡,!"
		
		return operacion
	
	# Pendiente!!
	def generador_signos_int_excl2(self):
		
		azar= random.randrange(0,2)
		num= True
		
		if azar == 0:
			num=False
			
		pregunta= self.interor.generador_pregunta_exclamacion(num)
				
		operacion= BasicOperacion()
		operacion.TipoOperacion= TipoOperacion.signos_int_excl
		operacion.nivelOperacion=2
		operacion.audio_pregunta= pregunta
		operacion.feedback_correcto = "Bien \n" + self.alumno.Nombre
		operacion.feedback_error = "Inténtalo \nde nuevo"
		
		if num==True:
			operacion.respuesta= "¿?"
		else:
			operacion.respuesta = "¡!"
				   
		return operacion
	
	def generador_mayus_nombres_propios1(self):
		
		operacion= BasicOperacion()
		
		operacion.TipoOperacion = TipoOperacion.primero
		operacion.nivelOperacion = 1
		operacion.feedback_correcto = "Bien \n" + self.alumno.Nombre
		operacion.audio_pregunta = "Selecciona el sustantivo propio"
		operacion.feedback_error = "Inténtalo \nde nuevo"
		sust_propio = self.interpal.generador_sust_propio(True) #La primera letra es mayuscula
		print "sustantivo: "+sust_propio
		
		#operacion.alternativas.append(sust_propio)
		operacion.alternativas.append(self.interpal.generador_sust_propio(True))
		operacion.alternativas.append(self.interpal.generador_sust_propio(False))
		operacion.alternativas.append(self.interpal.generador_sust_propio(False))
		operacion.respuesta= operacion.alternativas[0]
		
		random.shuffle(operacion.alternativas)
		
		return operacion
	
	# Pendiente!
	def generador_mayus_nombres_propios2(self):
		
		operacion= BasicOperacion()
		operacion.TipoOperacion= TipoOperacion.mayus_nombres_propios
		operacion.nivelOperacion=2
		operacion.feedback_correcto = "Bien \n" + self.alumno.Nombre
		operacion.feedback_error = "Inténtalo \nde nuevo"
		
		pregunta = self.interor.generador_oracion_propio_comun();
		
		operacion.pregunta= pregunta
		operacion.alternativas.append(self.interpal.generador_sust_propio(True))
		operacion.alternativas.append(self.interpal.generador_sust_propio(False))
		operacion.alternativas.append(self.interpal.generador_sust_propio(False))
		operacion.respuesta= operacion.alternativas[0]
		
		random.shuffle(operacion.alternativas)
		
		return operacion
	
	def generador_patrones_ort_comunes1(self):
		operacion= BasicOperacion()
		azar= random.randrange(0,2)
		alter1=""
		alter2=""
		
		if azar==0:
			alter1= self.interpal.generador_palabra_contiene("v")
			alter2= alter1.replace("v","b")
			
		else:
			alter1= self.interpal.generador_palabra_contiene("b")
			alter2= alter1.replace("b","v")
	   
		operacion.TipoOperacion= TipoOperacion.patrones_ort_comunes
		operacion.nivelOperacion=1
		operacion.feedback_correcto = "Bien \n" + self.alumno.Nombre
		operacion.feedback_error = "Inténtalo \nde nuevo"
		operacion.audio_pregunta = "Selecciona la palabra escrita correctamente"
		
		operacion.alternativas.append(alter1)
		operacion.alternativas.append(alter2)
		operacion.respuesta= operacion.alternativas[0]
		random.shuffle(operacion.alternativas)         
		
		return operacion;
	
	def generador_patrones_ort_comunes2(self):
		operacion= BasicOperacion()
		
		respuesta= self.interpal.generador_palabra_contiene("aba")
		
		while respuesta[len(respuesta-4):len(respuesta)-1] != "aba":
			respuesta= self.interpal.generador_palabra_contiene("aba")
		pregunta= respuesta.replace("aba","___")
		
		operacion.TipoOperacion = TipoOperacion.patrones_ort_comunes
		operacion.nivelOperacion = 2
		operacion.feedback_correcto = "Bien \n" + self.alumno.Nombre
		operacion.feedback_error = "Inténtalo \nde nuevo"
		operacion.audio_pregunta = "Los verbos terminados en aba se escriben con b y nos indican que una acción ocurrió en el pasado"
		operacion.pregunta = pregunta
		operacion.respuesta = respuesta;
			  
		return operacion
		
		# pendiente
	def generador_patrones_ort_comunes3(self):
		
		operacion= BasicOperacion()
		
		respuesta = self.interpal.generador_palabra_contiene("mb")
		pregunta = respuesta.replace("mb", "__")
		operacion.TipoOperacion = TipoOperacion.patrones_ort_comunes
		operacion.nivelOperacion = 3
		operacion.feedback_correcto = "Bien \n" + self.alumno.Nombre
		operacion.feedback_error = "Inténtalo \nde nuevo"
		operacion.audio_pregunta = "Escoge la combinación que corresponde para cada palabra"
		operacion.pregunta = pregunta
		operacion.respuesta = "mb"
		
		operacion.alternativas.append("mb")
		operacion.alternativas.append("mp")
		operacion.alternativas.append("nv")
		
		random.shuffle(operacion.alternativas)
		
		return operacion
	
	#pendiente
	def generador_patrones_ort_comunes4(self):
		
		operacion= BasicOperacion()
		
		operacion.TipoOperacion = TipoOperacion.patrones_ort_comunes
		operacion.nivelOperacion = 4
		operacion.feedback_correcto = "Bien \n" + self.alumno.Nombre
		operacion.feedback_error = "Inténtalo \nde nuevo"
		operacion.audio_pregunta = "Selecciona la palabra con la combinación doble erre"
		operacion.alternativas.append(self.interpal.generador_palabra_contiene("rr"))
		operacion.alternativas.append(self.interpal.generador_palabra_contiene("r"))
		
		while "rr" in operacion.alternativas[1]:
			operacion.alternativas[1] = self.interpal.generador_palabra_contiene("r");
		operacion.respuesta = operacion.alternativas[0]
		
		random.shuffle(operacion.alternativas)

		return operacion    
	
	def generador_patrones_ort_comunes5(self):
		
		operacion= BasicOperacion()
		
		operacion.TipoOperacion = TipoOperacion.patrones_ort_comunes
		operacion.nivelOperacion = 5
		operacion.feedback_correcto = "Bien \n" + self.alumno.Nombre
		operacion.feedback_error = "Inténtalo \nde nuevo"
		operacion.pregunta = ""
		operacion.respuesta = self.interpal.generador_sust_propio(False)
		operacion.audio_pregunta = "Escribe la palabra: " + operacion.respuesta
		
		return operacion   
'''
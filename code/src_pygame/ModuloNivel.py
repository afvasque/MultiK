

from TipoOperacionNivel import *

#Lista de los tipos de operaciones que posee
tipoOperaciones= list()

#Detalle de que operaciones y niveles posee
nivelesTipoOperacion= list()

class ModuloNivel:


	def GenerarOperandosContenidos(self):
		for i in range(0,len(nivelesTipoOperacion)-1):
			if not nivelesTipoOperacion[i].tipo_op in tipoOperaciones:
				tipoOperaciones.append(nivelesTipoOperacion[i].tipo_op)
 

	# Constructor de un modulo
	def __init__(self, lista,nombre=""):

		#Nombre del modulo, en el que se explica los contenidos pedagogicos de las reglas que contiene
		self.nombre = nombre;
		
		for on in lista:
			nivelesTipoOperacion.append(on);
		self.GenerarOperandosContenidos()
		
			
		

	def ContieneTipoOperacionNivel(self, nivel, op):
		if op in tipoOperaciones:
			for on in nivelesTipoOperacion:
				if on.IsOpNivel(nivel,op):
					return nivelesTipoOperacion.index(on)
		return -1


	def GetSiguiente(self, indexOf):
		if len(nivelesTipoOperacion)-1 == indexOf:
			return TipoOperacionNivel.TipoOpGlobal
		else:
			return nivelesTipoOperacion[int(indexOf)+1]


	def GetPrimerOpNivel(self):
		return nivelesTipoOperacion[0]

		
	
		

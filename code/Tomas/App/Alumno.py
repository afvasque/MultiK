class Alumno:
	def __init__(self,id):
		self.id = id
		self.name = ""
		self.audio = ""
		self.ready = False
		self.grupo = -1
		self.real = True
		
	def set_nombre(self, numero_lista):
		if numero_lista == 17090326:
			self.name = "bot"
			self.real = False
		else:
			lista_alumnos = LectorCSV.getInstance().alumnos
			if numero_lista in lista_alumnos:
				self.name = lista_alumnos[numero_lista]
			else:
				self.name = "Alumno"
		
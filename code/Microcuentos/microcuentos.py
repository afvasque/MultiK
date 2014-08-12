class Jugador:

	def __init__(self, nombre,identificador):
		self.nombre = nombre
		self.identificador = identificador
		#self.texto_exhibido = ""
		self.texto_nuevo = ""


class Microcuento:
	
	def __init__(self):
		self.iteracion = 0
		#self.numJ = numJ
		#self.listaJ = listaJ
		#self.listaC = listaC

	def run(self,numJ,listaJ,listaC):
		turno = 0
		Ejecutar = True

		while Ejecutar:
			print("Turno:"+str(turno))
			contador = 0

			for i in range(0,numJ):

				x=(i-turno)%numJ    					#iterador que seleccionara el cuento del anterior jugador y asi con cada turno 
				jugador_actual = listaJ[i]

				print("Jugador " + str(i) + ": " + jugador_actual.nombre + " es su turno.")
				print("No ingrese texto para terminar. Finalizará si ningun jugador en este turno ha ingresado texto.\n")

				if turno == 0:
					print ("Escriba la primera oracion del microcuento: ")
					jugador_actual.texto = input()
					if jugador_actual.texto == "":
						jugador_actual.texto = "\n"
						contador +=1

					cuento_actual = [jugador_actual.texto]
					listaC.append(cuento_actual)						#se crean los numJ cuentos


				else:
					cuento_actual = listaC[x]
					a=len(cuento_actual)-1
					print("Oracion anterior: ", cuento_actual[a])
					print("Continue con otra oracion del microcuento:")
					jugador_actual.texto = input()
					if jugador_actual.texto == "":
						jugador_actual.texto = "\n"
						contador +=1
						
					cuento_actual.append(jugador_actual.texto)

				print("\n\n")

			if contador == numJ:
				Ejecutar = False
			turno += 1

		iteracion = 0
		for c in listaC:
			c = "\n ".join(c)
			print("El cuento", iteracion, "es:\n", c,"\n")
			iteracion += 1

	

#

#

#

#

#inicio del programa

print("Ingrese la cantidad de jugadores:")
numJ = int(input())

lista_cuentos = []
lista_jugadores = []

for m in range(0,numJ):           									#creamos los jugadores
	print("Ingrese el nombre del Jugador" + str(m) + ": ")
	nombre = input()
	jugador_creado = Jugador(nombre,m)
	lista_jugadores.append(jugador_creado)
	
print("\n------------o------------\n")	
p = Microcuento()
p.run(numJ,lista_jugadores,lista_cuentos)

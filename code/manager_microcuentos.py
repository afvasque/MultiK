# -*- coding: utf-8 -*-

import manejo_pantalla
import random
import threading
import logging

logging.basicConfig(filename='multik.log',level=logging.INFO)

class Jugador:

	def __init__(self, id_teclado, id_audifono):
		self.id_teclado = id_teclado
		self.id_audifono = id_audifono
		self.texto_nuevo = ""
		# ID del ultimo cuento donde escribio
		self.ultimo_ingresado = -1
		self.status = "START"
		self.waiting_flag = False 

class ManagerMicrocuentos:

	def __init__(self, lib_audio, lib_teclados):
		self.lib_audio = lib_audio
		self.lib_teclados = lib_teclados

		self.lista_cuentos = {}
		self.lista_jugadores = {}


	def add_player(self, id_teclado, id_audifono):
		jugador_creado = Jugador(id_teclado, id_audifono)
		self.lista_jugadores[id_teclado] = jugador_creado

	def verificar_respuesta(self, id_teclado, text):
		if len(self.lista_cuentos) == 0:
			self.iniciar_juego()
		else:
			self.instrucciones(id_teclado, text)

	def iniciar_juego(self):
		# Incializar lista de cuentos
		for j in list(self.lista_jugadores.values()):
			self.lista_cuentos[j.id_teclado] = []
			self.instrucciones(j.id_teclado, "")

	def esperar_cuento(self, id_teclado):
		# Tomar aleatoriamente un cuento diferente al cual recien aporte
		ultimo = self.lista_jugadores[id_teclado].ultimo_ingresado
		i = ultimo
		while i == ultimo or len(self.lista_cuentos[i]) == 0 :
			self.lista_jugadores[id_teclado].waiting_flag = True
			# Timer para bajar carga?
			i = random.choice(list(self.lista_cuentos.keys()))
		print("Actual: ", id_teclado, " ultimo ingresado: ", i)
		self.lista_jugadores[id_teclado].waiting_flag = False
		# Enviar la ultima frase
		print(self.lista_cuentos[i][-1])
		self.lib_audio.play(self.lista_jugadores[id_teclado].id_audifono, self.lista_cuentos[i][-1])
		self.lista_jugadores[id_teclado].ultimo_ingresado = i
		self.lista_jugadores[id_teclado].status = "WRITING"

	def instrucciones(self, id_teclado, text):
		try:
			# Si no hay nada, es primer turno -> escribir primera frase 
			if self.lista_jugadores[id_teclado].status == "START":
				manejo_pantalla.reset_layout(id_teclado)
				self.lib_audio.play(self.lista_jugadores[id_teclado].id_audifono, "Escribe una frase para iniciar tu micro cuento.")
				self.lista_jugadores[id_teclado].ultimo_ingresado = id_teclado
				self.lista_jugadores[id_teclado].status = "WRITING"
			# Guardar oracion anterior
			elif self.lista_jugadores[id_teclado].status == "WRITING":
				print("Jugador ", id_teclado, " en WRITING ", "ultimo: ", self.lista_jugadxores[id_teclado].ultimo_ingresado)
				self.guardar_oracion(self.lista_jugadores[id_teclado].ultimo_ingresado, text)
				self.lista_jugadores[id_teclado].status = "DONE"
				# Mensaje de espera
				if self.lista_jugadores[id_teclado].waiting_flag:
					manejo_pantalla.reset_layout(id_teclado)
					manejo_pantalla.write(id_teclado, "Esperar", 0, 0)
				else:
					manejo_pantalla.reset_layout(id_teclado)
				self.instrucciones(id_teclado, "")
			else:
				print("Jugador ", id_teclado, " en THREAD")
				t = threading.Thread(target=self.esperar_cuento, args = (id_teclado,))
				t.daemon = True
				t.start()
				
			# Pedir oracion nueva
			manejo_pantalla.draw_textbox(id_teclado,50)
			
		except Exception as e:
			print type(e)


	def guardar_oracion(self, ultimo_ingresado, oracion):
		# Guardar oracion en el cuento del grupo
		self.lista_cuentos[ultimo_ingresado].append(oracion)


	# Se llama al hacer POW en una actividad
	def replay(self, id_teclado):
		ultimo = self.lista_jugadores[id_teclado].ultimo_ingresado
		self.lib_audio.play(self.lista_jugadores[id_teclado].id_audifono, self.lista_cuentos[ultimo][-1])


# -*- coding: utf-8 -*-

import manejo_pantalla
import random
import threading
import logging
import time

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
		# y diferente al mio propio
		ultimo = self.lista_jugadores[id_teclado].ultimo_ingresado
		i = ultimo

		while (i == ultimo or i == id_teclado or len(self.lista_cuentos[i]) == 0):
			i = random.choice(list(self.lista_cuentos.keys()))

		self.lista_jugadores[id_teclado].waiting_flag = False

		# Enviar la ultima frase
		self.lib_audio.play(self.lista_jugadores[id_teclado].id_audifono, self.lista_cuentos[i][-1])
		self.lista_jugadores[id_teclado].ultimo_ingresado = i
		self.lista_jugadores[id_teclado].status = "WRITING"


	def instrucciones(self, id_teclado, text):
		try:
			# Si no hay nada, es primer turno -> escribir primera frase 
			if self.lista_jugadores[id_teclado].status == "START":
				manejo_pantalla.reset_layout(id_teclado)
				manejo_pantalla.draw_textbox(id_teclado,50)

				self.lib_audio.play(self.lista_jugadores[id_teclado].id_audifono, "Escribe una frase para iniciar tu micro cuento.")
				self.lista_jugadores[id_teclado].ultimo_ingresado = id_teclado
				self.lista_jugadores[id_teclado].status = "WRITING"
				
			# Guardar oracion anterior
			elif self.lista_jugadores[id_teclado].status == "WRITING":				
				
				# Mensaje de espera
				if not self.lista_jugadores[id_teclado].waiting_flag:
					self.lista_jugadores[id_teclado].waiting_flag = True
					self.guardar_oracion(self.lista_jugadores[id_teclado].ultimo_ingresado, text)
					manejo_pantalla.reset_layout(id_teclado)
					self.instrucciones(id_teclado, "")
				else:
					t = threading.Thread(target=self.esperar_cuento, args = (id_teclado,))
					t.daemon = True
					t.start()
					manejo_pantalla.reset_layout(id_teclado)
					manejo_pantalla.draw_textbox(id_teclado,50)						
			
		except Exception as e:
			print e


	def guardar_oracion(self, ultimo_ingresado, oracion):
		# Guardar oracion en el cuento del grupo
		self.lista_cuentos[ultimo_ingresado].append(oracion)


	# Se llama al hacer POW en una actividad
	def replay(self, id_teclado):
		ultimo = self.lista_jugadores[id_teclado].ultimo_ingresado

		if len(self.lista_cuentos[ultimo]) > 0:
			self.lib_audio.play(self.lista_jugadores[id_teclado].id_audifono, self.lista_cuentos[ultimo][-1])
		else:
			self.lib_audio.play(self.lista_jugadores[id_teclado].id_audifono, "Escribe una frase para iniciar tu microcuento.")

	
	def audio_cuento_final(self, id_teclado, id_audifono):
		bienvenida = "Microcuento. Jugador " + str(id_teclado) + "."
		self.lib_audio.play(self.lista_jugadores[id_teclado].id_audifono, bienvenida)
		# Explicar esto en paper
		#time.sleep(1)
		result = ""
		for piece in self.lista_cuentos[id_teclado]:
			result += piece + ". "
		self.lib_audio.play(self.lista_jugadores[id_teclado].id_audifono, result)
			# Explicar esto en paper
			#time.sleep(1)
		logging.info("[%f: [%s, %s, %s] ], " % (time.time(), 'END MICROTALES AUDIO', id_teclado, id_audifono))


	def leer_cuento_final(self):
		# Generar archivo de texto con el microcuento
		for jugador in self.lista_jugadores.values():
			logging.info("[%f: [%s, %s, %s] ], " % (time.time(), 'START MICROTALES TEXTFILES', jugador.id_teclado, jugador.id_audifono))
			filename = "microcuento_" + str(jugador.id_teclado)
			with open(filename, 'wb') as f:
				for piece in self.lista_cuentos[jugador.id_teclado]:
					f.write(piece + "\n")
			logging.info("[%f: [%s, %s, %s] ], " % (time.time(), 'END MICROTALES TEXTFILES', jugador.id_teclado, jugador.id_audifono))

		
		
		# Reproducir microcuento
		for jugador in self.lista_jugadores.values():
			logging.info("[%f: [%s, %s, %s] ], " % (time.time(), 'START MICROTALES AUDIO', jugador.id_teclado, jugador.id_audifono))
			t = threading.Thread(target=self.audio_cuento_final, args=(jugador.id_teclado,jugador.id_audifono))
			t.start()
			# Explicar esto en paper
			#time.sleep(1)

		# Explicar esto en paper -> si no lo pongo, sale exception bad file descriptor
		#time.sleep(1)

			
		

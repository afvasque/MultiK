# -*- coding: utf-8 -*-

import manejo_pantalla

class ManagerMicrocuentos:

	def __init__(self, lib_audio, lib_teclados):
		self.lib_audio = lib_audio
		self.lib_teclados = lib_teclados
		self.pareamientos = {}

	def add_player(self, id_teclado, id_audifono):
		self.pareamientos[id_teclado] = id_audifono

	def verificar_respuesta(self, id_teclado):
		manejo_pantalla.reset_layout(id_teclado)
		manejo_pantalla.draw_textbox(id_teclado,50)
		self.lib_audio.play(self.pareamientos[id_teclado], "Hola!")

	def replay(self, id_teclado):
		self.lib_audio.play(self.pareamientos[id_teclado], "Última instrucción!")


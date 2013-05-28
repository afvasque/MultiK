import random
from socket import *
import sys
import multiprocessing
from threading import Thread


class Generador_pal:
	
	def __init__(self, archivo):
		self.archivo=archivo
		'''
		HOST = 'localhost'
		PORT = 7388
		self.BUFSIZE = 1024
		ADDR = (HOST, PORT)

		self.tcpCliSock = socket()
		self.tcpCliSock.connect(ADDR)

		print 'conectando'
		data = "SustantivosFinal.multik"
		self.tcpCliSock.send(data)


		print 'recibiendo1'
		data = self.tcpCliSock.recv(self.BUFSIZE)
		if not data: sys.exit(0)
		print data


		print 'conectando'
		data = "30/1"
		self.tcpCliSock.send(data)

		print 'recibiendo2'
		data = self.tcpCliSock.recv(self.BUFSIZE)
		if not data: sys.exit(0)
		print data
		'''
		
		return
	
	def generador_letra_alfabeto(self):

		return "a"

		data = "1/1"
		self.tcpCliSock.send(data)

		data = self.tcpCliSock.recv(self.BUFSIZE)
		if not data: sys.exit(0)

		temp= data.split('/')
		return temp[1]

	
	def generador_palabra_contiene(self, letra):

		return "a"

		data = "1/2/"+letra
		self.tcpCliSock.send(data)

		data = self.tcpCliSock.recv(self.BUFSIZE)
		if not data: sys.exit(0)

		temp= data.split('/')

		return temp[1]
		
	def generador_palabra_no_contine(self, letra):

		return "a"

		data = "1/3/"+letra
		self.tcpCliSock.send(data)

		data = self.tcpCliSock.recv(self.BUFSIZE)
		if not data: sys.exit(0)

		temp= data.split('/')

		return temp[1]
	
	def generador_palabra_silaba(self, silaba):
		
		return "a"

		data = "1/4/"+silaba
		self.tcpCliSock.send(data)

		data = self.tcpCliSock.recv(self.BUFSIZE)
		if not data: sys.exit(0)

		temp= data.split('/')

		return temp[1]
		
	def generador_sust_propio(self,propio):
		return "a"
		
		data = "1/5/"+propio
		self.tcpCliSock.send(data)

		data = self.tcpCliSock.recv(self.BUFSIZE)
		if not data: sys.exit(0)

		temp= data.split('/')

		return temp[1]
		
		
		
class Generador_or:
	
	def __init__(self, archivo):
		self.archivo=archivo
		
	def generador_pregunta_exclamacion(self, num):
		return "pregunta "+num
	
	def generador_oracion_propio_comun(self):
		return "oracion propio comun"
	
	
	
	
	
	
	
	
	
		

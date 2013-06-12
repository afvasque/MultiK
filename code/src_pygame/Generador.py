import random
from socket import *
import sys
import multiprocessing
from threading import Thread

## Singleton class
#
class Generador_pal:
	## Stores the unique Singleton instance-
	_iInstance = None
 
	## Class used with this Python singleton design pattern
	#  @todo Add all variables, and methods needed for the Singleton class below
	class Singleton:
		def __init__(self, archivo):
			self.archivo=archivo
			
			HOST = 'localhost'
			PORT = 7388
			self.BUFSIZE = 1024
			ADDR = (HOST, PORT)

			self.tcpCliSock = socket()
			self.tcpCliSock.connect(ADDR)

			print 'conectando'
			data = "Biblioteca.multik"
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


		def generador_letra_alfabeto(self):

			data = "1/1"
			self.tcpCliSock.send(data)

			data = self.tcpCliSock.recv(self.BUFSIZE)
			print data
			
			if not data: sys.exit(0)

			temp= data.split('/')
			
			return temp[1]

		
		def generador_palabra_contiene(self, letra):

			data = "1/2/"+letra
			self.tcpCliSock.send(data)

			data = self.tcpCliSock.recv(self.BUFSIZE)
			data = data.decode('utf8')
			if not data: sys.exit(0)

			temp= data.split('/')

			return temp[1]
			
		def generador_palabra_no_contine(self, letra):

			data = "1/3/"+letra
			self.tcpCliSock.send(data)

			data = self.tcpCliSock.recv(self.BUFSIZE)
			data = data.decode('utf8')
			if not data: sys.exit(0)

			temp= data.split('/')

			return temp[1]
		
		def generador_palabra_silaba(self, silaba):

			data = "1/4/"+str(silaba)
			self.tcpCliSock.send(data)

			data = self.tcpCliSock.recv(self.BUFSIZE)
			data = data.decode('utf8')
			if not data: sys.exit(0)

			temp= data.split('/')

			return temp[1]
			
		def generador_sust_propio(self,propio):
			
			data = "1/5/"+str(propio)
			self.tcpCliSock.send(data)

			data = self.tcpCliSock.recv(self.BUFSIZE)
			data = data.decode('utf8')
			if not data: sys.exit(0)

			temp= data.split('/')

			return temp[1]
			
 
	## The constructor
	#  @param self The object pointer.
	def __init__( self, archivo ):
		# Check whether we already have an instance
		if Generador_pal._iInstance is None:
			# Create and remember instanc
			Generador_pal._iInstance = Generador_pal.Singleton(archivo)
 
		# Store instance reference as the only member in the handle
		self._EventHandler_instance = Generador_pal._iInstance
 
 
	## Delegate access to implementation.
	#  @param self The object pointer.
	#  @param attr Attribute wanted.
	#  @return Attribute
	def __getattr__(self, aAttr):
		return getattr(self._iInstance, aAttr)
 
 
	## Delegate access to implementation.
	#  @param self The object pointer.
	#  @param attr Attribute wanted.
	#  @param value Vaule to be set.
	#  @return Result of operation.
	def __setattr__(self, aAttr, aValue):
		return setattr(self._iInstance, aAttr, aValue)

		
		
		
class Generador_or:
	
	def __init__(self, archivo):
		self.archivo=archivo
		
	def generador_pregunta_exclamacion(self, num):
		return "pregunta "+str(num)
	
	def generador_oracion_propio_comun(self):
		return "oracion propio comun"
	
	
	
	
	
	
	
	
	
		

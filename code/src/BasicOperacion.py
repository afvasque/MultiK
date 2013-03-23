from Reglas_Fijas import *

class BasicOperacion:
    
        
    def __init__(self):
        self.operacionTotal = ""
        self.nivelOperacion = 3
        self.puntajesNivel = list()
        self.cantidadNivel = 0
        self.cantidadMaximaNivel = None
        self.vecesIncorrecta = 0
        self.CantidadVecesIncorrectaSoloEsta = 0
        self.correctasTotales = 0
        self.numeroSesion = -1
        self.puntaje = -1
        self.respuesta_correcta = False
        self.TipoOperacion= None

        self.alternativas = list()
        self.pregunta = ""
        self.respuesta = ""
        self.audio_pregunta = ""
        self.feedback_correcto = ""
        self.feedback_error=""

        return
    
    def AgregarPuntajesNivel(self, listvieja, nuevoPuntaje):
        
        if listvieja != None:
            for i in listvieja:
                self.puntajesNivel.append(i)
                
        self.puntajesNivel.append(nuevoPuntaje)
                
    def RespuestaCorrecta(self):
        
        if self.CantidadVecesIncorrectaSoloEsta==0:
            self.correctasTotales+=1
            
            self.respuesta_correcta=True
            
            self.SetearPuntaje()
        
    def SetearPuntaje(self):
        
        if self.CantidadVecesIncorrectaSoloEsta >=2:
            self.puntaje=0
        else:
            self.puntaje= 2- self.CantidadVecesIncorrectaSoloEsta
        
    def RespuestaIncorrecta(self):
        
        self.vecesIncorrecta+=1
        self.CantidadVecesIncorrectaSoloEsta+=1
        
        if self.cantidadMaximaNivel < Reglas_Fijas.CantidadPreguntasNivelError:
            self.cantidadMaximaNivel= Reglas_Fijas.CantidadPreguntasNivelError
            
        self.cantidadNivel+=1
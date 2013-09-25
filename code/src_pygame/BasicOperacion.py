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
        self.cambio_reciente_nivel = False;
        self.TipoOperacion= None

        self.alternativas = list()
        self.pregunta = ""
        self.respuesta = ""
        self.audio_pregunta = ""
        self.feedback_correcto = ""
        self.feedback_error=""
        self.path_imagen = ""
        self.contenido = ""
        self.instrucciones_generales = ""

        return
    
    def AgregarPuntajesNivel(self, listvieja, nuevoPuntaje):
        
        print "largo: "+str(len(self.puntajesNivel))

        
        self.puntajesNivel.append(nuevoPuntaje)
                
    def RespuestaCorrecta(self):
        self.respuesta_correcta=True
        if self.feedback_correcto != "First":
            self.cantidadNivel+=1
        self.SetearPuntaje()

        if self.CantidadVecesIncorrectaSoloEsta==0:
            self.correctasTotales+=1                       
            
            
        
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

    def GetControlType(self):
        
        if len(self.alternativas)>0:
            return "Lista"
        else:
            return "Texto"

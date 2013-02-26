
class BasicOperacion:
    operacionTotal = ""
    nivelOperacion = 0
    puntajesNivel = list()
    cantidadNivel = 0
    cantidadMaximaNivel = None
    vecesIncorrecta = 0
    CantidadVecesIncorrectaSoloEsta = 0
    correctasTotales = 0
    numeroSesion = -1
    puntaje = -1
    respuesta_correcta = False
    TipoOperacion= None

    alternativas = list()
    pregunta = ""
    respuesta = ""
    audio_pregunta = ""
    feedback_correcto = ""
    feedback_error=""
    
    
    def __init__(self):
        return
    
    def AgregarPuntajesNivel(self, listvieja, nuevoPuntaje):
        
        if listvieja is not None:
            for i in listvieja:
                self.puntajesNivel.append(i)
                
        self.puntajesNivel.append(nuevoPuntaje)
                

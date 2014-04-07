from TipoOperacionNivel import *

class Reglas_Fijas:
    #Cantidad maxima de operaciones por nivel
    MaximoNivel = 5
    #Cantidad de buenas que debe tener un niño para pasar de nivel
    MinimoPasoNivel = 10
    #Cantidad de preguntas cuando hay un error
    CantidadPreguntasNivelError = 15
    #Buenas seguidas
    BuenasSeguidas = 5
    
    @staticmethod
    def StringToTipoOperacion(tipoOperacion):
        if tipoOperacion== "primero":
            return TipoOperacion.primero
        elif tipoOperacion=="segundo":
            return TipoOperacion.segundo
        elif tipoOperacion=="tercero":
            return TipoOperacion.tercero
        elif tipoOperacion=="cuarto":
            return TipoOperacion.cuarto
        elif tipoOperacion=="quinto":
            return TipoOperacion.quinto
        else:
            return TipoOperacion.sexto

    @staticmethod
    def CambioNivel(operacion):
        siguiente_nivel = operacion.nivelOperacion
        cantidad_nivel = operacion.cantidadNivel
        cantidad_maxima_nivel = operacion.cantidadMaximaNivel
        correctas_seguidas = operacion.correctas_seguidas
        to_return = CambioNivel.Mantiene        
    
        # Si ha contestado menos de las mínimas
        if operacion.correctasTotales < Reglas_Fijas.MinimoPasoNivel and cantidad_nivel>= Reglas_Fijas.CantidadPreguntasNivelError :
            return CambioNivel.Mantiene
        
        #si ya no tiene que contestar más
        if operacion.correctasTotales >= Reglas_Fijas.MinimoPasoNivel and cantidad_nivel >= Reglas_Fijas.CantidadPreguntasNivelError and  correctas_seguidas >= Reglas_Fijas.BuenasSeguidas:
            to_return = CambioNivel.Sube
            
        return to_return
            
        
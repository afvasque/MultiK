from TipoOperacionNivel import *

class Reglas_Fijas:
    #Cantidad maxima de operaciones por nivel
    MaximoNivel = 5

    #Cantidad de buenas que debe tener un niño para pasar de nivel
    MinimoPasoNivel = 3
    #Cantidad de preguntas cuando hay un error
    CantidadPreguntasNivelError = 1

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
        print "cantidad: "+str(cantidad_nivel)
        print "maximo: "+str(cantidad_maxima_nivel)
        to_return = CambioNivel.Mantiene
        
        # En caso de que tenga buena prgeunta de exclamación, pasa directo a interrogacioń
        #if operacion.TipoOperacion == TipoOperacion.signos_int_excl and operacion.nivelOperacion==1 and "?" in operacion.respuesta:
        #    return CambioNivel.Sube
        
        # Si ha contestado menos de las mínimas
        if operacion.correctasTotales < Reglas_Fijas.MinimoPasoNivel and cantidad_nivel>= Reglas_Fijas.CantidadPreguntasNivelError :
            return CambioNivel.Mantiene
        
        #si ya no tiene que contestar más
        if cantidad_nivel +1 > cantidad_maxima_nivel:
            to_return= CambioNivel.Sube
        elif operacion.correctasTotales >= Reglas_Fijas.MinimoPasoNivel and cantidad_nivel >= Reglas_Fijas.CantidadPreguntasNivelError:
            to_return = CambioNivel.Sube
            
        return to_return
            
          


'''	
			
			
        /// <summary>
        /// Traduce de un string a Enum Pperando
        /// </summary>
        /// <param name="TipoOperacion">Suma, Resta, Division, Multiplicacion</param>
        /// <returns>TipoOperacion.Suma, TipoOperacion.Resta, TipoOperacion.Division, TipoOperacion.Multiplicacion</returns>
        public static TipoOperacion StringToTipoOperacion(string tipoOperacion)
        {
            switch (tipoOperacion)
            {
                case "mayus_nombres_propios": { return TipoOperacion.mayus_nombres_propios; }
                case "patrones_ort_comunes": { return TipoOperacion.patrones_ort_comunes; }
                case "Reproduccion_letras_alfabeto": { return TipoOperacion.Reproduccion_letras_alfabeto; }
                case "sentido_vocales_silabas": { return TipoOperacion.sentido_vocales_silabas; }
                case "signos_int_excl": { return TipoOperacion.signos_int_excl; }
                default: { return TipoOperacion.mayus_nombres_propios; }
            }
        }

     

        public static IEnumerable<T> Randomize<T>(this IEnumerable<T> source)
        {
            Random rnd = new Random();
            return source.OrderBy<T, int>((item) => rnd.Next());
        }
    }
}
'''
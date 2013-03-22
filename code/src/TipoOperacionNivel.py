


class TipoOperacion:
    Reproduccion_letras_alfabeto=1
    sentido_vocales_silabas=2
    signos_int_excl=3
    mayus_nombres_propios=4
    patrones_ort_comunes=5
    

# Establece que sucede con el nivel del alumno    
class CambioNivel:
    Mantiene=1
    Sube=2

class TipoOperacionNivel:
    
    TipoOpGlobal= None
    NivelGlobal= None
    
    def __init__(self, nivel, tipo_op):
        self.nivel = nivel
        self.tipo_op = tipo_op
        self.notNull= True
        TipoOpGlobal= tipo_op
        NivelGlobal= nivel

    '''


    /// <summary>
    /// Estructura que contiene un Tipo de Operacion y un nivel asociado
    /// </summary>
    public struct TipoOperacionNivel
    {
        #region Miembros Privados y Propiedades

        int nivel;
        /// <summary>
        /// Retorna el nivel de este tipo de operacion
        /// </summary>
        public int Nivel { get { return nivel; } }

        TipoOperacion tipoOperacion;
        /// <summary>
        /// Retorna el tipo de operacion de la estructura
        /// </summary>
        public TipoOperacion TipoOperacion { get { return tipoOperacion; } }

        bool notNull;
        /// <summary>
        /// Booleano que determina si la estructura es vacia
        /// </summary>
        public bool IsNull { get { return !notNull; } }

        #endregion


        #region Funciones

        /// <summary>
        /// Returna el tipo de la estructura
        /// </summary>
        /// <returns></returns>
        public Tuple<TipoOperacion, int> ReturnType()
        {
            return new Tuple<TipoOperacion, int>(tipoOperacion, nivel);
        }

        /// <summary>
        /// Establece si el nivel y tipoo de operación son iguales
        /// </summary>
        /// <param name="nivel"></param>
        /// <param name="op"></param>
        /// <returns></returns>
        public bool IsOpNivel(int nivel, TipoOperacion op)
        {
            return (this.nivel == nivel && tipoOperacion == op);
        }

        #endregion
    }
}
'''
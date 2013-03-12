

from TipoOperacionNivel import *

#Lista de los tipos de operaciones que posee
tipoOperaciones= list()

#Detalle de que operaciones y niveles posee
nivelesTipoOperacion= list()

class ModuloNivel:


	def GenerarOperandosContenidos(self):
		for i in range(0,len(nivelesTipoOperacion)):
			if not nivelesTipoOperacion[i].tipo_op in tipoOperaciones:
				tipoOperaciones.append(nivelesTipoOperacion[i].tipo_op)
 

	# Constructor de un modulo
	def __init__(self, niveles, tipo_op,nombre=""):
		self.niveles= niveles
		self.tipo_op= tipo_op
		#Nombre del modulo, en el que se explica los contenidos pedagogicos de las reglas que contiene
		self.nombre = nombre;
		
		for i in range(0,len(niveles)):
			nivelesTipoOperacion.append(TipoOperacionNivel(niveles[i], tipo_op[i]))
			if not tipo_op[i] in tipoOperaciones:
				tipoOperaciones.append(tipo_op[i])
				self.GenerarOperandosContenidos();
		
	def ModuloNivel(self, lista, nombre):
		nombreModulo = nombre
			
		for on in lista:
			nivelesTipoOperacion.append(on);
		self.GenerarOperandosContenidos()
		
	def GetSiguiente(self, indexOf):
		if len(nivelesTipoOperacion)-1 == indexOf:
			return TipoOperacionNivel.TipoOpGlobal
		else:
			return nivelesTipoOperacion[indexOf+1]
			

	def GetPrimerOpNivel(self):
		return nivelesTipoOperacion[0]
'''
  public TipoOperacionNivel GetSiguiente(int indexOf)
        {
            if (nivelesTipoOperacion.Count - 1 == indexOf)
            {
                return new TipoOperacionNivel();
            }
            else
            {
                return nivelesTipoOperacion[indexOf + 1];
            }
        }
'''	
		
	
		
				
		
'''
		# Determina si posee algun nivel y tipo de operacion particular
        def ContieneAlgunTipoOperacionNivel(opNiveles):
			for opNivel in opNiveles:
				if nivelesTipoOperacion.Contains(opNivel):
					return true
			return false

        

        /// <summary>
        /// Determina cual es TipoOperacionNivel en el indice elegido
        /// </summary>
        /// <param name="index">Indice que se desea buscar</param>
        /// <returns>Retorna una estructura vacia (ver atributo notNull)</returns>
        public TipoOperacionNivel GetIndex(int index)
        {
            if (index > this.CantidadNiveles() || index < 0) return new TipoOperacionNivel();
            else
            {
                return nivelesTipoOperacion[index];
            }
        }

        /// <summary>
        /// Retorna la cantidad de niveles que posee este módulo
        /// </summary>
        /// <returns></returns>
        public int CantidadNiveles()
        {
            return nivelesTipoOperacion.Count;
        }

        /// <summary>
        /// Determina la cantidad hasta un tipo de operacion y nivel. Es inclusivo
        /// </summary>
        /// <param name="nivel"></param>
        /// <param name="op"></param>
        /// <returns></returns>
        public int CantidadesHasta(int nivel, TipoOperacion op)
        {
            for (int i = 0; i < nivelesTipoOperacion.Count; i++)
            {
                if (nivelesTipoOperacion[i].IsOpNivel(nivel, op))
                {
                    return (i + 1);
                }
            }

            return 0;
        }

        /// <summary>
        /// Determina si el modulo posee un Tipo de Operacion especifico y un nivel respectivo
        /// </summary>
        /// <param name="nivel"></param>
        /// <param name="op"></param>
        /// <returns></returns>
        public int ContieneTipoOperacionNivel(int nivel, TipoOperacion op)
        {
            if (tipoOperaciones.Contains(op))
            {
                foreach (TipoOperacionNivel on in nivelesTipoOperacion)
                {
                    if (on.IsOpNivel(nivel, op))
                    {
                        return nivelesTipoOperacion.IndexOf(on);
                    }
                }
            }

            return -1;
        }

        /// <summary>
        /// Obtiene el primer tipo de operacion y su nivel
        /// </summary>
        /// <returns></returns>
        public TipoOperacionNivel GetPrimerOpNivel()
        {
            return nivelesTipoOperacion[0];
        }

        /// <summary>
        /// Obtiene el último tipo de operacion y su nivel
        /// </summary>
        /// <returns></returns>
        public TipoOperacionNivel GetUltimoOpNivel()
        {
            return nivelesTipoOperacion[nivelesTipoOperacion.Count - 1];
        }

        /// <summary>
        /// Obtiene el siguiente TipoOperacionNivel desde el indice seleccionado
        /// </summary>
        /// <param name="indexOf"></param>
        /// <returns>Retorna un TipoOperacionNivel vacio en caso de no poseer alguno</returns>
        public TipoOperacionNivel GetAnterior(int indexOf)
        {
            if (indexOf <= 0 || indexOf > nivelesTipoOperacion.Count)
            {
                return new TipoOperacionNivel();
            }
            else
            {
                return nivelesTipoOperacion[indexOf - 1];
            }
        }

        /// <summary>
        /// Obtiene el siguiente TipoOperacionNivel desde el indice seleccionado
        /// </summary>
        /// <param name="indexOf"></param>
        /// <returns>Retorna un TipoOperacionNivel vacio en caso de no poseer alguno</returns>
        public TipoOperacionNivel GetSiguiente(int indexOf)
        {
            if (nivelesTipoOperacion.Count - 1 == indexOf)
            {
                return new TipoOperacionNivel();
            }
            else
            {
                return nivelesTipoOperacion[indexOf + 1];
            }
        }

        private void GenerarOperandosContenidos()
        {
            for (int i = 0; i < nivelesTipoOperacion.Count; i++)
            {
                if (!tipoOperaciones.Contains(nivelesTipoOperacion[i].TipoOperacion))
                {
                    tipoOperaciones.Add(nivelesTipoOperacion[i].TipoOperacion);
                }
            }
        '''
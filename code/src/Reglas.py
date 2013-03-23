
from TipoOperacionNivel import *
from ModuloNivel import ModuloNivel
from BasicOperacion import *
from Reglas_Fijas import *
from GeneradorPreguntas import *

class Reglas:

	modulosNivel = list()

	# pendiente 2 mayus
	# pendiente 2 otr (no hay palabras terminadas en aba en la base de datos)
	#pendiente 2 int
	lista = list()
	
	
	def __init__(self):
		self.lista.append(TipoOperacionNivel(1, TipoOperacion.mayus_nombres_propios))
		self.lista.append(TipoOperacionNivel(1, TipoOperacion.patrones_ort_comunes)) # falta temporizador
		self.lista.append(TipoOperacionNivel(1, TipoOperacion.sentido_vocales_silabas))
		self.lista.append(TipoOperacionNivel(1, TipoOperacion.signos_int_excl))
		self.lista.append(TipoOperacionNivel(1,TipoOperacion.Reproduccion_letras_alfabeto))
		self.lista.append(TipoOperacionNivel(2,TipoOperacion.Reproduccion_letras_alfabeto))
		self.lista.append(TipoOperacionNivel(3, TipoOperacion.patrones_ort_comunes)) # falta imagen en las palabras
		self.lista.append(TipoOperacionNivel(4, TipoOperacion.patrones_ort_comunes)) # pendiente 4, no hay diferencias entre palabras con r y rr
		self.lista.append(TipoOperacionNivel(5, TipoOperacion.patrones_ort_comunes))
		self.modulosNivel.append(ModuloNivel(self.lista, "principal"))
		return		
	
	# Metodo publico que entrega la siguiente operacion en funcion
	# de las reglas pedagogicas. Es lo unico que se puede acceder de
	# la clase Reglas
	def GetSiguienteOperacion(self, operacion, alumno):
		
		
		if not operacion.respuesta_correcta  and operacion.CantidadVecesIncorrectaSoloEsta <= 2 and operacion.feedback_correcto != "First" :
			return operacion
		
        
		operacion.cantidadMaximaNivel= max(Reglas_Fijas.MaximoNivel, operacion.cantidadMaximaNivel)
		
		siguiente_nivel = operacion.nivelOperacion
		cantidad_nivel = operacion.cantidadNivel
		cantidad_maxima_nivel = operacion.cantidadMaximaNivel
		borrarCorrectas = False
		tipoActual = operacion.TipoOperacion;
		
		cambia_nivel= Reglas_Fijas.CambioNivel(operacion)
		
		if cambia_nivel == CambioNivel.Sube:
			borrarCorrectas = True
			siguiente_nivel+=1
			cantidad_nivel = 1
			op= self.AlterarFlujo(operacion, siguiente_nivel)
			tipoActual = op.TipoOperacion
			siguiente_nivel = op.nivelOperacion
		
		elif cambia_nivel == CambioNivel.Mantiene:
			cantidad_maxima_nivel += self.SubidaMaximoNivel(operacion)
			cantidad_nivel+=1
		
		siguiente_operacion= None
		generador= GeneradorPreguntas(alumno)
		
		if tipoActual == TipoOperacion.mayus_nombres_propios:
			if siguiente_nivel==1:
				siguiente_operacion = generador.generador_mayus_nombres_propios1()
			elif siguiente_nivel==2:
				siguiente_operacion = generador.generador_mayus_nombres_propios2()
				
		if tipoActual == TipoOperacion.patrones_ort_comunes:
			if siguiente_nivel==1:
				siguiente_operacion = generador.generador_patrones_ort_comunes1()
			if siguiente_nivel==2:
				siguiente_operacion = generador.generador_patrones_ort_comunes2()
			if siguiente_nivel==3:
				siguiente_operacion = generador.generador_patrones_ort_comunes3()
			if siguiente_nivel==4:
				siguiente_operacion = generador.generador_patrones_ort_comunes4()
			if siguiente_nivel==5:
				siguiente_operacion = generador.generador_patrones_ort_comunes5()
				
		if tipoActual == TipoOperacion.Reproduccion_letras_alfabeto:
			if siguiente_nivel==1:
				siguiente_operacion = generador.generador_reproduccion_letras_alfabeto1()
			if siguiente_nivel==2:
				siguiente_operacion = generador.generador_reproduccion_letras_alfabeto2()
				
		if tipoActual == TipoOperacion.sentido_vocales_silabas:
			
			next_num= random.randrange(1,3)
			
			siguiente_operacion = generador.generador_sentido_vocales1(next_num)
			
		if tipoActual == TipoOperacion.signos_int_excl:
			if siguiente_nivel==1:
				if operacion.TipoOperacion == TipoOperacion.sentido_vocales_silabas:
					siguiente_operacion = generador.generador_signos_int_excl1(False)
				else:
					siguiente_operacion = generador.generador_signos_int_excl1(True)
			if siguiente_nivel==2:
				siguiente_operacion = generador.generador_signos_int_excl2()
		
		if siguiente_nivel == operacion.nivelOperacion:
			siguiente_operacion.cantidadMaximaNivel= cantidad_maxima_nivel
			siguiente_operacion.AgregarPuntajesNivel(operacion.puntajesNivel, operacion.puntaje)
			siguiente_operacion.cantidadNivel= cantidad_nivel
		else:
			siguiente_operacion.cantidadNivel=1
			
		if not borrarCorrectas:
			siguiente_operacion.correctasTotales = operacion.correctasTotales
		
		siguiente_operacion.vecesIncorrecta = operacion.vecesIncorrecta
		
		return siguiente_operacion
		
	
	def AlterarFlujo(self, operacion, siguienteNivel):
		nivelActual = siguienteNivel - 1
		
		for mn in self.lista:
			index= mn.ContieneTipoOperacionNivel(nivelActual, operacion.TipoOperacion)
			
			if index != -1:
				on= mn.GetSiguiente(index)
				
				if on != None:
					indexMO= self.lista.index(mn)
					indexMO+=1
					
					if indexMO== len(self.lista):
						op= BasicOperacion()
						op.TipoOperacion= operacion.TipoOperacion
						op.nivelOperacion= nivelActual
						return op
					else:
						on= self.lista[indexMO].GetPrimerOpNivel()
				
				op= BasicOperacion()
				op.TipoOperacion= TipoOperacionNivel.TipoOpGlobal
				op.nivelOperacion= TipoOperacionNivel.NivelGlobal
				return op
				
		op= BasicOperacion()
		op.TipoOperacion= operacion.TipoOperacion
		op.nivelOperacion= nivelActual
		return op		
		
		
	def SubidaMaximoNivel(self,op):

		if op.correctasTotales < Reglas_Fijas.MinimoPasoNivel and op.cantidadNivel>= Reglas_Fijas.CantidadPreguntasNivelError:
			return 1
		
		return 0
		
	
		
				

'''        
        public BasicOperacion GetSiguienteOperacion(BasicOperacion operacion, Alumno alumno)
        {

            if (!operacion.respuesta_correcta && operacion.CantidadVecesIncorrectaSoloEsta <= 2 && !operacion.feedback_correcto.Equals("first"))
            {
                return operacion;
            }


            operacion.CantidadMaximaNivel = Math.Max(Reglas_Fijas.MaximoNivel, operacion.CantidadMaximaNivel);

            int siguiente_nivel = operacion.NivelOperacion;
            int cantidad_nivel = operacion.CantidadNivel;
            int cantidad_maxima_nivel = operacion.CantidadMaximaNivel;

            bool borrarCorrectas = false;
            TipoOperacion tipoActual = operacion.TipoOperacion;

            switch (Reglas_Fijas.CambiaNivel(operacion))
            {
                case CambioNivel.Sube:
                    {
                        borrarCorrectas = true;
                        siguiente_nivel++;
                        cantidad_nivel = 1;

                        Tuple<TipoOperacion, int> tupla = AlterarFlujo(operacion, siguiente_nivel);

                        tipoActual = tupla.Item1;
                        siguiente_nivel = tupla.Item2;

                        break;
                    }
                case CambioNivel.Mantiene:
                    {
                        cantidad_maxima_nivel += SubidaMaximoNivel(operacion);
                        cantidad_nivel++;

                        break;
                    }
            }

            BasicOperacion siguiente_operacion = null;
                       
            GeneradorPreguntas generador = new GeneradorPreguntas(alumno);

            #region Siguiente Operacion
            //TODO: Falta implementar la generación de ejercicios.
            switch (tipoActual) 
            {
                case TipoOperacion.mayus_nombres_propios:
                    {
                        switch (siguiente_nivel)
                        {
                            case 1:
                                siguiente_operacion = generador.generador_mayus_nombres_propios1();
                                break;
                            case 2:
                                siguiente_operacion = generador.generador_mayus_nombres_propios2();
                                break;
                        }
                        break;
                    }

                case TipoOperacion.patrones_ort_comunes:
                    {
                        switch (siguiente_nivel)
                        {
                            case 1:
                                siguiente_operacion = generador.generador_patrones_ort_comunes1();
                                break;
                            case 2:
                                siguiente_operacion = generador.generador_patrones_ort_comunes2();
                                break;
                            case 3:
                                siguiente_operacion = generador.generador_patrones_ort_comunes3();
                                break;
                            case 4:
                                siguiente_operacion = generador.generador_patrones_ort_comunes4();
                                break;
                            case 5:
                                siguiente_operacion = generador.generador_patrones_ort_comunes5();
                                break;
                        }
                        break;
                    }

                case TipoOperacion.Reproduccion_letras_alfabeto:
                    {
                        switch (siguiente_nivel)
                        {
                            case 1:
                                siguiente_operacion = generador.generador_reproduccion_letras_alfabeto1();
                                break;
                            case 2:
                                siguiente_operacion = generador.generador_reproduccion_letras_alfabeto2();
                                break;
                        }
                        break;
                    }

                case TipoOperacion.sentido_vocales_silabas:
                    {
                        Random rand = new Random();
                        int next = rand.Next(1, 4);

                        if (next == 4)
                            next -= 1;

                        siguiente_operacion = generador.generador_sentido_vocales1(next);
                        break;
                    }
                case TipoOperacion.signos_int_excl:
                    {
                        switch (siguiente_nivel)
                        {
                            case 1:
                                {
                                    if (operacion.TipoOperacion==TipoOperacion.sentido_vocales_silabas)
                                        siguiente_operacion = generador.generador_signos_int_excl1(false);
                                    else
                                        siguiente_operacion = generador.generador_signos_int_excl1(true);
                                }
                                break;
                            case 2:
                                siguiente_operacion = generador.generador_signos_int_excl2();
                                break;
                        }
                        break;

                    }
            }

            #endregion

            if (siguiente_nivel == operacion.NivelOperacion)
            {
                siguiente_operacion.CantidadMaximaNivel = cantidad_maxima_nivel;
                siguiente_operacion.AgregarPuntajesNivel(operacion.PuntajesNivel, operacion.Puntaje);
                siguiente_operacion.CantidadNivel = cantidad_nivel;
            }
            else
            {
                siguiente_operacion.CantidadNivel = 1;
            }
            if (!borrarCorrectas)
            {
                siguiente_operacion.CantidadCorrectasTotales = operacion.CantidadCorrectasTotales;
            }

            siguiente_operacion.CantidadVecesIncorrecta = operacion.CantidadVecesIncorrecta;
            

            return siguiente_operacion;
        }


        public Tuple<TipoOperacion, int> AlterarFlujo(BasicOperacion operacion, int siguienteNivel)
        {
            int nivelActual = siguienteNivel - 1;
            foreach (ModuloNivel mn in modulosNivel)
            {
                int index = mn.ContieneTipoOperacionNivel(nivelActual, operacion.TipoOperacion);

                if (index != -1)
                {
                    TipoOperacionNivel on = mn.GetSiguiente(index);

                    if (on.IsNull)
                    {
                        int indexMO = modulosNivel.IndexOf(mn);
                        indexMO++;

                        if (indexMO == modulosNivel.Count)
                        {
                            return new Tuple<TipoOperacion, int>(operacion.TipoOperacion, nivelActual);
                        }
                        else
                        {
                            on = modulosNivel[indexMO].GetPrimerOpNivel();
                        }
                    }

                    return on.ReturnType();
                }
            }

            return new Tuple<TipoOperacion, int>(operacion.TipoOperacion, nivelActual);
        }

        public int SubidaMaximoNivel(BasicOperacion op)
        {
            if (op.CantidadCorrectasTotales < Reglas_Fijas.MinimoPasoNivel && op.CantidadNivel >= Reglas_Fijas.CantidadPreguntasNivelError)
            {
                return 1;
            }

            return 0;
        }


       



        /// <summary>
        /// Método que entrega la primera operación del primer nivel del TipoOperacion especificado 
        /// </summary>
        /// <param name="TipoOperacion_actual">TipoOperacion de la operación (+,-,*,/)</param>
        /// <returns>Primera operación</returns>
        public static BasicOperacion GetPrimeraOperacion(TipoOperacion tipo_operacion)
        {
            return GetPrimeraOperacion(tipo_operacion, 1);
        }

        /// <summary>
        /// Método que entrega la primera operación del nivel etsablecido para el TipoOperacion especificado 
        /// </summary>
        /// <param name="TipoOperacion_actual">TipoOperacion de la operación (+,-,*,/)</param>
        /// <param name="nivel_actual">Nivel de la operación</param>
        /// <returns>Primera operación</returns>
        public static BasicOperacion GetPrimeraOperacion(TipoOperacion tipo_operacion, int nivel_actual)
        {
            int siguiente_nivel = nivel_actual;
            int cantidad_nivel = 1;

            BasicOperacion siguiente_operacion = null;

            switch (tipo_operacion)
            {
                case TipoOperacion.mayus_nombres_propios:
                    {
                        //siguiente_operacion = GetSiguienteSuma(nivel_actual, cantidad_nivel);
                        break;
                    }
                case TipoOperacion.patrones_ort_comunes:
                    {
                        //siguiente_operacion = GetSiguienteResta(nivel_actual, cantidad_nivel);
                        break;
                    }
                case TipoOperacion.Reproduccion_letras_alfabeto:
                    {
                        //siguiente_operacion = GetSiguienteMultiplicacion(nivel_actual, cantidad_nivel, siguiente_operacion);
                        break;
                    }
                case TipoOperacion.sentido_vocales_silabas:
                    {
                        //siguiente_operacion = GetSiguienteDivision(nivel_actual, cantidad_nivel, siguiente_operacion);
                        break;
                    }
                case TipoOperacion.signos_int_excl:
                    {
                        //siguiente_operacion = GetSiguienteDivision(nivel_actual, cantidad_nivel, siguiente_operacion);
                        break;
                    }
            }

            return siguiente_operacion;
        }

        

        
        #region Matematica

        /// <summary>
        /// Eleva un numero a un exponente
        /// </summary>
        /// <param name="elevado"></param>
        /// <param name="exponente"></param>
        /// <returns></returns>
        private static int ElevarNumero(int elevado, int exponente)
        {
            int resultado = 1;

            if (exponente != 0)
            {
                for (int i = 0; i < exponente; i++)
                {
                    resultado = resultado * elevado;
                }
            }

            return resultado;
        }

        #endregion

        #region Randoms


        #region Sumas

     
        #endregion

        #region Restas


        
        #endregion

        #region Multiplicacion


        #endregion

        #region Fracciones

      
        #endregion

        #region Decimal

        #endregion

        #region Escritura

        
        #endregion

        #region Utilidades Varias

        /// <summary>
        /// Transforma una lista de bools a un arreglo de 0 o 1 en enteros
        /// </summary>
        /// <param name="lista_reservas"></param>
        /// <returns></returns>
        private static int[] TransformarBoolsInt(bool[] lista_reservas, int target_lenght)
        {
            int[] aux = new int[target_lenght];
            int index = 0;

            foreach (bool i in lista_reservas)
            {
                if (i)
                {
                    aux[index] = 1;
                }
                else
                {
                    aux[index] = 0;
                }

                index++;
            }

            for (int j = index; j < target_lenght; j++)
            {
                aux[j] = 0;
            }

            return aux;
        }

        /// <summary>
        /// Alterna los valores de un arreglo de 2 enteros si cambiar es 1
        /// </summary>
        /// <param name="valores"></param>
        /// <param name="cambiar"></param>
        /// <returns></returns>
        private static int[] SwapearValores(int[] valores, int cambiar)
        {
            if (cambiar == 1)
            {
                int aux = valores[0];
                valores[0] = valores[1];
                valores[1] = aux;
            }

            return valores;
        }

        /// <summary>
        /// Retorna si esta dentro del arreglo el numero determinado.
        /// </summary>
        /// <param name="arreglo"></param>
        /// <param name="numero"></param>
        /// <returns></returns>
        internal static bool NumeroEnArreglo(int[] arreglo, int numero)
        {
            foreach (int i in arreglo)
            {
                if (i == numero)
                {
                    return true;
                }
            }

            return false;
        }

        /// <summary>
        /// Entrega el indice del numero dentro del arreglo
        /// </summary>
        /// <param name="arreglo"></param>
        /// <param name="numero"></param>
        /// <returns></returns>
        internal static int IndiceArreglo(int[] arreglo, int numero)
        {
            for (int i = 0; i < arreglo.Length; i++)
            {
                if (arreglo[i] == numero)
                {
                    return i;
                }
            }

            return -1;
        }

        /// <summary>
        /// Dado un arreglo ordenado, establece en que intervalo esta el numero, entregando 0 si es menor que cualquier elemento del arreglo
        /// y el largo del arreglo si es superior a todos.
        /// </summary>
        /// <param name="arreglo"></param>
        /// <param name="numero"></param>
        /// <returns></returns>
        internal static int IntervaloSuperiorArreglo(int[] arreglo, int numero)
        {
            for (int i = 0; i < arreglo.Length; i++)
            {
                if (numero < arreglo[i])
                {
                    return i;
                }
            }

            return arreglo.Length;
        }

       
       
        /// <summary>
        /// Parsea de forma segura un string (capta las excepciones que podrían ser lanzadas). 
        /// </summary>
        /// <param name="parser">String a ser parseado</param>
        /// <returns>Int parseado, 0 en caso de error</returns>
        private static int ParsearString(string parser)
        {
            int resultado = 0;

            if (parser != "")
            {

                try
                {
                    resultado = int.Parse(parser, CultureInfo.InvariantCulture);
                }

                catch (FormatException)
                {
                    resultado = 0;
                }
            }

            return resultado;
        }

       
        
        #endregion
    }
}
        #endregion
        '''
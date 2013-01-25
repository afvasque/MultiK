using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using Biblioteca;
using System.Runtime.Serialization.Formatters.Binary;
using System.IO;
using MySql.Data.MySqlClient;

namespace GeneradorTexto
{
    public delegate Oracion Modelo_oracion ();

    public class Generador : InterfazPalabras
    {
        public static BibliotecaCentral biblioteca = new BibliotecaCentral();
        string ubicacion;
        public List<Modelo_oracion> Lista_Modelos = new List<Modelo_oracion>();
        MySqlConnection conexion;

        public static Random random = new Random();

        #region Verbos organizados en grupos

        #endregion

        public Generador()
        {
        }

        public Generador(string ubicacion, string servidor_sql, string nombre_bd_sql, string usuario_sql, string password_sql)
        {
            this.ubicacion = ubicacion;

            try
            {
                using (Stream stream = File.Open(ubicacion, FileMode.Open))
                {
                    BinaryFormatter bin = new BinaryFormatter();
                    biblioteca = (BibliotecaCentral)bin.Deserialize(stream);
                }
            }
            catch (IOException)
            {
            }


            biblioteca.Inicializar();

            M_Conexion(servidor_sql, nombre_bd_sql, usuario_sql, password_sql);
        }

        public Generador(BibliotecaCentral bibliotecarecibida, string servidor_sql, string nombre_bd_sql, string usuario_sql, string password_sql)
        {
            biblioteca = bibliotecarecibida;

            M_Conexion(servidor_sql, nombre_bd_sql, usuario_sql, password_sql);
        }

        public string generador_letra_alfabeto()
        {
            return "" + (char)random.Next(97, 123);
        }

        public string generador_palabra_contiene(string texto)
        {
            try
            {
                List<Palabra> palabra = biblioteca.palabras.FindAll(a => a.palabra.Contains(texto));
                return palabra[random.Next(palabra.Count())].palabra;
            }
            catch
            {
                return null;
            }
        }

        public string generador_palabra_no_contine(string texto)
        {
            try
            {
                List<Palabra> palabra = biblioteca.palabras.FindAll(a => !a.palabra.Contains(texto));
                return palabra[random.Next(palabra.Count())].palabra;
            }
            catch
            {
                return null;
            }
        }

        public string generador_palabra_silaba(int cantidad)
        {
            try
            {
                List<Palabra> palabra = biblioteca.palabras.FindAll(a => a.silabas.Count() == cantidad);
                return palabra[random.Next(palabra.Count())].palabra;
            }
            catch
            {
                return null;
            }
        }

        /// <summary>
        /// Entrega un sust. propio si es true o común si es false
        /// </summary>
        /// <param name="propio"></param>
        /// <returns></returns>
        public string generador_sust_propio(bool propio)
        {
            string palabra = "";
            if (propio)
            {
                palabra = biblioteca.sustantivospropios[random.Next(biblioteca.sustantivospropios.Count())].formas_nucleares[0].palabra;
            }
            else
            {
                palabra = biblioteca.sustantivoscomunes[random.Next(biblioteca.sustantivoscomunes.Count())].formas_nucleares[0].palabra;
            }

            return palabra;
        }

        /// <summary>
        /// Dada una palabra entrega true si contiene alguna 'r' o 'rr' que suene fuerte. 
        /// Entrega false si no contiene 'r' o no suena fuerte
        /// </summary>
        /// <param name="palabra"></param>
        /// <returns></returns>
        private bool Suena_R_Fuerte(Palabra palabra)
        {
            int posicion_r = palabra.palabra.IndexOf('r');


            if (posicion_r > 0)
            {
                string anterior = palabra.palabra.Substring(posicion_r - 1, 1);
                if (posicion_r + 1 < palabra.palabra.Length)
                {
                    string posterior = palabra.palabra.Substring(posicion_r + 1, 1);

                    int sub = palabra.palabra.IndexOf("sub");

                    if (posterior == "r" || anterior == "r")
                    {
                        return true;
                    }

                    if (anterior == "b" || anterior == "c" || anterior == "d" || anterior == "f" || anterior == "g" || anterior == "p" || anterior == "t")
                    {
                        return false;
                    }

                    if (anterior == "l" || anterior == "n" || anterior == "s")
                    {
                        return true;
                    }

                    if (sub + 3 == posicion_r && sub>-1)
                    {
                        return true; // despues de sub suena fuerte
                    }

                    return false;
                }
                else
                    return false; // Si termina con r no suena fuerte
            }

            return true; // Si empieza con r suena fuerte
        }

        /// <summary>
        /// Entrega un string con la palabra solicitada
        /// </summary>
        /// <param name="fuerte">true si buscas sonido con r fuerte, false con rr despacio</param>
        /// <returns></returns>
        public string Palabra_R_Fuerte(bool fuerte)
        {
            List<Palabra> palabras = biblioteca.palabras.FindAll(a => this.Suena_R_Fuerte(a) == fuerte && (a.palabra.Contains('r') || a.palabra.Contains('R')) );
            List<Palabra> palabras2 = new List<Palabra>();
            foreach (Palabra i in palabras)
            {
                if (this.Descartar_Muchas_R(i))
                    palabras2.Add(i);
            }
            foreach (Palabra i in palabras2)
                palabras.Remove(i);

            return palabras[random.Next(palabras.Count())].palabra;
        }

        /// <summary>
        /// Devuelve true si se debe descartar, false si no.
        /// </summary>
        /// <param name="palabra"></param>
        /// <returns></returns>
        private bool Descartar_Muchas_R(Palabra palabra)
        {
            int posicion_r = palabra.palabra.IndexOf('r');

            if (palabra.palabra.Substring(0, 1) == "R") //Parte con R
            {
                if (posicion_r == -1)
                    return false; //Parte con R y no contiene mas "R's"

                else
                    return true; //Parte con R y tiene más R's
            }
            
            if (posicion_r == -1)
                return true; //Se debe descartar ya que no contiene r.
            
            int posicion_rr = palabra.palabra.Substring(posicion_r + 1).IndexOf('r');

            if (posicion_rr == -1)
                return false; //No descartar ya que contiene solo 1 r.

            else //Si llego aquí es porque contiene al menos 2 rr's.
            {

                if (posicion_rr > 0)
                {
                    return true; //Si las rr's no están juntas, luego descartar!
                }

                else
                {
                    int posicion_rrr = palabra.palabra.Substring(posicion_rr + posicion_r +2).IndexOf('r');
                    if (posicion_rrr != -1) //Contiene más de 2 rr's, descartar!
                        return true;
                    else
                        return false; //Contiene exactamente 2 rr's juntas, entregar.
                }
                    
            }


        }

        private void Inicializar_Delegates()
        {
        }

        #region Zona de modelos de creación de oraciones

        /// <summary>
        /// Entrega una oración con el verbo ser
        /// </summary>
        /// <param name="id_tiempo">Tiempo de la BD Onoma (Ver Excel)</param>
        public Oracion Ser()
        {
            int id_tiempo = 1;

            // id del verbo = 1

            /*
             * La lógica presente es que los adjetivos atributos son todos aquellos en los que se usa el verbo ser
             * Se usa el verbo presente porque se asume que los adjetivos atributos son de estado actual.
             */

            Oracion oracion = new Oracion();

            List<Sustantivo> lista = biblioteca.id_verbo[1].sustantivos;
            //Sustantivo sustantivo = lista[random.Next(0, lista.Count)];
            Sustantivo sustantivo = biblioteca.sustantivoscomunes[random.Next(0,17)];
            Nucleo_Sustantival nucleo = sustantivo.formas_nucleares[random.Next(0, sustantivo.formas_nucleares.Length)];
            int id_persona = PersonaOnoma(nucleo);

            if (sustantivo.escomun)
            {
                Articulo articulo = biblioteca.BuscarArticulo(nucleo.genero, nucleo.essingular, true);
                oracion.Sujeto.Add(articulo);
            }

            oracion.Sujeto.Add(nucleo);

            string el_verbo = Select(1, id_persona, id_tiempo);

            Verbo verbo = new Verbo(el_verbo);

            oracion.Predicado.Add(verbo);

            Adjetivo adjetivo = sustantivo.adjetivosatributos[random.Next(0, sustantivo.adjetivosatributos.Count())];


            oracion.Predicado.Add(adjetivo.Obtener_Adjetivo(id_persona,nucleo.genero));

            return oracion;
        }

        

        #endregion

        public void M_Conexion(string servidor, string basedato, string usuario, string password) //metodo de conexion
        {
            string cadenadeConexion = "SERVER=" + servidor + ";" + "DATABASE=" + basedato + ";" + "UID=" + usuario + ";" + "PASSWORD=" + password + ";";
            conexion = new MySqlConnection(cadenadeConexion);
            conexion.Open();
        }

        public string Select(int id_verbo, int id_persona, int id_tiempo)
        {
            string sentencia = "select formaconjugada from t_formasverbales where verboinfinitivo = "+id_verbo+" and  numeropersona = "+id_persona
                +" and tiempomodo ="+id_tiempo;

            MySqlCommand ejecutar = new MySqlCommand(sentencia, conexion);
            MySqlDataReader reader = ejecutar.ExecuteReader();
            reader.Read();
            string resultado = reader[0].ToString();
            reader.Close();
            return resultado;
        }

        public int PersonaOnoma(Nucleo_Sustantival nucleo)
        {
            if (nucleo.genero == BibliotecaCentral.Genero.masculino)
            {
                // el, ellos
                if (nucleo.essingular)
                    return 5;
                else
                    return 13;
            }

            else if (nucleo.genero == BibliotecaCentral.Genero.femenino)
            {
                // la, ellas
                if (nucleo.essingular)
                    return 6;
                else
                    return 14;
            }

            else
            {
                return 7;
            }

        }

    }
}

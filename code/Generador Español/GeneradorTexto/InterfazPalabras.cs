using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace GeneradorTexto
{
    interface InterfazPalabras
    {

        /// <summary>
        /// Entrega una letra del alfabeto al azar
        /// </summary>
        /// <param name="operacion"></param>
        string generador_letra_alfabeto();

        /// <summary>
        /// Entrega una palabra que contiene el texto entregado
        /// </summary>
        /// <param name="texto"></param>
        /// <returns></returns>
        string generador_palabra_contiene(string texto);

        /// <summary>
        /// /// Entrega una palabra que NO contiene el texto entregado
        /// </summary>
        /// <param name="texto"></param>
        /// <returns></returns>
        string generador_palabra_no_contine(string texto);

        /// <summary>
        /// Entrega una palabra que contiene el número de sílabas entregado.
        /// </summary>
        /// <param name="cantidad"></param>
        /// <returns></returns>
        string generador_palabra_silaba(int cantidad);

        /// <summary>
        /// Entrega un sust. propio si es true o común si es false
        /// </summary>
        /// <param name="propio"></param>
        /// <returns></returns>
        string generador_sust_propio(bool propio);



    }
}

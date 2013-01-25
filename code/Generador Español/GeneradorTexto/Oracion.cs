using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using Biblioteca;

namespace GeneradorTexto
{
    public class Oracion
    {
        internal List<Palabra> Sujeto = new List<Palabra>();
        internal List<Palabra> Predicado = new List<Palabra>();

        internal string frase = "";

        public override string ToString()
        {
            if (Sujeto.Count == 0 && Predicado.Count == 0)
                return frase;

            string Frase = "";
            foreach (Palabra i in Sujeto)
                Frase += i + " ";

            foreach (Palabra i in Predicado)
                Frase += i+ " ";

            Frase = Frase.Substring(0, 1).ToUpperInvariant() + Frase.Substring(1, Frase.Length - 2);
            Frase = Frase + ".";
            return Frase;
        }

        public string Obtener_Sujeto()
        {
            string auxiliar = "";

            foreach (Palabra i in Sujeto)
                auxiliar += i + " ";

            auxiliar = auxiliar.Substring(0, 1).ToUpperInvariant() + auxiliar.Substring(1, auxiliar.Length - 1);
            return auxiliar;
        }

        public string Obtener_Predicado()
        {
            string auxiliar = "";

            foreach (Palabra i in Predicado)
                auxiliar += i + " ";

            auxiliar = auxiliar.Substring(0, auxiliar.Length - 1);
            
            return auxiliar;
        }

    }
}

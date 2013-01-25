using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Biblioteca
{
    [Serializable]
    public class Palabra
    {
        public static int contador;

        public string[] silabas;
        public string palabra;

        public Palabra()
        {
        }

        public Palabra(string[] silabas)
        {
            this.silabas = silabas;
            foreach (string i in silabas)
                palabra += i;
        }

        internal void Construir(string[] silabas)
        {
            this.silabas = silabas;
            foreach (string i in silabas)
                palabra += i;
        }

        public virtual void Inicializar()
        {
        }

        public override string ToString()
        {
            return palabra;
        }
    }
}

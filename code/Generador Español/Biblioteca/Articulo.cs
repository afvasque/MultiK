using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Biblioteca
{
    [Serializable]
    public class Articulo:Palabra
    {
        public bool esdeterminado, essingular;
        public BibliotecaCentral.Genero genero;

        public Articulo(BibliotecaCentral.Genero genero, bool esdeterminado, bool essingular, string[] silabas):base(silabas)
        {
            this.genero = genero;
            this.esdeterminado = esdeterminado;
            this.essingular = essingular;
        }

    }
}

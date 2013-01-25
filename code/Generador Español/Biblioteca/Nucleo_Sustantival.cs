using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Biblioteca
{
    [Serializable]
    public class Nucleo_Sustantival:Palabra
    {
        public bool essingular;
        public BibliotecaCentral.Genero genero;

        public Nucleo_Sustantival(string[] silabas, bool essingular, BibliotecaCentral.Genero genero):base(silabas)
        {
            this.essingular = essingular;
            this.genero = genero;
        }
    }
}

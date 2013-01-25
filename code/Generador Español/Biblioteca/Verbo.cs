using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Biblioteca
{
    [Serializable]
    public class Verbo : Palabra
    {
        public List<Adjetivo> complementosdirectos = new List<Adjetivo>();

        public List<Sustantivo> sustantivos = new List<Sustantivo>();

        public List<Adjetivo> adjetivos = new List<Adjetivo>();

        public int id_bd;

        public Verbo(string[] silabas, int id)
            : base(silabas)
        {
            this.id_bd = id;
        }

        public Verbo(string palabra)
            : base()
        {
            this.palabra = palabra;
        }

        
    }
}

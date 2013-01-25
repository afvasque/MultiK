using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Biblioteca
{
    [Serializable]
    public class Sustantivo : Palabra
    {
        public bool escomun, escontable;

        //Confirmado

        public List<Verbo> verbos = new List<Verbo>();

        public List<Adjetivo> adjetivosatributos = new List<Adjetivo>();
        public List<Adjetivo> adjetivoestado = new List<Adjetivo>();

        //No Confirmado 
        public List<Adjetivo> adjetivosrelacionales = new List<Adjetivo>();
        public List<Adjetivo> adjetivosindefinidos = new List<Adjetivo>();
        public List<Adjetivo> adjetivosposesivos = new List<Adjetivo>();
        public List<Adjetivo> adjetivosexplicativos = new List<Adjetivo>();
        public List<Adjetivo> adjetivoscalificativos = new List<Adjetivo>();

        public Nucleo_Sustantival[] formas_nucleares;

        public string path_imagen_asociada;

        public Sustantivo(bool escomun, bool escontable, string[] SilabasSingularMasculino, string[] SilabasSingularFemenino, string[] SilabasPluralMasculino,
            string[] SilabasPluralFemenino, string path)
            : base()
        {
            this.escomun = escomun;
            this.escontable = escontable;

            List<Nucleo_Sustantival> lista_auxiliar = new List<Nucleo_Sustantival>();


            if (SilabasSingularMasculino != null && SilabasSingularMasculino.Length != 0)
                lista_auxiliar.Add(new Nucleo_Sustantival(SilabasSingularMasculino, true, BibliotecaCentral.Genero.masculino));
            if (SilabasSingularFemenino != null && SilabasSingularFemenino.Length != 0)
                lista_auxiliar.Add(new Nucleo_Sustantival(SilabasSingularFemenino, true, BibliotecaCentral.Genero.femenino));
            if (SilabasPluralMasculino != null && SilabasPluralMasculino.Length != 0)
                lista_auxiliar.Add(new Nucleo_Sustantival(SilabasPluralMasculino, false, BibliotecaCentral.Genero.masculino));
            if (SilabasPluralFemenino != null && SilabasPluralFemenino.Length != 0)
                lista_auxiliar.Add(new Nucleo_Sustantival(SilabasPluralFemenino, false, BibliotecaCentral.Genero.femenino));

            formas_nucleares = lista_auxiliar.ToArray();
            Construir(formas_nucleares[0].silabas);

            if (path != null)
                path_imagen_asociada = path;
        }
    }
}

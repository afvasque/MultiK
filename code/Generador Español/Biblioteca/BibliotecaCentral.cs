using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Biblioteca
{
    [Serializable]
    public class BibliotecaCentral
    {
        public enum Genero { masculino, femenino, neutro, pordefecto };

        public List<Adjetivo> adjetivos = new List<Adjetivo>();
        public List<Articulo> articulos = new List<Articulo>();
        public List<Pronombre> pronombres = new List<Pronombre>();
        public List<Sustantivo> sustantivoscomunes = new List<Sustantivo>();
        public List<Sustantivo> sustantivospropios = new List<Sustantivo>();
        public List<Verbo> verbos = new List<Verbo>();
        public Dictionary<int, Verbo> id_verbo = new Dictionary<int, Verbo>();
        
        public List<Palabra> palabras = new List<Palabra>();

        public BibliotecaCentral()
        {
        }

        public void AgregarArticulo(BibliotecaCentral.Genero genero, bool esdeterminado, bool essingular, string[] silabas)
        {
            Articulo articulo = new Articulo(genero, esdeterminado, essingular, silabas);
            articulos.Add(articulo);
            palabras.Add(articulo);
        }

        public void AgregarAdjetivo(string[] SilabasSingularMasculino,
            string[] SilabasSingularFemenino, string[] SilabasPluralMasculino, string[] SilabasPluralFemenino,
            string[] SilabaSuperlativoMasculino, string[] SilabaSuperlativaFemenina, Adjetivo.Unico unico)
        {
            Adjetivo adjetivo = new Adjetivo(SilabasSingularMasculino, SilabasSingularFemenino,
                SilabasPluralMasculino, SilabasPluralFemenino, SilabaSuperlativoMasculino, SilabaSuperlativaFemenina, unico);
            adjetivos.Add(adjetivo);
            palabras.Add(adjetivo);
        }

        public void AgregarSustantivo(bool escomun, bool escontable, string[] SilabasSingularMasculino,
            string[] SilabasSingularFemenino, string[] SilabasPluralMasculino, string[] SilabasPluralFemenino, string path)
        {
            Sustantivo sustantivo = new Sustantivo(escomun, escontable, SilabasSingularMasculino, SilabasSingularFemenino,
                SilabasPluralMasculino, SilabasPluralFemenino, path);
            if (sustantivo.escomun)
                sustantivoscomunes.Add(sustantivo);
            else
                sustantivospropios.Add(sustantivo);
            palabras.Add(sustantivo);
        }

        public void AgregarVerbo(string[] silabas, int id)
        {
            Verbo verbo = new Verbo(silabas, id);
            verbos.Add(verbo);
            palabras.Add(verbo);
            id_verbo.Add(id, verbo);
        }

        public void Inicializar()
        { 
            #region Actualizar Contadores
            if (palabras == null)
            {
                palabras = new List<Palabra>();
            }

            foreach (Palabra i in palabras)
                i.Inicializar();

            #endregion
        }

        #region Búsqueda

        public Articulo BuscarArticulo(Genero genero, bool essingular, bool esdeterminado)
        {
            foreach (Articulo i in articulos)
            {
                if (i.genero == genero && i.essingular == essingular && i.esdeterminado == esdeterminado)
                {
                    return i;
                }
            }
            return null;
        }

        #endregion





    }
}

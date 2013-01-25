using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using Biblioteca;
using System.Runtime.Serialization.Formatters.Binary;
using System.IO;

namespace ModificadorBaseDato
{
    public class Modificador
    {
        public static BibliotecaCentral biblioteca = new BibliotecaCentral();
        string ubicacion;

        /// <summary>
        /// El archivo ya existe, solo se está entregando su ubicación.
        /// </summary>
        /// <param name="ubicacion">Ubicación del archivo existente</param>
        public Modificador(string ubicacion)
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
        }


        /// <summary>
        /// El archivo no existe y se le da la ruta para que lo cree
        /// </summary>
        /// <param name="ubicacion">La ruta del archivo con su respectivo nombre</param>
        /// <param name="inutil">No sirve</param>
        public Modificador(string ubicacion, string inutil)
        {
            this.ubicacion = ubicacion;
            try
            {
                using (Stream stream = File.Open(ubicacion, FileMode.Create))
                {
                    BinaryFormatter bin = new BinaryFormatter();
                    bin.Serialize(stream, biblioteca);
                }

            }

            catch
            {
            }

        }

        public void Guardar()
        {
            try
            {
                using (Stream stream = File.Open(ubicacion, FileMode.Create))
                {
                    BinaryFormatter bin = new BinaryFormatter();
                    bin.Serialize(stream, biblioteca);
                }

            }

            catch
            {
            }
        }

        #region Agregar/Eliminar Elementos Biblioteca

        public void AgregarArticulo(BibliotecaCentral.Genero genero, bool esdeterminado, bool essingular, string[] silabas)
        {
            biblioteca.AgregarArticulo(genero, esdeterminado, essingular, silabas);
        }

        public void AgregarSustantivo(bool escomun, bool escontable, string[] SilabasSingularMasculino,
            string[] SilabasSingularFemenino, string[] SilabasPluralMasculino, string[] SilabasPluralFemenino, string path)
        {
            biblioteca.AgregarSustantivo(escomun, escontable, SilabasSingularMasculino, SilabasSingularFemenino,
                SilabasPluralMasculino, SilabasPluralFemenino, path);
        }

        public void AgregarAdjetivo(string[] SilabasSingularMasculino,
            string[] SilabasSingularFemenino, string[] SilabasPluralMasculino, string[] SilabasPluralFemenino,
            string[] SilabaSuperlativoMasculino, string[] SilabaSuperlativaFemenina, Adjetivo.Unico unico)
        {
            biblioteca.AgregarAdjetivo(SilabasSingularMasculino, SilabasSingularFemenino,
                SilabasPluralMasculino, SilabasPluralFemenino, SilabaSuperlativoMasculino, SilabaSuperlativaFemenina, unico);
        }


        public void AgregarVerbo(string[] silabas, int id)
        {
            biblioteca.AgregarVerbo(silabas, id);
        }

        public void EliminarArticulo(string palabra)
        {
            foreach (Articulo i in biblioteca.articulos)
            {
                if (i.palabra == palabra)
                {
                    biblioteca.articulos.Remove(i);
                    biblioteca.palabras.Remove(i);
                    break;
                }
            }
        }

        public void EliminarSustantivo(string palabra)
        {
            foreach (Sustantivo sustantivo in biblioteca.sustantivospropios)
            {
                if (sustantivo.formas_nucleares[0].palabra == palabra)
                {
                    foreach (Verbo verbo in biblioteca.verbos)
                    {
                        if (verbo.sustantivos.Contains(sustantivo))
                        {
                            verbo.sustantivos.Remove(sustantivo);
                        }
                    }
                    biblioteca.sustantivospropios.Remove(sustantivo);
                    biblioteca.palabras.Remove(sustantivo);
                    break;
                }
            }

            foreach (Sustantivo sustantivo in biblioteca.sustantivoscomunes)
            {
                if (sustantivo.formas_nucleares[0].palabra == palabra)
                {
                    foreach (Verbo verbo in biblioteca.verbos)
                    {
                        if (verbo.sustantivos.Contains(sustantivo))
                        {
                            verbo.sustantivos.Remove(sustantivo);
                        }
                    }
                    biblioteca.palabras.Remove(sustantivo);
                    biblioteca.sustantivoscomunes.Remove(sustantivo);
                    break;
                }
            }

        }

        public void EliminarVerbo(string palabra)
        {
            foreach (Verbo verbo in biblioteca.verbos)
            {
                if (verbo.palabra == palabra)
                {
                    foreach (Sustantivo sustantivo in biblioteca.sustantivospropios)
                    {
                        if (sustantivo.verbos.Contains(verbo))
                        {
                            sustantivo.verbos.Remove(verbo);
                        }
                    }
                    foreach (Sustantivo sustantivo in biblioteca.sustantivoscomunes)
                    {
                        if (sustantivo.verbos.Contains(verbo))
                        {
                            sustantivo.verbos.Remove(verbo);
                        }
                    }
                    biblioteca.palabras.Remove(verbo);
                    biblioteca.verbos.Remove(verbo);
                    break;
                }
            }
        }

        public void EliminarAdjetivo(string palabra)
        {
            foreach (Adjetivo adjetivo in biblioteca.adjetivos)
            {
                if (adjetivo.palabra == palabra)
                {
                    foreach (Sustantivo sustantivo in biblioteca.sustantivospropios)
                    {
                        sustantivo.adjetivosatributos.Remove(adjetivo);
                        sustantivo.adjetivoscalificativos.Remove(adjetivo);
                        sustantivo.adjetivosexplicativos.Remove(adjetivo);
                        sustantivo.adjetivosindefinidos.Remove(adjetivo);
                        sustantivo.adjetivosposesivos.Remove(adjetivo);
                        sustantivo.adjetivosrelacionales.Remove(adjetivo);
                    }

                    foreach (Sustantivo sustantivo in biblioteca.sustantivoscomunes)
                    {
                        sustantivo.adjetivosatributos.Remove(adjetivo);
                        sustantivo.adjetivoscalificativos.Remove(adjetivo);
                        sustantivo.adjetivosexplicativos.Remove(adjetivo);
                        sustantivo.adjetivosindefinidos.Remove(adjetivo);
                        sustantivo.adjetivosposesivos.Remove(adjetivo);
                        sustantivo.adjetivosrelacionales.Remove(adjetivo);
                    }
                    break;
                }

            }
        }

        #endregion

        #region Solicitar Elementos a Biblioteca

        public string[] SolicitarAdjetivos()
        {
            List<string> lista = new List<string>();
            foreach (Adjetivo i in biblioteca.adjetivos)
                lista.Add(i.palabra);

            return lista.ToArray();
        }

        public string[] SolicitarArticulos()
        {
            List<string> lista = new List<string>();
            foreach (Articulo i in biblioteca.articulos)
                lista.Add(i.palabra);

            return lista.ToArray();
        }

        public string[] SolicitarPronombres()
        {
            List<string> lista = new List<string>();
            foreach (Pronombre i in biblioteca.pronombres)
                lista.Add(i.palabra);

            return lista.ToArray();
        }

        public string[] SolicitarSustantivos()
        {
            List<string> lista = new List<string>();
            foreach (Sustantivo i in biblioteca.sustantivospropios)
                lista.Add(i.palabra);
            foreach (Sustantivo i in biblioteca.sustantivoscomunes)
                lista.Add(i.palabra);

            return lista.ToArray();
        }

        public string[] SolicitarVerbos()
        {
            List<string> lista = new List<string>();
            foreach (Verbo i in biblioteca.verbos)
                lista.Add(i.palabra);

            return lista.ToArray();
        }

        public string[] SolicitarVerbosdeSustantivo(string palabra)
        {
            Sustantivo sustantivo = null;
            List<string> lista = new List<string>();
            foreach (Sustantivo i in biblioteca.sustantivoscomunes)
            {
                if (i.palabra == palabra)
                {
                    sustantivo = i;
                    break;
                }
            }
            foreach (Sustantivo i in biblioteca.sustantivospropios)
            {
                if (i.palabra == palabra)
                {
                    sustantivo = i;
                    break;
                }
            }
            if (sustantivo != null)
            {
                foreach (Verbo i in sustantivo.verbos)
                    lista.Add(i.palabra);
                return lista.ToArray();
            }
            return lista.ToArray();

        }

        public string[] SolicitarAdjetivosdeSustantivo(string palabra)
        {
            Sustantivo sustantivo = null;
            List<string> lista = new List<string>();
            foreach (Sustantivo i in biblioteca.sustantivoscomunes)
            {
                if (i.formas_nucleares[0].palabra == palabra)
                {
                    sustantivo = i;
                    break;
                }
            }
            foreach (Sustantivo i in biblioteca.sustantivospropios)
            {
                if (i.formas_nucleares[0].palabra == palabra)
                {
                    sustantivo = i;
                    break;
                }
            }
            if (sustantivo != null)
            {
                foreach (Adjetivo i in sustantivo.adjetivosrelacionales)
                    lista.Add(i.palabra);
                foreach (Adjetivo i in sustantivo.adjetivosindefinidos)
                    lista.Add(i.palabra);
                foreach (Adjetivo i in sustantivo.adjetivosposesivos)
                    lista.Add(i.palabra);
                foreach (Adjetivo i in sustantivo.adjetivosatributos)
                    lista.Add(i.palabra);
                foreach (Adjetivo i in sustantivo.adjetivosexplicativos)
                    lista.Add(i.palabra);
                foreach (Adjetivo i in sustantivo.adjetivoscalificativos)
                    lista.Add(i.palabra);
                return lista.ToArray();
            }
            return lista.ToArray();

        }

        public string[] SolicitarSustantivodeVerbo(string palabra)
        {
            Verbo verbo = null;
            List<string> lista = new List<string>();
            foreach (Verbo i in biblioteca.verbos)
            {
                if (i.palabra == palabra)
                {
                    verbo = i;
                    break;
                }
            }
            if (verbo != null)
            {
                foreach (Sustantivo i in verbo.sustantivos)
                    lista.Add(i.palabra);
                return lista.ToArray();
            }
            return lista.ToArray();

        }

        public string[] SolicitarAdjetivodeVerbo(string palabra)
        {
            Verbo verbo = null;
            List<string> lista = new List<string>();
            foreach (Verbo i in biblioteca.verbos)
            {
                if (i.palabra == palabra)
                {
                    verbo = i;
                    break;
                }
            }
            if (verbo != null)
            {
                foreach (Adjetivo i in verbo.adjetivos)
                    lista.Add(i.palabra);
                return lista.ToArray();
            }
            return lista.ToArray();
        }

        #endregion

        #region Asignar/desasignar elementos

        public void AsignarVerboaSustantivo(string Sustantivo, string Verbo)
        {
            Sustantivo sustantivo = null;
            Verbo verbo = null;
            foreach (Sustantivo i in biblioteca.sustantivoscomunes)
            {
                if (i.palabra == Sustantivo)
                {
                    sustantivo = i;
                    break;
                }
            }

            foreach (Sustantivo i in biblioteca.sustantivospropios)
            {
                if (i.palabra == Sustantivo)
                {
                    sustantivo = i;
                    break;
                }
            }

            foreach (Verbo i in biblioteca.verbos)
            {
                if (i.palabra == Verbo)
                {
                    verbo = i;
                    break;
                }
            }


            if (sustantivo != null && verbo != null)
            {
                if (sustantivo.verbos.Contains(verbo))
                    return;

                sustantivo.verbos.Add(verbo);
                verbo.sustantivos.Add(sustantivo);
            }
        }

        public void AsignarAdjetivoaSustantivo(string Sustantivo, string Adjetivo, string Funcion)
        {
            Sustantivo sustantivo = null;
            Adjetivo adjetivo = null;
            foreach (Sustantivo i in biblioteca.sustantivoscomunes)
            {
                if (i.palabra == Sustantivo)
                {
                    sustantivo = i;
                    break;
                }
            }

            foreach (Sustantivo i in biblioteca.sustantivospropios)
            {
                if (i.palabra == Sustantivo)
                {
                    sustantivo = i;
                    break;
                }
            }

            foreach (Adjetivo i in biblioteca.adjetivos)
            {
                if (i.palabra == Adjetivo)
                {
                    adjetivo = i;
                    break;
                }
            }


            if (sustantivo != null && adjetivo != null)
            {
                if (Funcion == "Atributo")
                {
                    sustantivo.adjetivosatributos.Add(adjetivo);
                }
                if (Funcion == "Estado")
                {
                    sustantivo.adjetivoestado.Add(adjetivo);
                }
                if (Funcion == "Relacional")
                {
                    sustantivo.adjetivosrelacionales.Add(adjetivo);
                }
                if (Funcion == "Indefinido")
                {
                    sustantivo.adjetivosindefinidos.Add(adjetivo);
                }
                if (Funcion == "Posesivo")
                {
                    sustantivo.adjetivosposesivos.Add(adjetivo);
                }
                if (Funcion == "Explicativo")
                {
                    sustantivo.adjetivosexplicativos.Add(adjetivo);
                }
                if (Funcion == "Calificativo")
                {
                    sustantivo.adjetivoscalificativos.Add(adjetivo);
                }
            }
        }

        public void AsignarSustantivoaVerbo(string Verbo, string Sustantivo)
        {
            Sustantivo sustantivo = null;
            Verbo verbo = null;
            foreach (Sustantivo i in biblioteca.sustantivoscomunes)
            {
                if (i.palabra == Sustantivo)
                {
                    sustantivo = i;
                    break;
                }
            }

            foreach (Sustantivo i in biblioteca.sustantivospropios)
            {
                if (i.palabra == Sustantivo)
                {
                    sustantivo = i;
                    break;
                }
            }

            foreach (Verbo i in biblioteca.verbos)
            {
                if (i.palabra == Verbo)
                {
                    verbo = i;
                    break;
                }
            }


            if (sustantivo != null && verbo != null)
            {
                if (verbo.sustantivos.Contains(sustantivo))
                    return;
                verbo.sustantivos.Add(sustantivo);
                sustantivo.verbos.Add(verbo);
            }
        }

        public void AsignarAdjetivoaVerbo(string Verbo, string Adjetivo)
        {
            Verbo verbo = null;
            Adjetivo adjetivo = null;
            foreach (Verbo i in biblioteca.verbos)
            {
                if (i.palabra == Verbo)
                {
                    verbo = i;
                    break;
                }
            }

            foreach (Adjetivo i in biblioteca.adjetivos)
            {
                if (i.palabra == Adjetivo)
                {
                    adjetivo = i;
                    break;
                }
            }


            if (verbo != null && adjetivo != null)
            {
                if (verbo.adjetivos.Contains(adjetivo))
                    return;
                verbo.adjetivos.Add(adjetivo);
            }
        }

        public void DesasignarVerboSustantivo(string Verbo, string Sustantivo)
        {
            Verbo verbo = null;
            Sustantivo sustantivo = null;

            foreach (Verbo i in biblioteca.verbos)
            {
                if (Verbo == i.palabra)
                {
                    verbo = i;
                    break;
                }
            }

            foreach (Sustantivo i in biblioteca.sustantivoscomunes)
            {
                if (Sustantivo == i.palabra)
                {
                    sustantivo = i;
                    break;
                }
            }

            foreach (Sustantivo i in biblioteca.sustantivospropios)
            {
                if (Sustantivo == i.palabra)
                {
                    sustantivo = i;
                    break;
                }
            }

            if (verbo != null && sustantivo != null)
            {
                verbo.sustantivos.Remove(sustantivo);
                sustantivo.verbos.Remove(verbo);
            }


        }

        public void DesasignarAdjetivoaSustantivo(string Sustantivo, string Adjetivo)
        {
            Adjetivo adjetivo = null;
            Sustantivo sustantivo = null;

            foreach (Adjetivo i in biblioteca.adjetivos)
            {
                if (Adjetivo == i.palabra)
                {
                    adjetivo = i;
                    break;
                }
            }

            foreach (Sustantivo i in biblioteca.sustantivoscomunes)
            {
                if (Sustantivo == i.palabra)
                {
                    sustantivo = i;
                    break;
                }
            }

            foreach (Sustantivo i in biblioteca.sustantivospropios)
            {
                if (Sustantivo == i.palabra)
                {
                    sustantivo = i;
                    break;
                }
            }

            if (adjetivo != null && sustantivo != null)
            {
                sustantivo.adjetivosrelacionales.Remove(adjetivo);

                sustantivo.adjetivosindefinidos.Remove(adjetivo);

                sustantivo.adjetivosposesivos.Remove(adjetivo);

                sustantivo.adjetivosatributos.Remove(adjetivo);

                sustantivo.adjetivosexplicativos.Remove(adjetivo);

                sustantivo.adjetivoscalificativos.Remove(adjetivo);
            }
        }

        public void DesasignarAdjetivoaVerbo(string Verbo, string Adjetivo)
        {
            Adjetivo adjetivo = null;
            Verbo verbo = null;

            foreach (Adjetivo i in biblioteca.adjetivos)
            {
                if (Adjetivo == i.palabra)
                {
                    adjetivo = i;
                    break;
                }
            }

            foreach (Verbo i in biblioteca.verbos)
            {
                if (Verbo == i.palabra)
                {
                    verbo = i;
                    break;
                }
            }

            if (adjetivo != null && verbo != null)
            {
                verbo.adjetivos.Remove(adjetivo);
            }
        }
        #endregion

        public void SustantivoAgregarPath(string sustantivo, string path)
        {
            if (path == null)
                return;
            Sustantivo sust = biblioteca.sustantivoscomunes.Find(a => a.formas_nucleares[0].ToString() == sustantivo);
            sust.path_imagen_asociada = path;
        }


    }
}

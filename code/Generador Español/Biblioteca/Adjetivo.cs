using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Biblioteca
{
    [Serializable]
    public class Adjetivo:Palabra
    {
        public enum Unico { forma, color, textura, olor, sabor, tamaño, aspecto, otro };

        public Unico unico;

        public string[] silabas_singular_masculino;
        public string[] silabas_singular_femenino;
        public string[] silabas_plural_masculino;
        public string[] silabas_plural_femenino;
        public string[] silabas_superlativo_masculino;
        public string[] silabas_superlativo_femenina;

        public string palabra_singular_masculino;
        public string palabra_singular_femenino;
        public string palabra_plural_masculino;
        public string palabra_plural_femenino;
        public string palabra_superlativa_masculina;
        public string palabra_superlativa_femenina;



        public Adjetivo(string[] SilabasSingularMasculino, string[] SilabasSingularFemenino, string[] SilabasPluralMasculino, string[] SilabasPluralFemenino,
            string[] SilabasSuperlativoMasculino, string[] SilabasSuperlativaFemenina, Unico unico):base()
        {
            this.silabas_singular_masculino = SilabasSingularMasculino;
            this.silabas_singular_femenino = SilabasSingularFemenino;
            this.silabas_plural_masculino = SilabasPluralMasculino;
            this.silabas_plural_femenino = SilabasPluralFemenino;
            this.silabas_superlativo_masculino = SilabasSuperlativoMasculino;
            this.silabas_superlativo_femenina = SilabasSuperlativaFemenina;

            foreach (string i in SilabasSingularMasculino)
                palabra_singular_masculino += i;
            foreach (string i in SilabasSingularFemenino)
                palabra_singular_femenino += i;
            foreach (string i in SilabasPluralMasculino)
                palabra_plural_masculino += i;
            foreach (string i in SilabasPluralFemenino)
                palabra_plural_femenino += i;
            foreach (string i in SilabasSuperlativoMasculino)
                palabra_superlativa_masculina += i;
            foreach (string i in SilabasSuperlativaFemenina)
                palabra_superlativa_femenina += i;

            this.unico = unico;

            if (silabas_singular_masculino != null)
            {
                this.Construir(silabas_singular_masculino);
                return;
            }

            else if (silabas_singular_femenino != null)
            {
                this.Construir(silabas_singular_femenino);
                return;
            }

            else if (silabas_plural_masculino != null)
            {
                this.Construir(silabas_plural_masculino);
                return;
            }

            else if (silabas_plural_femenino != null)
            {
                this.Construir(silabas_plural_femenino);
                return;
            }

            else if (silabas_superlativo_masculino != null)
            {
                this.Construir(silabas_superlativo_masculino);
                return;
            }

            else if (silabas_superlativo_femenina != null)
            {
                this.Construir(silabas_superlativo_femenina);
                return;
            }
        }

        public Adjetivo(string[] palabra)
            : base(palabra)
        {
        }


        /// <summary>
        /// 
        /// </summary>
        /// <param name="id_persona">Usar la persona de Onoma</param>
        /// <param name="genero">No se requiere para tercera persona</param>
        /// <returns></returns>
        public Adjetivo Obtener_Adjetivo(int id_persona, BibliotecaCentral.Genero genero)
        {
            if (id_persona == 5)
                return new Adjetivo(silabas_singular_masculino);

            else if (id_persona == 6)
                return new Adjetivo(silabas_singular_femenino);

            else if (id_persona == 8)
                return new Adjetivo(silabas_plural_masculino);

            else if (id_persona == 9)
                return new Adjetivo(silabas_plural_femenino);

            else if (id_persona == 12)
                return new Adjetivo(silabas_plural_masculino);

            else if (id_persona == 13)
                return new Adjetivo(silabas_plural_masculino);

            else if (id_persona == 14)
                return new Adjetivo(silabas_plural_femenino);

            else if (id_persona == 1 && genero == BibliotecaCentral.Genero.masculino)
                return new Adjetivo(silabas_singular_masculino);

            else if (id_persona == 1 && genero == BibliotecaCentral.Genero.femenino)
                return new Adjetivo(silabas_singular_femenino);

            else if (id_persona == 2 && genero == BibliotecaCentral.Genero.masculino)
                return new Adjetivo(silabas_singular_masculino);

            else if (id_persona == 2 && genero == BibliotecaCentral.Genero.femenino)
                return new Adjetivo(silabas_singular_femenino);

            else if (id_persona == 3 && genero == BibliotecaCentral.Genero.masculino)
                return new Adjetivo(silabas_singular_masculino);

            else if (id_persona == 3 && genero == BibliotecaCentral.Genero.femenino)
                return new Adjetivo(silabas_singular_femenino);

            else if (id_persona == 7)
                return new Adjetivo(silabas_singular_masculino);

            else if (id_persona == 4 && genero == BibliotecaCentral.Genero.masculino)
                return new Adjetivo(silabas_singular_masculino);

            else if (id_persona == 4 && genero == BibliotecaCentral.Genero.femenino)
                return new Adjetivo(silabas_singular_femenino);

            else if (id_persona == 10)
                return new Adjetivo(silabas_plural_masculino);

            else // persona == 11
                return new Adjetivo(silabas_plural_femenino);

            
        }




    }
}

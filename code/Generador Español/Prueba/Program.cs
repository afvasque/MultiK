using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using Biblioteca;
using System.Runtime.Serialization.Formatters.Binary;
using System.IO;
using System.Xml.Serialization;
using GeneradorTexto;
using MySql.Data.MySqlClient;


namespace Prueba
{
    class Program
    {
        static void Main(string[] args)
        {
            BibliotecaCentral biblioteca = new Biblioteca.BibliotecaCentral();
            string ubicacion = "SustantivosFinal.multik";


            using (Stream stream = File.Open(ubicacion, FileMode.Open))
            {
                BinaryFormatter bin = new BinaryFormatter();
                biblioteca = (Biblioteca.BibliotecaCentral)bin.Deserialize(stream);
            }

            biblioteca.Inicializar();
            Generador gen = new Generador(biblioteca, "localhost", "mibase", "root", "h");


            for (int i = 0; i < 80; i++)
            {
                Console.WriteLine(gen.Ser());
            }

            Console.ReadKey();
            Console.ReadKey();

            using (Stream stream = File.Open("SustantivosFinal.multik", FileMode.Create))
            {
                BinaryFormatter bin = new BinaryFormatter();
                bin.Serialize(stream, biblioteca);
            }

            Console.ReadKey();
            Console.ReadKey();

        }
    }
}

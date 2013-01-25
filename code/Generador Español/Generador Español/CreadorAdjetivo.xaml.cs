using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Shapes;
using Biblioteca;
using ModificadorBaseDato;

namespace Generador_Español
{
    /// <summary>
    /// Lógica de interacción para CreadorAdjetivo.xaml
    /// </summary>
    public partial class CreadorAdjetivo : Window
    {
        Modificador modificador;
        List<string> silabas = new List<string>();
        public Dictionary<string,Adjetivo.Unico> diccionario = new Dictionary<string,Adjetivo.Unico>();

        public CreadorAdjetivo(Modificador modificador)
        {
            InitializeComponent();
            this.modificador = modificador;

            bool continuar = true;
            int contador = 0;

            while (continuar)
            {
                Adjetivo.Unico unico = (Adjetivo.Unico)contador;
                if (unico.ToString().Length > 2)
                {
                    diccionario.Add(unico.ToString(), unico);
                    ComboBoxItem item = new ComboBoxItem();
                    item.Content = unico.ToString();
                    Caracter_ComboBox.Items.Add(item);
                }
                else
                    continuar = false;

                contador++;
            }


        }

        private void Ingresar_Click(object sender, RoutedEventArgs e)
        {
            TextBox[] textbox1 = { SilabasMasculinoSingular1 , SilabasMasculinoSingular2,
             SilabasMasculinoSingular3, SilabasMasculinoSingular4, SilabasMasculinoSingular5};

            TextBox[] textbox2 = { SilabasMasculinoPlural1, SilabasMasculinoPlural2, SilabasMasculinoPlural3,
             SilabasMasculinoPlural4, SilabasMasculinoPlural5};

            TextBox[] textbox3 = { SilabasFemeninoSingular1, SilabasFemeninoSingular2, SilabasFemeninoSingular3,
                                     SilabasFemeninoSingular4, SilabasFemeninoSingular5};

            TextBox[] textbox4 = { SilabasFemeninoPlural1, SilabasFemeninoPlural2, SilabasFemeninoPlural3,
                                     SilabasFemeninoPlural4, SilabasFemeninoPlural5};

            TextBox[] textbox5 = { SilabaSuperlativoM1, SilabaSuperlativoM2, SilabaSuperlativoM3,
                                     SilabaSuperlativoM4, SilabaSuperlativoM5 };

            TextBox[] textbox6 = { SilabaSuperlativoF1, SilabaSuperlativoF2, SilabaSuperlativoF3, SilabaSuperlativoF4, SilabaSuperlativoF5 };

            ComboBoxItem item = (ComboBoxItem)Caracter_ComboBox.SelectedItem;

            Adjetivo.Unico unico = diccionario[item.Content.ToString()];

            modificador.AgregarAdjetivo(JuntarSilabas(textbox1), JuntarSilabas(textbox2),
                JuntarSilabas(textbox3), JuntarSilabas(textbox4), JuntarSilabas(textbox5), JuntarSilabas(textbox6),unico);

            CreadorAdjetivo creadoradjetivo = new CreadorAdjetivo(modificador);
            creadoradjetivo.Show();
            this.Close();
        }

        private string[] JuntarSilabas(TextBox[] textboxes)
        {
            silabas.Clear();
            foreach (TextBox i in textboxes)
            {
                if (i.GetLineText(0) != "")
                    silabas.Add(i.GetLineText(0).ToLower());
                i.Clear();
            }
            return silabas.ToArray();
        }
    }
}

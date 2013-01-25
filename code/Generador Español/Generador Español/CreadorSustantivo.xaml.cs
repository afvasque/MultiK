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
using ModificadorBaseDato;
using Biblioteca;

namespace Generador_Español
{
    /// <summary>
    /// Lógica de interacción para CreadorSustantivo.xaml
    /// </summary>
    public partial class CreadorSustantivo : Window
    {
        Modificador modificador;
        List<string> silabas = new List<string>();
        bool escomun, escontable;

        public CreadorSustantivo(Modificador modificador)
        {
            InitializeComponent();
            this.modificador = modificador;
            Tipo.SelectedItem = ViñetaComun;
            Contabilidad.SelectedItem = ViñetaContable;
        }

        private void Ingresar_Click(object sender, RoutedEventArgs e)
        {
            ComboBoxItem itemtipo = (ComboBoxItem)Tipo.SelectedItem;
            ComboBoxItem itemcontabilidad = (ComboBoxItem)Contabilidad.SelectedItem;

            if (itemtipo.Content.ToString() == "Comun")
                escomun = true;

            else if (itemtipo.Content.ToString() == "Propio")
                escomun = false;

            if (itemcontabilidad.Content.ToString() == "Contable")
                escontable = true;

            else if (itemcontabilidad.Content.ToString() == "Incontable")
                escontable = false;

            TextBox[] textbox1 = { SilabasMasculinoSingular1 , SilabasMasculinoSingular2,
             SilabasMasculinoSingular3, SilabasMasculinoSingular4, SilabasMasculinoSingular5};

            TextBox[] textbox2 = { SilabasMasculinoPlural1, SilabasMasculinoPlural2, SilabasMasculinoPlural3,
             SilabasMasculinoPlural4, SilabasMasculinoPlural5};

            TextBox[] textbox3 = { SilabasFemeninoSingular1, SilabasFemeninoSingular2, SilabasFemeninoSingular3,
                                     SilabasFemeninoSingular4, SilabasFemeninoSingular5};

            TextBox[] textbox4 = { SilabasFemeninoPlural1, SilabasFemeninoPlural2, SilabasFemeninoPlural3,
                                     SilabasFemeninoPlural4, SilabasFemeninoPlural5};

            modificador.AgregarSustantivo(escomun, escontable, JuntarSilabas(textbox1), JuntarSilabas(textbox3),
                JuntarSilabas(textbox2), JuntarSilabas(textbox4), null);

            CreadorSustantivo creador = new CreadorSustantivo(modificador);
            creador.Show();
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
            if (silabas.Count() == 0)
                return null;
            return silabas.ToArray();
        }
    }
}

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
    /// Lógica de interacción para CreadorArticulo.xaml
    /// </summary>
    public partial class CreadorArticulo : Window
    {
        Modificador modificador;
        List<string> silabas = new List<string>();
        BibliotecaCentral.Genero genero;
        bool essingular, esdeterminado;

        public CreadorArticulo(Modificador modificador)
        {
            InitializeComponent();
            this.modificador = modificador;
        }

        private void Ingresar_Click(object sender, RoutedEventArgs e)
        {
            ComboBoxItem itemgenero = (ComboBoxItem)Genero.SelectedItem;
            ComboBoxItem itemnumero = (ComboBoxItem)Numero.SelectedItem;
            ComboBoxItem itemtipo = (ComboBoxItem)Tipo.SelectedItem;

            if (itemgenero.Content.ToString() == "Masculino")
                genero = BibliotecaCentral.Genero.masculino;

            else if (itemgenero.Content.ToString() == "Femenino")
                genero = BibliotecaCentral.Genero.femenino;

            else if (itemgenero.Content.ToString() == "Neutro")
                genero = BibliotecaCentral.Genero.neutro;

            if (itemnumero.Content.ToString() == "Singular")
                essingular = true;

            else if (itemnumero.Content.ToString() == "Plural")
                essingular = false;

            if (itemtipo.Content.ToString() == "Determinado")
                esdeterminado = true;

            else if (itemtipo.Content.ToString() == "Indeterminado")
                esdeterminado = false;

            #region RegionComunACreadores

            if (Silaba1.GetLineText(0) != "")
            {
                silabas.Add(Silaba1.GetLineText(0));
                Silaba1.Clear();
            }

            if (Silaba2.GetLineText(0) != "")
            {
                silabas.Add(Silaba2.GetLineText(0));
                Silaba2.Clear();
            }

            if (Silaba3.GetLineText(0) != "")
            {
                silabas.Add(Silaba3.GetLineText(0));
                Silaba3.Clear();
            }

            if (Silaba4.GetLineText(0) != "")
            {
                silabas.Add(Silaba4.GetLineText(0));
                Silaba4.Clear();
            }

            if (Silaba5.GetLineText(0) != "")
            {
                silabas.Add(Silaba5.GetLineText(0));
                Silaba5.Clear();
            }

            if (Silaba6.GetLineText(0) != "")
            {
                silabas.Add(Silaba6.GetLineText(0));
            }

            if (Silaba7.GetLineText(0) != "")
            {
                silabas.Add(Silaba7.GetLineText(0));
            }

            #endregion

            modificador.AgregarArticulo(genero, esdeterminado, essingular, silabas.ToArray());
            this.Close();
        }

    }
}


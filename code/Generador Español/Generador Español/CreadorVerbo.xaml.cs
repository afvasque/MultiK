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
    /// Lógica de interacción para CreadorVerbo.xaml
    /// </summary>
    public partial class CreadorVerbo : Window
    {
        Modificador modificador;
        List<string> silabas = new List<string>();
        int id;

        public CreadorVerbo(Modificador modificador)
        {
            InitializeComponent();
            this.modificador = modificador;
        }

        private void Ingresar_Click(object sender, RoutedEventArgs e)
        {


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

            id = int.Parse(id_onoma.GetLineText(0));

            modificador.AgregarVerbo(silabas.ToArray(),id);
            this.Close();
        }
    }
}
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

namespace Generador_Español
{
    /// <summary>
    /// Lógica de interacción para VentanaCierre.xaml
    /// </summary>
    public partial class VentanaCierre : Window
    {
        Modificador modificador;
        public VentanaCierre(Modificador modificador)
        {
            this.modificador = modificador;
            InitializeComponent();
        }

        private void button1_Click(object sender, RoutedEventArgs e)
        {
            modificador.Guardar();
            this.Close();
        }

        private void button2_Click(object sender, RoutedEventArgs e)
        {
            this.Close();
        }
    }
}
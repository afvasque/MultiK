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
using System.Windows.Navigation;
using System.Windows.Shapes;
using ModificadorBaseDato;
using Microsoft.Win32;
using System.IO;
using GeneradorTexto;
using System.Threading;
using System.Diagnostics;

namespace Generador_Español
{
    /// <summary>
    /// Lógica de interacción para MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        Modificador modificador;
        Generador generador;
        string elementovisualizar;
        string palabramodificar;
        string palabravisualizada;

        public MainWindow()
        {
            Closing += new System.ComponentModel.CancelEventHandler(MainWindow_Closing);
            InitializeComponent();
        }

        void MainWindow_Closing(object sender, System.ComponentModel.CancelEventArgs e)
        {
            if (modificador == null)
                return;
            VentanaCierre ventanacierre = new VentanaCierre(modificador);
            ventanacierre.Show();
        }

        #region VisualEvents

        private void IngresarPalabra_Click(object sender, RoutedEventArgs e)
        {
            if (modificador == null)
            {
                palabraencreacion.SelectedItem = null;
                Advertencia advertencia = new Advertencia();
                advertencia.Show();
                return;
            }
            ComboBoxItem itemseleccionado = (ComboBoxItem)palabraencreacion.SelectedItem;
            if (itemseleccionado == null)
                return;
            if (itemseleccionado.Content.ToString() == "Adjetivo")
            {
                CreadorAdjetivo creadoradjetivo = new CreadorAdjetivo(modificador);
                creadoradjetivo.Show();
            }

            else if (itemseleccionado.Content.ToString() == "Adverbio")
            {
            }

            else if (itemseleccionado.Content.ToString() == "Articulo")
            {
                CreadorArticulo creadorarticulo = new CreadorArticulo(modificador);
                creadorarticulo.Show();
            }

            else if (itemseleccionado.Content.ToString() == "Predeterminante")
            {
            }

            else if (itemseleccionado.Content.ToString() == "Pronombre")
            {
            }

            else if (itemseleccionado.Content.ToString() == "Sustantivo")
            {
                CreadorSustantivo creadorsustantivo = new CreadorSustantivo(modificador);
                creadorsustantivo.Show();
            }

            else if (itemseleccionado.Content.ToString() == "Verbo")
            {
                CreadorVerbo creadorverbo = new CreadorVerbo(modificador);
                creadorverbo.Show();
            }

            else
                throw new Exception();
            palabraencreacion.SelectedItem = null;

        }

        private void AbrirBiblioteca_Click(object sender, RoutedEventArgs e)
        {
            OpenFileDialog openFileDialog1 = new OpenFileDialog();
            openFileDialog1.InitialDirectory = Directory.GetCurrentDirectory();
            openFileDialog1.Filter = "Archivos de datos (*.multik)|*.multik";
            openFileDialog1.ShowDialog();
            string link = openFileDialog1.FileName;
            if (link != null && link != "")
            {
                modificador = new Modificador(link);
            }
            generador = new Generador(Modificador.biblioteca,"localhost","mibase","root","h");
        }

        private void CrearBiblioteca_Click(object sender, RoutedEventArgs e)
        {
            string nombrebiblioteca = NombreBiblioteca.GetLineText(0);
            SaveFileDialog save = new SaveFileDialog();
            save.AddExtension = true;
            save.DefaultExt = ".xml";
            save.FileName = nombrebiblioteca;
            save.Filter = "Archivos de datos (*.xml)|*.xml";
            save.ShowDialog();
            modificador = new Modificador(save.FileName, "cualquiercosa");
            generador = new Generador(Modificador.biblioteca, "localhost", "mibase", "root", "h");
        }

        private void GuardarBiblioteca_Click(object sender, RoutedEventArgs e)
        {
            if (modificador == null)
            {
                Advertencia advertencia = new Advertencia();
                advertencia.Show();
                return;
            }
            modificador.Guardar();
        }

        private void ComboBoxItem_MouseMove(object sender, MouseEventArgs e)
        {
            if (modificador == null)
            {
                Advertencia advertencia = new Advertencia();
                advertencia.Show();
                return;
            }
            ComboBoxItem item = (ComboBoxItem)sender;
            string[] visualizaciones = { "error" };
            if (item.Content.ToString() != elementovisualizar)
            {
                elementovisualizar = item.Content.ToString();
                ListaVisualizar.Items.Clear();

                if (elementovisualizar == "Adjetivos")
                {
                    visualizaciones = modificador.SolicitarAdjetivos();
                }

                else if (elementovisualizar == "Articulos")
                {
                    visualizaciones = modificador.SolicitarArticulos();
                }

                else if (elementovisualizar == "Pronombres")
                {
                    visualizaciones = modificador.SolicitarPronombres();
                }

                else if (elementovisualizar == "Sustantivos")
                {
                    visualizaciones = modificador.SolicitarSustantivos();
                }

                else if (elementovisualizar == "Verbos")
                {
                    visualizaciones = modificador.SolicitarVerbos();
                }

                foreach (string i in visualizaciones)
                {
                    ListBoxItem itemvisualizar = new ListBoxItem();
                    itemvisualizar.Content = i;
                    ListaVisualizar.Items.Add(itemvisualizar);
                }

            }

        }

        private void PalabraModificada_SelectionChanged(object sender, SelectionChangedEventArgs e)
        {
            ListBox box = (ListBox)sender;
            ListBoxItem item = (ListBoxItem)box.SelectedItem;
            if (item != null)
                palabramodificar = item.Content.ToString();
        }

        private void EliminarPalabra_Click(object sender, RoutedEventArgs e)
        {
            ComboBoxItem item = (ComboBoxItem)ElementosVisualizar.SelectedItem;
            if (palabravisualizada == null)
                return;
            if (item.Content.ToString() == "Articulos")
                modificador.EliminarArticulo(palabravisualizada);
            else if (item.Content.ToString() == "Sustantivos")
                modificador.EliminarSustantivo(palabravisualizada);
            else if (item.Content.ToString() == "Verbos")
                modificador.EliminarVerbo(palabravisualizada);
            else if (item.Content.ToString() == "Adjetivos")
                modificador.EliminarAdjetivo(palabravisualizada);
        }

        private void ListaVisualizar_SelectionChanged(object sender, SelectionChangedEventArgs e)
        {
            ListBox box = (ListBox)sender;
            ListBoxItem item = (ListBoxItem)box.SelectedItem;
            if (item != null)
                palabravisualizada = item.Content.ToString();
        }

        private void ElementosModificar_SelectionChanged(object sender, SelectionChangedEventArgs e)
        {
            ComboBox box = (ComboBox)sender;
            ComboBoxItem item = (ComboBoxItem)box.SelectedItem;

            PalabraModificada.Items.Clear();

            if (item.Content.ToString() == "Sustantivos")
            {
                foreach (string i in modificador.SolicitarSustantivos())
                {
                    ListBoxItem palabra = new ListBoxItem();
                    palabra.Content = i;
                    PalabraModificada.Items.Add(palabra);
                }
            }

            else if (item.Content.ToString() == "Verbos")
            {
                foreach (string i in modificador.SolicitarVerbos())
                {
                    ListBoxItem palabra = new ListBoxItem();
                    palabra.Content = i;
                    PalabraModificada.Items.Add(palabra);
                }
            }

        }

        private void Modificar_Click(object sender, RoutedEventArgs e)
        {
            ComboBoxItem item = (ComboBoxItem)ElementosModificar.SelectedItem;
            if (item.Content.ToString() == "Sustantivos")
            {
                ModificadorSustantivo mod = new ModificadorSustantivo(modificador, palabramodificar);
                mod.Show();
            }
        }

        #endregion

        private void GenerarOracionBasica_Click(object sender, RoutedEventArgs e)
        {

            string prueba1 = generador.generador_palabra_contiene("a");
            if (true)
            {
            }



        }

        private void Readme_Click(object sender, RoutedEventArgs e)
        {
            Process notepad = new Process();
            ProcessStartInfo info = new ProcessStartInfo("Notepad", "readme.txt");
            notepad.StartInfo = info;
            notepad.Start();
        }
    }
}

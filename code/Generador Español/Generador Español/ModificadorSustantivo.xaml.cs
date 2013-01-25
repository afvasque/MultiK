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
using Microsoft.Win32;

namespace Generador_Español
{
    /// <summary>
    /// Lógica de interacción para ModificadorSustantivo.xaml
    /// </summary>
    public partial class ModificadorSustantivo : Window
    {
        Modificador modificador;
        string sustantivo;
        string palabradisponible, palabraasignada;
        public ModificadorSustantivo(Modificador modificador, string sustantivo)
        {
            InitializeComponent();
            this.modificador = modificador;
            this.sustantivo = sustantivo;
            PalabraModificada.Content = sustantivo;
        }

        private void PalabraAsignada_SelectionChanged(object sender, SelectionChangedEventArgs e)
        {
            PalabrasDisponibles.Items.Clear();
            PalabrasAsignadas.Items.Clear();

            ComboBox box = (ComboBox)sender;
            ComboBoxItem item = (ComboBoxItem)box.SelectedItem;
            if (item.Content.ToString() == "Adjetivos")
            {
                foreach (string i in modificador.SolicitarAdjetivos())
                {
                    ListBoxItem l_item = new ListBoxItem();
                    l_item.Content = i;
                    PalabrasDisponibles.Items.Add(l_item);
                }

                foreach (string i in modificador.SolicitarAdjetivosdeSustantivo(sustantivo))
                {
                    ListBoxItem l_item = new ListBoxItem();
                    l_item.Content = i;
                    PalabrasAsignadas.Items.Add(l_item);
                }

            }

            else
            {
                foreach (string i in modificador.SolicitarVerbos())
                {
                    ListBoxItem l_item = new ListBoxItem();
                    l_item.Content = i;
                    PalabrasDisponibles.Items.Add(l_item);
                }
                foreach (string i in modificador.SolicitarVerbosdeSustantivo(sustantivo))
                {
                    ListBoxItem l_item = new ListBoxItem();
                    l_item.Content = i;
                    PalabrasAsignadas.Items.Add(l_item);
                }
            }

            #region Asignacion Funciones

            FuncionPalabraAsignar.Items.Clear();
            if (item.Content.ToString() == "Adjetivos")
            {
                ComboBoxItem atributo = new ComboBoxItem();
                ComboBoxItem estado = new ComboBoxItem();

                ComboBoxItem relacional = new ComboBoxItem();
                ComboBoxItem indefinido = new ComboBoxItem();
                ComboBoxItem posesivo = new ComboBoxItem();
                ComboBoxItem explicativo = new ComboBoxItem();
                ComboBoxItem calificativo = new ComboBoxItem();

                estado.Content = "Estado";
                relacional.Content = "Relacional";
                indefinido.Content = "Indefinido";
                posesivo.Content = "Posesivo";
                atributo.Content = "Atributo";
                explicativo.Content = "Explicativo";
                calificativo.Content = "Calificativo";

                FuncionPalabraAsignar.Items.Add(estado);
                FuncionPalabraAsignar.Items.Add(relacional);
                FuncionPalabraAsignar.Items.Add(indefinido);
                FuncionPalabraAsignar.Items.Add(posesivo);
                FuncionPalabraAsignar.Items.Add(atributo);
                FuncionPalabraAsignar.Items.Add(explicativo);
                FuncionPalabraAsignar.Items.Add(calificativo);
            }



            #endregion

        }

        private void PalabrasAsignadas_SelectionChanged(object sender, SelectionChangedEventArgs e)
        {
            ListBox box = (ListBox)sender;
            ListBoxItem item = (ListBoxItem)box.SelectedItem;
            if (item != null)
                palabraasignada = item.Content.ToString();
        }

        private void PalabrasDisponibles_SelectionChanged(object sender, SelectionChangedEventArgs e)
        {

            ListBox box = (ListBox)sender;
            ListBoxItem item = (ListBoxItem) box.SelectedItem;
            if (item != null)
                palabradisponible = (string)item.Content;
        }

        private void Asignar_Click(object sender, RoutedEventArgs e)
        {
            ComboBoxItem disponible = (ComboBoxItem)PalabraAsignada.SelectedItem;
            ComboBoxItem funcion = (ComboBoxItem)FuncionPalabraAsignar.SelectedItem;

            if (disponible.Content.ToString() == "Verbos")
            {
                modificador.AsignarVerboaSustantivo(sustantivo, palabradisponible);
            }

            else
            {
                if (funcion == null)
                {
                    AdvertenciaFuncion advertencia = new AdvertenciaFuncion();
                    advertencia.Show();
                    return;
                }

                modificador.AsignarAdjetivoaSustantivo(sustantivo, palabradisponible, funcion.Content.ToString());
            }


            this.PalabraAsignada_SelectionChanged(PalabraAsignada, null);
        }

        private void Desasignar_Click(object sender, RoutedEventArgs e)
        {
            ComboBoxItem disponible = (ComboBoxItem)PalabraAsignada.SelectedItem;
            ComboBoxItem funcion = (ComboBoxItem)FuncionPalabraAsignar.SelectedItem;

            if (disponible.Content.ToString() == "Verbos")
                modificador.DesasignarVerboSustantivo(sustantivo, palabradisponible);


            else
                modificador.DesasignarAdjetivoaSustantivo(sustantivo, palabradisponible);
            this.PalabraAsignada_SelectionChanged(PalabraAsignada, null);
        }

        private void Boton_Aceptar_Click(object sender, RoutedEventArgs e)
        {
            this.Close();
        }

        private void Boton_Ingresar_Click(object sender, RoutedEventArgs e)
        {
            OpenFileDialog open = new OpenFileDialog();
            open.ShowDialog();
            modificador.SustantivoAgregarPath(sustantivo, open.SafeFileName);
        }

    }
}

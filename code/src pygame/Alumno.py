

class Alumno:
    #   string nombre;
    #  string apellido;
    #    int id;
    #    string simbolo;
    #    string dni;
    #    bool seleccionado = false; # determina si un alumno está asociado a un teclado

    #Tiempo en que el niño aparece en pantalla previo a la liberacion
    #public DateTime TiempoInicioReconocimiento;

    #  //Tiempo en que el niño aparece en pantalla previo a la liberacion
    #  public DateTime TiempoFinalReconocimiento;

    def __init__(self, Id, Nombre, Apellido):
        self.Id=Id
        self.Nombre=Nombre
        self.Apellido=Apellido
        #self.simbolo= simbolo
        

     

        #region IComparable<Alumno> Members
'''
        /// <summary>
        /// Compara alfabeticamente dos alumnos, primero por el apellido y despues por el nombre.
        /// </summary>
        /// <param name="other"></param>
        /// <returns></returns>
        public int CompareTo(Alumno other)
        {
            return string.Compare(NombreCompleto, other.NombreCompleto, StringComparison.CurrentCultureIgnoreCase);
        }

        #endregion

'''

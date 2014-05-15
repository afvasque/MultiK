

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

    def __init__(self, Id):
        self.Id=Id
        self.Nombre=""
        self.Apellido=""
        self.ready = False
        self.nro_lista= ""
        

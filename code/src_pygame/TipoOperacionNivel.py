


class TipoOperacion:
    primero=1
    segundo=2
    tercero=3
    cuarto=4
    quinto=5
    sexto=6

# Establece que sucede con el nivel del alumno    
class CambioNivel:
    Mantiene=1
    Sube=2

class TipoOperacionNivel:
    
    TipoOpGlobal= None
    NivelGlobal= None
    
    def __init__(self, nivel, tipo_op):
        self.nivel = nivel
        self.tipo_op = tipo_op
        self.notNull= True
        TipoOpGlobal= tipo_op
        NivelGlobal= nivel

    def IsOpNivel(self, nivel, op):
        return (self.nivel == nivel and self.tipo_op==op)

    @staticmethod
    def InttoTipoOperacion(nivel):
        if nivel==1:
            return TipoOperacion.primero
        elif nivel==2:
            return TipoOperacion.segundo
        elif nivel==3:
            return TipoOperacion.tercero
        elif nivel==4:
            return TipoOperacion.cuarto
        elif nivel==5:
            return TipoOperacion.quinto
        elif nivel==6:
            return TipoOperacion.sexto




import random

class Generador_pal:
    
    def __init__(self, archivo):
        self.archivo=archivo
        
        return
    
    def generador_letra_alfabeto(self):
        azar= random.randrange(0,4)
        
        if azar==0:        
            return "a"
        elif azar==1:
            return "b"
        elif azar==2:
            return "f"
        elif azar==3:
            return "j"
        elif azar==4:
            return "m"
    
    def generador_palabra_contiene(self, letra):
        return letra+"prueba"
        
    def generador_palabra_no_contine(self, letra):
        return "nocont"+letra
    
    def generador_palabra_silaba(self, silaba):
        if silaba == 1:
            return "sol"
        elif silaba == 2:
            return "casa"
        elif silaba ==3:
            return "camara"
        
    def generador_sust_propio(self,propio):
        if propio == True:
            return "Pedro"
        else:
            return "perro"
        
        
        
class Generador_or:
    
    def __init__(self, archivo):
        self.archivo=archivo
        
    def generador_pregunta_exclamacion(self, num):
        return "pregunta "+num
    
    def generador_oracion_propio_comun(self):
        return "oracion propio comun"
    
    
    
    
    
    
    
    
    
        
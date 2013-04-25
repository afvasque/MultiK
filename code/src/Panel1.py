# coding=utf-8
#Boa:FramePanel:Panel1

import wx
import os
import audio_library
from Reglas import *
from socket import *
import sys
import multiprocessing
from threading import Thread
from BasicOperacion import *

[wxID_PANEL1] = [wx.NewId() for _init_ctrls in range(1)]


audio_lib = audio_library.AudioLibrary()


        
def scale_bitmap(bitmap, width, height):
    image = wx.ImageFromBitmap(bitmap)
    image = image.Scale(width, height, wx.IMAGE_QUALITY_HIGH)
    result = wx.BitmapFromImage(image)
    return result

def print_event(sender, earg):
    print "TerminÛ audio en " + str(earg)
    global audio_lib
    print str(audio_lib.reproduciendo[int(earg['id'])])
    audio_lib.reproduciendo[int(earg['id'])]=True
    print "audio_lib:"+str(audio_lib.reproduciendo[int(earg['id'])])

audio_lib.finished += print_event

class Panel1(wx.Panel):
  


    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Panel.__init__(self, id=wxID_PANEL1, name='', parent=prnt,
              pos=wx.Point(0,0), size=wx.Size(0, 0),
              style=wx.NO_BORDER)
        #self.SetClientSize(wx.Size(419, 134))
        

        self.box_tot = wx.BoxSizer(orient=wx.VERTICAL)#rows=4, cols=1, hgap=0, vgap=0)
        box_up= wx.BoxSizer(orient=wx.HORIZONTAL) # tiene los indicadores de arriba
        self.box_left= wx.BoxSizer(orient=wx.VERTICAL)  # tiene el espacio para ejercicios
        box_right= wx.BoxSizer(orient=wx.VERTICAL) # tiene el sem√°foro

        box_down= wx.BoxSizer(orient=wx.HORIZONTAL)
        box_down.Add(self.box_left,0,wx.ALIGN_TOP,0)
        box_down.Add(box_right,0,wx.ALIGN_TOP,0)

        self.box_tot.Add(box_up)
        self.box_tot.Add(box_down)



        staticText1 = wx.StaticText(
              label=u'Escribe la letra...', name='staticText1', parent=self,
              pos=wx.Point(0, 10), size=wx.Size(108, 17), style=0)
        self.box_left.Add(staticText1, 0, wx.ALIGN_TOP, 0)

        textCtrl1 = wx.TextCtrl(
              parent=self, pos=wx.Point(10, 40), size=wx.Size(80, 32), style=0,
              value='textCtrl1')
        textCtrl1.Value= ""
        self.box_left.Add(textCtrl1, 0, wx.ALIGN_TOP, 0)

        staticBitmap1 = wx.StaticBitmap(bitmap=wx.NullBitmap,
              name='staticBitmap1', parent=self,
              pos=wx.Point(0, 0), size=wx.Size(30, 20), style=0)
        staticBitmap1.SetBitmap(wx.Bitmap('keyboard.png'))
        staticBitmap1.SetBitmap(scale_bitmap(wx.Bitmap('keyboard.png'), 30, 10))

        box_up.Add(staticBitmap1, 0, wx.ALIGN_TOP, 0)


        staticBitmap2 = wx.StaticBitmap(bitmap=wx.NullBitmap,
              name='staticBitmap2', parent=self,
              pos=wx.Point(110, 20), size=wx.Size(182, 229), style=0)
        staticBitmap2.SetBitmap(wx.Bitmap('barra_progreso.png'))
        staticBitmap2.SetBitmap(scale_bitmap(wx.Bitmap('barra_progreso.png'), 20, 60))

        box_right.Add(staticBitmap2, 0, wx.ALIGN_TOP, 0)
        
        self.pareado= False
        self.nombre_ingresado=False
        
        self.mayus= False
        self.tilde=False
        self.SetAutoLayout(True)
        self.SetSizer(self.box_tot)
        self.Layout()
        self.Refresh()
        
        

    def __init__(self, parent, Id, pos, size, style, name, numero_audifono, Alumno):
        self._init_ctrls(parent)
        
        
        self.numero_audifono= numero_audifono
        audio_lib.reproduciendo[int(self.numero_audifono)]=False
        self.Alumno_actual= Alumno
        self.reglas_main= Reglas()
        
        operacion= BasicOperacion()
        operacion.TipoOperacion= TipoOperacion.Reproduccion_letras_alfabeto
        operacion.nivelOperacion= 1
        operacion.feedback_correcto= "First"
        self.Operacion_actual= operacion
        
        """
        HOST = 'localhost'
        PORT = 7388
        BUFSIZE = 1024
        ADDR = (HOST, PORT)

        tcpCliSock = socket()
        tcpCliSock.connect(ADDR)

        print 'conectando'
        data = "SustantivosFinal.multik"
        tcpCliSock.send(data)


        print 'recibiendo1'
        data = tcpCliSock.recv(BUFSIZE)
        if not data: sys.exit(0)
        print data


        print 'conectando'
        data = "30/1"
        tcpCliSock.send(data)

        print 'recibiendo2'
        data = tcpCliSock.recv(BUFSIZE)
        if not data: sys.exit(0)
        print data

        
        return

        #tcpCliSock.close()

        """
        
        '''
        s = socket(AF_INET, SOCK_STREAM)         # Create a socket object
        #host = socket.gethostname() # Get local machine name
        #port = 7388
        print 'conectando con servicio'
        server_address = ('localhost', 7388)
        BUFSIZE= 1024
        s.connect(server_address)
        print 'conectado'
        #s.sendall("/media/Disco Local/Dropbox/magister/Github/MultiK/code/Windows Service/Servicio Final/SustantivosFinal.multik")
        #data= input('asd')
        s.send(bytes('sdfds'))
        print 'enviado'

        #s.setblocking(True) # not really needed but to emphasize this 
                                #is a blocking socket until the timeout
        #s.settimeout(15)

        while True:
            try:
                data= 'asd'
                s.send(bytes(data),'UTF-8')
            
                msg = s.recv(1024)
                print(msg)
                content += msg
                break
            except socket.timeout:
                print 'timeout'
            else:
                print 'murio por alguna razon'#socket died for another reason or ended the way it was supposed to.
        s.close()


        #temp= 'mensaje: '+s.recv(1).strip()
        print 'recibido1'
        #print temp
        print 'recibido2'
        '''
        

        #print operacion.TipoOperacion
        #print operacion.nivelOperacion
        #print TipoOperacion.Reproduccion_letras_alfabeto
        self.Operacion_actual= self.reglas_main.GetSiguienteOperacion(self.Operacion_actual, self.Alumno_actual)
              
        self.CreateGrid(self.Operacion_actual)
        
        
    def CreateGrid(self, operacion):
        
        self.ResetLayout()
        
        if self.pareado == False:
            self.parear()
            return
        
        if operacion.TipoOperacion == TipoOperacion.Reproduccion_letras_alfabeto:
            #print operacion.nivelOperacion
            if operacion.nivelOperacion == 1:
                self.reproduccion_letras_alfabeto1(operacion)
            elif operacion.nivelOperacion ==2:
                self.reproduccion_letras_alfabeto2(operacion)
                
        elif operacion.TipoOperacion == TipoOperacion.sentido_vocales_silabas:
            
            if operacion.nivelOperacion ==1:
                self.sentido_vocales1(operacion)
        
        elif operacion.TipoOperacion == TipoOperacion.signos_int_excl:
            if operacion.nivelOperacion ==1:
                self.signos_int_excl1(operacion)
            elif operacion.nivelOperacion ==2:
                self.signos_int_excl2(operacion)
                
        elif operacion.TipoOperacion == TipoOperacion.mayus_nombres_propios:
            if operacion.nivelOperacion ==1:
                self.mayus_nombres_propios1(operacion)
            elif operacion.nivelOperacion ==2:
                self.mayus_nombres_propios2(operacion)
                
        elif operacion.TipoOperacion == TipoOperacion.patrones_ort_comunes:
            if operacion.nivelOperacion ==1:
                self.patrones_ort_comunes1(operacion)            
            elif operacion.nivelOperacion ==2:
                self.patrones_ort_comunes2(operacion)
            elif operacion.nivelOperacion ==3:
                self.patrones_ort_comunes3(operacion)
            elif operacion.nivelOperacion ==4:
                self.patrones_ort_comunes4(operacion)
            elif operacion.nivelOperacion ==5:
                self.patrones_ort_comunes5(operacion)

        self.Refresh()
                
        

    def ResetLayout(self):
        self.box_left.Clear(True)
        
        staticText1 = wx.StaticText(
              label=u'', name='staticText1', parent=self,
              pos=wx.Point(0, 10), size=wx.Size(108, 47), style=0)
        self.box_left.Add(staticText1, 0, wx.ALIGN_TOP, 0)


        

    def reproduccion_letras_alfabeto1(self,operacion):        
        self.box_left.GetChildren()[0].GetWindow().SetLabel(operacion.pregunta)
        self.TexttoSpeech(operacion.audio_pregunta)
        
        textCtrl1 = wx.TextCtrl(
              parent=self, pos=wx.Point(10, 40), size=wx.Size(80, 32), style=0,
              value='textCtrl1')
        textCtrl1.Value= ""
        self.box_left.Add(textCtrl1, 0, wx.ALIGN_TOP, 0)
        
        
        
    def reproduccion_letras_alfabeto2(self,operacion):
        
        self.box_left.GetChildren()[0].GetWindow().SetLabel("")
        
        self.TexttoSpeech(operacion.audio_pregunta)
        
        lista= wx.ListBox(parent=self, pos=wx.Point(10, 40), size=wx.Size(80, 62), style=0)        

        for st in operacion.alternativas:
            lista.Append(st)

        self.box_left.Add(lista, 0, wx.ALIGN_TOP, 0)
        
        
    
    def sentido_vocales1(self, operacion):        
        print "sentido"
        self.box_left.GetChildren()[0].GetWindow().SetLabel("")
        
        self.TexttoSpeech(operacion.audio_pregunta)
        
        lista= wx.ListBox(parent=self, pos=wx.Point(10, 40), size=wx.Size(80, 62), style=0)
        
        for st in operacion.alternativas:
            lista.Append(st)

        self.box_left.Add(lista, 0, wx.ALIGN_TOP, 0)
    
    
    def signos_int_excl1(self, operacion):        
        
        self.box_left.GetChildren()[0].GetWindow().SetLabel(operacion.pregunta)
        
        self.TexttoSpeech(operacion.audio_pregunta)
        
        textCtrl1 = wx.TextCtrl(
              parent=self, pos=wx.Point(10, 40), size=wx.Size(80, 32), style=0,
              value='textCtrl1')
        textCtrl1.Value= ""
        self.box_left.Add(textCtrl1, 0, wx.ALIGN_TOP, 0)
        

    def signos_int_excl2(self, operacion):        
        
        self.TexttoSpeech(operacion.audio_pregunta)
        
        self.box_left.Clear(True)
        
        
        textCtrl1 = wx.TextCtrl(
              parent=self, pos=wx.Point(10, 40), size=wx.Size(80, 32), style=0,
              value='textCtrl1')
        textCtrl1.Value= ""
        self.box_left.Add(textCtrl1, 0, wx.ALIGN_TOP, 0)
        
        staticText1 = wx.StaticText(
              label=u'', name='staticText1', parent=self,
              pos=wx.Point(0, 10), size=wx.Size(108, 17), style=0)
        self.box_left.Add(staticText1, 0, wx.ALIGN_TOP, 0)
        
        textCtrl2 = wx.TextCtrl(
              parent=self, pos=wx.Point(10, 40), size=wx.Size(80, 32), style=0,
              value='textCtrl2')
        textCtrl2.Value= ""
        self.box_left.Add(textCtrl2, 0, wx.ALIGN_TOP, 0)
        
        return
    
    def mayus_nombres_propios1(self, operacion):        
        
        self.box_left.GetChildren()[0].GetWindow().SetLabel("")
        
        self.TexttoSpeech(operacion.audio_pregunta)
        
        lista= wx.ListBox(parent=self, pos=wx.Point(10, 40), size=wx.Size(80, 32), style=0)
        
        for st in operacion.alternativas:
            lista.Append(st)
        
    # pendiente
    def mayus_nombres_propios2(self, operacion):        
        
        return
    
    def patrones_ort_comunes1(self, operacion):        
        
        self.box_left.GetChildren()[0].GetWindow().SetLabel(operacion.pregunta)
        
        self.TexttoSpeech(operacion.audio_pregunta)
        
        lista= wx.ListBox(parent=self, pos=wx.Point(10, 40), size=wx.Size(80, 32), style=0)
        
        for st in operacion.alternativas:
            lista.Append(st)
        
    
    def patrones_ort_comunes2(self, operacion):        
        
        self.box_left.GetChildren()[0].GetWindow().SetLabel(operacion.pregunta)
        
        textCtrl1 = wx.TextCtrl(
              parent=self, pos=wx.Point(10, 40), size=wx.Size(80, 32), style=0,
              value='textCtrl1')
        textCtrl1.Value= ""
        self.box_left.Add(textCtrl1, 0, wx.ALIGN_TOP, 0)
        
        self.TexttoSpeech(operacion.audio_pregunta)
    
    def patrones_ort_comunes3(self, operacion):        
        
        # Falta imagen!!
        
        self.box_left.GetChildren()[0].GetWindow().SetLabel(operacion.pregunta)
        
        self.TexttoSpeech(operacion.audio_pregunta)
        
        lista= wx.ListBox(parent=self, pos=wx.Point(10, 40), size=wx.Size(80, 32), style=0)
        
        for st in operacion.alternativas:
            lista.Append(st)
        
    
    def patrones_ort_comunes4(self, operacion):        
        
        self.box_left.GetChildren()[0].GetWindow().SetLabel(operacion.pregunta)
        
        self.TexttoSpeech(operacion.audio_pregunta)
        
        lista= wx.ListBox(parent=self, pos=wx.Point(10, 40), size=wx.Size(80, 32), style=0)
        
        for st in operacion.alternativas:
            lista.Append(st)
    
    def patrones_ort_comunes5(self, operacion):        
        
        self.box_left.GetChildren()[0].GetWindow().SetLabel(operacion.pregunta)
        
        textCtrl1 = wx.TextCtrl(
              parent=self, pos=wx.Point(10, 40), size=wx.Size(80, 32), style=0,
              value='textCtrl1')
        textCtrl1.Value= ""
        self.box_left.Add(textCtrl1, 0, wx.ALIGN_TOP, 0)
        
        self.TexttoSpeech(operacion.audio_pregunta)
        return


    ##########  PAREAMIENTO ##############
    
    def set_nombre(self):
        self.ResetLayout()
        self.Operacion_actual.audio_pregunta= "Ingresa tu nombre"
        
        self.box_left.GetChildren()[0].GetWindow().SetLabel("Ingresa tu nombre")
        self.TexttoSpeech(self.Operacion_actual.audio_pregunta)
        
        textCtrl1 = wx.TextCtrl(
              parent=self, pos=wx.Point(10, 40), size=wx.Size(80, 32), style=0,
              value='textCtrl1')
        textCtrl1.Value= ""
        self.box_left.Add(textCtrl1, 0, wx.ALIGN_TOP, 0)
    
        self.Refresh()
        
    def parear(self):
        
        self.ResetLayout()
        
        self.Operacion_actual.audio_pregunta= "Escribe el n˙mero"+str(self.numero_audifono)
        self.box_left.GetChildren()[0].GetWindow().SetLabel("")
        
        self.TexttoSpeech(self.Operacion_actual.audio_pregunta)
        
        textCtrl1 = wx.TextCtrl(
              parent=self, pos=wx.Point(10, 40), size=wx.Size(80, 32), style=0,
              value='textCtrl1')
        textCtrl1.Value= ""
        self.box_left.Add(textCtrl1, 0, wx.ALIGN_TOP, 0)
        
        self.Refresh()      
        
    def ModificarPareamiento(self, diccionario, earg):
        
        text= str(earg['char']).decode('utf-8')
        text= self.arreglar_texto(text)
        
        if self.pareado== True and self.nombre_ingresado==False:
            textctrl= self.box_left.GetChildren()[1].GetWindow()
            if text=="Enter" and len(textctrl.Value)>0:
                temp_nombre= textctrl.Value
                nombre_caps= temp_nombre.title()
                self.Alumno_actual.Nombre= nombre_caps
                self.nombre_ingresado=True
                self.Operacion_actual.RespuestaCorrecta()
                self.Operacion_actual= self.reglas_main.GetSiguienteOperacion(self.Operacion_actual, self.Alumno_actual)
                wx.CallAfter(self.CreateGrid,self.Operacion_actual)
                
        elif self.pareado== False and self.nombre_ingresado==False:
            textctrl= self.box_left.GetChildren()[1].GetWindow()
            if text=="Enter" and len(textctrl.Value)>0:
                temp= int(textctrl.Value)
                
                if temp>=0 and temp< len(diccionario):
                    self.numero_audifono=temp
                    self.pareado=True
                    self.set_nombre()
                    
        # reconocimiento de backspace para borrado
        
        if text == "Back": # backspace captura
                self.box_left.GetChildren()[1].GetWindow().Value=self.box_left.GetChildren()[1].GetWindow().Value[:-1]
                return
        
        strr= self.box_left.GetChildren()[1].GetWindow().Value
        self.box_left.GetChildren()[1].GetWindow().Value=strr+text   

        '''
        
         if ((e.Equals("0") || e.Equals("1") || e.Equals("2") || e.Equals("3") || e.Equals("4") || e.Equals("5")
                || e.Equals("6") || e.Equals("7") || e.Equals("8") || e.Equals("9")) && pareado == false)
            {              

                if (stackpanel1.Children[0] is TextBox)
                    (stackpanel1.Children[0] as TextBox).Text += e;
            }

            else if ((e.Equals("Q") || e.Equals("W") || e.Equals("E") || e.Equals("R") || e.Equals("T") || e.Equals("Y") || e.Equals("U") || e.Equals("I") || e.Equals("O") || e.Equals("P") ||
              e.Equals("A") || e.Equals("S") || e.Equals("D") || e.Equals("F") || e.Equals("G") || e.Equals("H") || e.Equals("J") || e.Equals("K") || e.Equals("L") || e.Equals("—") ||
              e.Equals("Z") || e.Equals("X") || e.Equals("C") || e.Equals("V") || e.Equals("B") || e.Equals("N") || e.Equals("M") ||
              e.Equals("·") || e.Equals("È") || e.Equals("Ì") || e.Equals("Û") || e.Equals("˙")) && pareado == true)
            {
                if (stackpanel1.Children[0] is TextBox && !soundDevice.IsPlaying())
                    (stackpanel1.Children[0] as TextBox).Text += e.ToUpper();
            }
        
        
        '''
        
        
            
    
    

    def Keyboard_Pressed(self, sender, earg):

        text= str(earg['char']).decode('utf-8')
        text= self.arreglar_texto(text)
        
        if len(text)==0:
            return

        if text == "Enter":
            
            if ((self.Operacion_actual.TipoOperacion == TipoOperacion.Reproduccion_letras_alfabeto and self.Operacion_actual.nivelOperacion == 2) or
                (self.Operacion_actual.TipoOperacion == TipoOperacion.mayus_nombres_propios and self.Operacion_actual.nivelOperacion == 1) or
                (self.Operacion_actual.TipoOperacion == TipoOperacion.patrones_ort_comunes and self.Operacion_actual.nivelOperacion == 1) or
                (self.Operacion_actual.TipoOperacion == TipoOperacion.patrones_ort_comunes and self.Operacion_actual.nivelOperacion == 3) or
                (self.Operacion_actual.TipoOperacion == TipoOperacion.patrones_ort_comunes and self.Operacion_actual.nivelOperacion == 4) or
                (self.Operacion_actual.TipoOperacion == TipoOperacion.sentido_vocales_silabas)):
                
                if isinstance(self.box_left.GetChildren()[1].GetWindow(),wx.ListBox):
                    
                    list= self.box_left.GetChildren()[1].GetWindow()
                    if len(list.GetSelections())>0:
                        if list.Items[list.GetSelections()[0]] == self.Operacion_actual.respuesta:
                            list.Clear()
                            list.Append(self.Operacion_actual.feedback_correcto)
                            self.TexttoSpeech(self.Operacion_actual.feedback_correcto)
                            self.Operacion_actual.RespuestaCorrecta()

                        else:
                            list.Clear()
                            list.Append(self.Operacion_actual.feedback_error)
                            self.TexttoSpeech(self.Operacion_actual.feedback_error)
                            self.Operacion_actual.RespuestaIncorrecta()
            
            elif ((self.Operacion_actual.TipoOperacion == TipoOperacion.Reproduccion_letras_alfabeto and self.Operacion_actual.nivelOperacion == 1) or
                (self.Operacion_actual.TipoOperacion == TipoOperacion.signos_int_excl and self.Operacion_actual.nivelOperacion == 1) or
                (self.Operacion_actual.TipoOperacion == TipoOperacion.patrones_ort_comunes and self.Operacion_actual.nivelOperacion == 2) or
                (self.Operacion_actual.TipoOperacion == TipoOperacion.patrones_ort_comunes and self.Operacion_actual.nivelOperacion == 5)):
                
                #textctrl= wx.TextCtrl
                textctrl= self.box_left.GetChildren()[1].GetWindow()
                
                if self.Operacion_actual.TipoOperacion == TipoOperacion.signos_int_excl:
                    resp= self.Operacion_actual.respuesta.split(",")
                    if ((resp[0] in textctrl.Value) and (resp[1] in textctrl.Value)):
                        textctrl.Value= self.Operacion_actual.respuesta
                        
                if textctrl.Value == self.Operacion_actual.respuesta:
                    self.TexttoSpeech(self.Operacion_actual.feedback_correcto)
                    self.Operacion_actual.RespuestaCorrecta()
                    textctrl.Value=""
                else:
                    self.TexttoSpeech(self.Operacion_actual.feedback_error)
                    self.Operacion_actual.RespuestaIncorrecta()
                    textctrl.Value=""
                    
            self.Operacion_actual= self.reglas_main.GetSiguienteOperacion(self.Operacion_actual, self.Alumno_actual)
            wx.CallAfter(self.CreateGrid,self.Operacion_actual)
           

        #if self.box_left.GetChildren()[1].GetWindow().Value == None:
        #    self.box_left.GetChildren()[1].GetWindow().SetValue('')


        if isinstance(self.box_left.GetChildren()[1].GetWindow(),wx.ListBox):
            if text == "-v" or text == "-^":

                if text == "-v":

                    if len(self.box_left.GetChildren()[1].GetWindow().GetSelections()) ==0:
                        self.box_left.GetChildren()[1].GetWindow().Select(0)
                        
                    else:
                        num=self.box_left.GetChildren()[1].GetWindow().GetSelections()[0]

                        if num == self.box_left.GetChildren()[1].GetWindow().GetCount()-1:
                            self.box_left.GetChildren()[1].GetWindow().Select(0)
                        else:
                            self.box_left.GetChildren()[1].GetWindow().Select(num+1)

                elif text == "-^":
                    if len(self.box_left.GetChildren()[1].GetWindow().GetSelections()) ==0:
                        cont=self.box_left.GetChildren()[1].GetWindow().GetCount()-1
                        self.box_left.GetChildren()[1].GetWindow().Select(cont)
                    else:
                        num=self.box_left.GetChildren()[1].GetWindow().GetSelections()[0]

                        if num==0:
                            cont=self.box_left.GetChildren()[1].GetWindow().GetCount()-1
                            self.box_left.GetChildren()[1].GetWindow().Select(cont)
                        else:
                            self.box_left.GetChildren()[1].GetWindow().Select(num-1)



            self.Refresh()


        try:
            
            if text == "Back": # backspace captura
                self.box_left.GetChildren()[1].GetWindow().Value=self.box_left.GetChildren()[1].GetWindow().Value[:-1]
                return

            if isinstance(self.box_left.GetChildren()[1].GetWindow(),wx.TextCtrl):
                strr= self.box_left.GetChildren()[1].GetWindow().Value
                #wx.CallAfter(self.box_left.GetChildren()[1].GetWindow().SetValue(strr+text))
                self.box_left.GetChildren()[1].GetWindow().Value=strr+text



        except TypeError as e:
            print "Error: %s" % str(e)
        except UnicodeDecodeError as e:
            print "Error: %s" % str(e)
        except:
            print "Unexpected error:"#, sys.exc_info()[0]

        #if text == 'Down':

        self.Refresh()
 
    lib_play_proc = None
    
    
    
    def arreglar_texto(self, texto):
               
        return texto
    
        # Reconocimiento de signos de interrogacion y exclamaciÛn
        
        if self.mayus:
            if texto== "'":
                texto="?"
            elif texto== "ø":
                texto="°"
            elif texto=="1":
                texto="!"
            self.mayus=False
        
        if self.tilde:
            if texto=="a":
                texto="·"
            elif texto=="e":
                texto="È"
            elif texto=="i":
                texto="Ì"
            elif texto=="o":
                texto="Û"
            elif texto=="u":
                texto="˙"
            self.mayus=False
            self.tilde=False
            
            
        # Reconocimiento de tildes
        
        if texto=="tilde":
            self.tilde=True
        
        if texto=="mayus":
            self.mayus=True
            texto=""
            
        return texto
        
            
                
            
            
    def RepetirPregunta(self):
    	print "Repetir pregunta"
    	print self.Operacion_actual.audio_pregunta
        self.TexttoSpeech(self.Operacion_actual.audio_pregunta)            
        
    
       
    def TexttoSpeech(self, text_to_speech):
        print "reproduciendo"
        #if audio_lib.reproduciendo[self.numero_audifono]==False:
        if self.lib_play_proc is None:
            self.text_to_speech_queue = multiprocessing.Queue()
            self.lib_play_proc = multiprocessing.Process(target=audio_lib.play, args=(self.numero_audifono, self.text_to_speech_queue))
            self.lib_play_proc.start()          
        
        if len(text_to_speech)>0:
            print "Reproduciendo en aud√≠fono #%s: \"%s\"" % (self.numero_audifono, text_to_speech)
            audio_lib.reproduciendo[int(self.numero_audifono)]=True
            print str(self.numero_audifono)+" "+str(audio_lib.reproduciendo[self.numero_audifono])
            self.text_to_speech_queue.put(text_to_speech)
        
        


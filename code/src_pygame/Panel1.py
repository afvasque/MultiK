# coding=utf-8
#Boa:FramePanel:Panel1
import lector_csv




        


class Panel1(wx.Panel):
  
    numero_alumno = {}

    def _init_ctrls(self, prnt):
        
        
        
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
        #Diccionario que relaciona el numero de lista con el nombre del alumno
        numero_alumno = obtener_lista("3B")               
        self._init_ctrls(parent)
        

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
        self.Operacion_actual.audio_pregunta= "Ingresa tu número de lista"
        
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
        
        self.Operacion_actual.audio_pregunta= "Escribe el número"+str(self.numero_audifono)
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
                
                # Buscamos el numero de lista en el CSV del curso
                temp_numero= textctrl.Value
                self.Alumno_actual.Nombre= numero_alumno[temp_numero]
                
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

  
        if self.lib_play_proc is None:
            self.text_to_speech_queue = multiprocessing.Queue()
            self.lib_play_proc = multiprocessing.Process(target=audio_lib.play, args=(self.numero_audifono, self.text_to_speech_queue))
            self.lib_play_proc.daemon = True # BETA
            self.lib_play_proc.start()          
        
        if len(text_to_speech)>0:
            #print "Reproduciendo en audí­fono #%s: \"%s\"" % (self.numero_audifono, text_to_speech)
            audio_lib.reproduciendo[int(self.numero_audifono)]=True
            #print str(self.numero_audifono)+" "+str(audio_lib.reproduciendo[self.numero_audifono])
            self.text_to_speech_queue.put(text_to_speech)


        


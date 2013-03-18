# coding=utf-8
#Boa:FramePanel:Panel1

import wx
import os
import audio_library
from Reglas import *
from BasicOperacion import *

[wxID_PANEL1] = [wx.NewId() for _init_ctrls in range(1)]

audio_lib = audio_library.AudioLibrary()

def scale_bitmap(bitmap, width, height):
    image = wx.ImageFromBitmap(bitmap)
    image = image.Scale(width, height, wx.IMAGE_QUALITY_HIGH)
    result = wx.BitmapFromImage(image)
    return result

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
        box_right= wx.BoxSizer(orient=wx.VERTICAL) # tiene el semáforo

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

        self.SetAutoLayout(True)
        self.SetSizer(self.box_tot)
        self.Layout()
        
        

    def __init__(self, parent, Id, pos, size, style, name, numero_audifono, Alumno):
        self._init_ctrls(parent)
        
        
        self.numero_audifono= numero_audifono
        self.Alumno_actual= Alumno
        self.reglas_main= Reglas()
        
        operacion= BasicOperacion()
        operacion.TipoOperacion= TipoOperacion.Reproduccion_letras_alfabeto
        operacion.nivelOperacion= 1
        operacion.feedback_correcto= "first"
        self.Operacion_actual= operacion
        
        self.Operacion_actual= self.reglas_main.GetSiguienteOperacion(self.Operacion_actual, self.Alumno_actual)

        
        
        self.CreateGrid(self.Operacion_actual)
        
        
    def CreateGrid(self, operacion):
        
        self.ResetLayout()
        
        if operacion.TipoOperacion is TipoOperacion.Reproduccion_letras_alfabeto:
            
            if operacion.nivelOperacion ==1:
                self.reproduccion_letras_alfabeto1(operacion)
            elif operacion.nivelOperacion ==2:
                self.reproduccion_letras_alfabeto2(operacion)
                
        elif operacion.TipoOperacion is TipoOperacion.sentido_vocales_silabas:
            
            if operacion.nivelOperacion ==1:
                self.sentido_vocales1(operacion)
        
        elif operacion.TipoOperacion is TipoOperacion.signos_int_excl:
            if operacion.nivelOperacion ==1:
                self.signos_int_excl1(operacion)
            elif operacion.nivelOperacion ==2:
                self.signos_int_excl2(operacion)
                
        elif operacion.TipoOperacion is TipoOperacion.mayus_nombres_propios:
            if operacion.nivelOperacion ==1:
                self.mayus_nombres_propios1(operacion)
            elif operacion.nivelOperacion ==2:
                self.mayus_nombres_propios2(operacion)
                
        elif operacion.TipoOperacion is TipoOperacion.patrones_ort_comunes:
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
                
        

    def ResetLayout(self):
        self.box_left.Clear(True)
        
        
        staticText1 = wx.StaticText(
              label=u'', name='staticText1', parent=self,
              pos=wx.Point(0, 10), size=wx.Size(108, 17), style=0)
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
        
        self.box_left.GetChildren()[0].GetWindow().SetLabel("dsa")
        
        self.TexttoSpeech(operacion.audio_pregunta)
        
        lista= wx.ListBox(parent=self, pos=wx.Point(10, 40), size=wx.Size(80, 32), style=0)

        lista.Append("1")
        lista.Append("2")
        lista.Append("3")

        for st in operacion.alternativas:
            lista.Append(st)
        
        
    
    def sentido_vocales1(self, operacion):        
        
        self.box_left.GetChildren()[0].GetWindow().SetLabel("")
        
        self.TexttoSpeech(operacion.audio_pregunta)
        
        lista= wx.ListBox(parent=self, pos=wx.Point(10, 40), size=wx.Size(80, 32), style=0)
        
        for st in operacion.alternativas:
            lista.Append(st)
    
    
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

    

    def Keyboard_Pressed(self, sender, earg):

        text= str(earg[1])
        

        if text is "Enter":
            audio_lib.play(self.numero_audifono, self.textCtrl1.Value)
            self.textCtrl1.Value=""
            return

        if text is '^H': # backspace captura
            self.textCtrl1.Value= self.textCtrl1.Value[:-1]
            return
        
        if isinstance(self.box_left.GetChildren()[1].GetWindow(),wx.TextCtrl):
            strr= self.box_left.GetChildren()[1].GetWindow().Value
            wx.CallAfter(self.box_left.GetChildren()[1].GetWindow().SetValue(strr+text))

        if text is 'Down':

        if isinstance(self.box_left.GetChildren()[1].GetWindow(),wx.ListBox):

            return

    
    def TexttoSpeech(self, st):
        
        if len(st)>0:
            audio_lib.play(self.numero_audifono, st)            
            return
        
        


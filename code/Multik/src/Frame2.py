# coding=utf-8
#Boa:Frame:Frame2

import wx
from Panel1 import Panel1
import usb.core
import threading
import math
import keyboard_library
import event

def create(parent):
    return Frame2(parent)

[wxID_FRAME2, wxID_FRAME2PANEL1, wxID_FRAME1PANEL2,
] = [wx.NewId() for _init_ctrls in range(3)]

lib = keyboard_library.KeyboardLibrary()
diccionario= {}

class Frame2(wx.Frame): 
    
    
    @staticmethod
    def Keyboard_event(sender, earg):
        diccionario[int(earg[0])].Keyboard_Pressed(sender,earg)
        print str(earg[0])+"id: "+earg[1]  # 0: id, 1: teclas
        
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME2, name='', parent=prnt,
              pos=wx.Point(0, 0), size=wx.Size(0, 0),
              style=wx.DEFAULT_FRAME_STYLE, title='Frame2')
        
        #box_tot= wx.BoxSizer(wx.VERTICAL)
        
        #box_tot.SetDimension(0,0,500,200)
        
        lib.keypress += self.Keyboard_event
        keyboardsNum= len(lib.keyboard_array)
        print "teclados: "+str(keyboardsNum)
        
        
        line_number= int(math.sqrt(keyboardsNum))
        
        if math.floor(math.sqrt(keyboardsNum)) < math.sqrt(keyboardsNum):
            line_number+=1
        
        box_tot = wx.GridSizer(rows=line_number, cols=line_number, hgap=0, vgap=0)
        
        for x in range(0,keyboardsNum,line_number):
                    
            #box_hor = wx.BoxSizer(wx.HORIZONTAL)
            #box_hor = wx.GridSizer(rows=1, cols=line_number, hgap=0, vgap=0)
            
            temp = keyboardsNum - x
            
            if temp > line_number: 
                temp = line_number;
        
            for y in range(x,x+temp):
                panel1 = Panel1(id=wxID_FRAME1PANEL2, name='panel'+str(y), parent=self,
                      pos=wx.Point(0, 0), size=wx.Size(0, 0), number=y,
                      style=wx.NO_BORDER)
                box_tot.Add(panel1, 0, wx.ALIGN_TOP, 0)
                diccionario[y]=panel1
                
            
            #box_tot.Add(box_hor)
        
        '''    
        panel2 = Panel1(id=wxID_FRAME1PANEL2, name='panel2', parent=self,
              pos=wx.Point(100, 0), size=wx.Size(100, 100),
              style=wx.TAB_TRAVERSAL)
        '''
        
        
        #box.Add(panel2,1,wx.EXPAND)
        
        self.SetAutoLayout(True)
        self.SetSizer(box_tot)
        self.Layout()
        
        '''
        self.panel1 = wx.Panel(id=wxID_FRAME2PANEL1, name='panel1', parent=self,
              pos=wx.Point(0, 0), size=wx.Size(519, 234),
              style=wx.TAB_TRAVERSAL)
        '''

    def __init__(self, parent):     
        
        lib.detect(0x0e8f,0x0022)
        lib.configure()
        
        self._init_ctrls(parent)
        
        t = ThreadKeyboard()
        t.start()
        
      
        
   

    def OnTextCtrl1KeyUp(self, event):
        keycode = event.GetKeyCode()
        
        if keycode== wx.WXK_RETURN:
            self.textCtrl1.Value="ar"
    
  
class ThreadKeyboard(threading.Thread):
    def run(self):
        lib.start(0x0e8f,0x0022)
        

if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = create(None)
    frame.Show() 

    app.MainLoop()

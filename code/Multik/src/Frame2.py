#Boa:Frame:Frame2

import wx
from Panel1 import Panel1
import e4
import usb.core
import threading
import math

def create(parent):
    return Frame2(parent)

[wxID_FRAME2, wxID_FRAME2PANEL1, wxID_FRAME1PANEL2,
] = [wx.NewId() for _init_ctrls in range(3)]

class Frame2(wx.Frame): 
    
    diccionario= {}
    
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME2, name='', parent=prnt,
              pos=wx.Point(0, 0), size=wx.Size(1000, 600),
              style=wx.DEFAULT_FRAME_STYLE, title='Frame2')
        
        box_tot= wx.BoxSizer(wx.VERTICAL)
        box_tot.SetDimension(0,0,1000,600)
        
        keyboardsNum= len(e4.Keyboard.keyboard_array)
        print "teclados: "+str(keyboardsNum)
        
        line_number= int(math.sqrt(keyboardsNum))
        
        if math.floor(math.sqrt(keyboardsNum)) < math.sqrt(keyboardsNum):
            line_number+=1
        
        
        for x in range(0,keyboardsNum,line_number):
                    
            box_hor = wx.BoxSizer(wx.HORIZONTAL)
            
            temp = keyboardsNum - x
            
            if temp > line_number: 
                 temp = line_number;
        
            for y in range(x,x+temp):
                panel1 = Panel1(id=wxID_FRAME1PANEL2, name='panel'+str(y), parent=self,
                      pos=wx.Point(0, 0), size=wx.Size(100, 100),
                      style=wx.TAB_TRAVERSAL)
                box_hor.Add(panel1,1,wx.EXPAND)
                self.diccionario[e4.Keyboard.keyboard_array[y]]=panel1
                
            
            box_tot.Add(box_hor)
        
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
        e4.Keyboard.detect(0x04D9,0x1603)
        self._init_ctrls(parent)
      
        
        
        
        
        
        
        
        
        
        
        
        
        
        t = ThreadKeyboard()
        t.start()
        
   

    def OnTextCtrl1KeyUp(self, event):
        keycode = event.GetKeyCode()
        
        if keycode== wx.WXK_RETURN:
            self.textCtrl1.Value=""
    
  
class ThreadKeyboard(threading.Thread):
    def run(self):
        #Display the keyboard input
        while True:
            for (i,kb) in enumerate(e4.Keyboard.keyboard_array):   # i is the index and kb the Keyboard object
                try:
                    data = kb._endpoint.read(kb._endpoint.wMaxPacketSize, 10) # timeout is the last argument
                    
                    # map the input to a character
                    map_keys = lambda c: e4.key_pages_shift[c[1]] if c[0] is 2 else e4.key_pages[c[1]]
                    data2 = "".join(map(map_keys, [(d[0], d[2]) for d in e4.chunks(data, 8)]))

                    # print the character
                    print "#" + str(i) + " : " + data2
                except usb.core.USBError as e:
                    pass
        

if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = create(None)
    frame.Show() 

    app.MainLoop()

#Boa:Frame:Frame2

import wx
from Panel1 import Panel1

def create(parent):
    return Frame2(parent)

[wxID_FRAME2, wxID_FRAME2PANEL1, wxID_FRAME1PANEL2,
] = [wx.NewId() for _init_ctrls in range(3)]

class Frame2(wx.Frame): 

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME2, name='', parent=prnt,
              pos=wx.Point(0, 0), size=wx.Size(1000, 600),
              style=wx.DEFAULT_FRAME_STYLE, title='Frame2')
        
        box_tot= wx.BoxSizer(wx.VERTICAL)
        box_tot.SetDimension(0,0,1000,600)
        
        for x in range(1,7):
                    
            box_hor = wx.BoxSizer(wx.HORIZONTAL)
        
            for y in range(1,7):
                panel1 = Panel1(id=wxID_FRAME1PANEL2, name='panel'+str(y), parent=self,
                      pos=wx.Point(0, 0), size=wx.Size(100, 100),
                      style=wx.TAB_TRAVERSAL)
                box_hor.Add(panel1,1,wx.EXPAND)
            
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
        self._init_ctrls(parent)

    def OnTextCtrl1KeyUp(self, event):
        keycode = event.GetKeyCode()
        
        if keycode== wx.WXK_RETURN:
            self.textCtrl1.Value=""
    
  


if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = create(None)
    frame.ShowFullScreen(True, style= wx.DEFAULT_FRAME_STYLE | 
                         wx.NO_FULL_REPAINT_ON_RESIZE | wx.FULLSCREEN_ALL) 

    app.MainLoop()

#Boa:Frame:Frame1

import wx
import os

def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1PANEL1, wxID_FRAME1STATICBITMAP1, 
 wxID_FRAME1STATICBITMAP2, wxID_FRAME1STATICTEXT1, wxID_FRAME1TEXTCTRL1, 
] = [wx.NewId() for _init_ctrls in range(6)]

def scale_bitmap(bitmap, width, height):
    image = wx.ImageFromBitmap(bitmap)
    image = image.Scale(width, height, wx.IMAGE_QUALITY_HIGH)
    result = wx.BitmapFromImage(image)
    return result

class Frame1(wx.Frame):
    

    
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(457, 255), size=wx.Size(519, 234),
              style=wx.DEFAULT_FRAME_STYLE, title='Frame1')
        self.SetClientSize(wx.Size(519, 234))

        self.panel1 = wx.Panel(id=wxID_FRAME1PANEL1, name='panel1', parent=self,
              pos=wx.Point(0, 0), size=wx.Size(519, 234),
              style=wx.TAB_TRAVERSAL)

        self.staticText1 = wx.StaticText(id=wxID_FRAME1STATICTEXT1,
              label=u'Escribe la letra..', name='staticText1',
              parent=self.panel1, pos=wx.Point(24, 96), size=wx.Size(108, 17),
              style=0)

        self.textCtrl1 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL1, name='textCtrl1',
              parent=self.panel1, pos=wx.Point(60, 144), size=wx.Size(80, 32),
              style=0, value='textCtrl1')
        self.textCtrl1.Bind(wx.EVT_KEY_UP, self.OnTextCtrl1KeyUp)

        self.staticBitmap1 = wx.StaticBitmap(bitmap=wx.NullBitmap,
              id=wxID_FRAME1STATICBITMAP1, name='staticBitmap1',
              parent=self.panel1, pos=wx.Point(160, 48), size=wx.Size(332, 124),
              style=0)
        self.staticBitmap1.SetBitmap(wx.Bitmap('keyboard.png'))

        self.staticBitmap2 = wx.StaticBitmap(bitmap=wx.NullBitmap,
              id=wxID_FRAME1STATICBITMAP2, name='staticBitmap2',
              parent=self.panel1, pos=wx.Point(180, 80), size=wx.Size(182,
              529), style=0)
        self.staticBitmap2.SetBitmap(wx.Bitmap('barra_progreso.png'))

    def __init__(self, parent):
        self._init_ctrls(parent)
        self.textCtrl1.Value= ""
        self.staticBitmap1.SetBitmap(scale_bitmap(wx.Bitmap('keyboard.png'), 50, 20))
        self.staticBitmap2.SetBitmap(scale_bitmap(wx.Bitmap('barra_progreso.png'), 30, 100))

    def tts(self,text):
        return os.system("echo "+text+" | festival --tts")

    def OnTextCtrl1KeyUp(self, event):
        keycode = event.GetKeyCode()
        
        if keycode== wx.WXK_RETURN:
            self.tts(self.textCtrl1.Value)            
            self.textCtrl1.Value=""
    
    


if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = create(None)
    frame.Show()

    app.MainLoop()
